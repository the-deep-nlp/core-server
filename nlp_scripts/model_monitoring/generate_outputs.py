import json
import logging
from typing import Dict, Optional, Tuple, Any

import boto3
import polars as pl
import numpy as np

from .utils import invoke_model_endpoint, group_tags
from .constants import CATEGORIES

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ClassificationModelOutput:
    """
    Classify excerpts to a defined list of tags and also generates embeddings
    """

    def __init__(
        self,
        dataframe: pl.DataFrame,
        batch_size: int = 2,
        prediction_generation: bool = True,
        embeddings_generation: bool = True,
        aws_access_key_id: Optional[str] = None,
        aws_secret_access_key: Optional[str] = None,
        endpoint_name: str = "",
        region_name: str = "us-east-1",
    ):
        # Note: AWS Creds should not be used when deployed in AWS
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.dataframe = dataframe
        self.batch = len(self.dataframe) // batch_size
        self.prediction_generation = prediction_generation
        self.embeddings_generation = embeddings_generation
        self.embeddings = []
        self.predictions = []
        self.thresholds = []
        self.endpoint_name = endpoint_name
        self.sagemaker_client = boto3.session.Session().client(
            "sagemaker-runtime",
            region_name=region_name,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )

    def _get_model_inputs(self, excerpts: list) -> Dict[str, Any]:
        """
        Build the model input data
        """
        processed_excerpts = [
            [str(x).encode().decode("utf-8", errors="ignore") for x in excerpt]
            for excerpt in excerpts
        ]
        excerpt_df: pl.DataFrame = pl.DataFrame({"excerpt": processed_excerpts})
        model_in_df = excerpt_df.with_columns(
            return_type=pl.lit(["default_analyis"]),
            analyis_framework_id=pl.lit(["all"]),
            interpretability=pl.lit([False]),
            ratio_interpreted_labels=pl.lit([0.5]),
            return_prediction_labels=pl.lit([self.prediction_generation]),
            output_backbone_embeddings=pl.lit([self.embeddings_generation]),
            pooling_type=pl.lit(["['mean_pooling']"]),
            finetuned_task=pl.lit(["['first_level_tags']"]),
            embeddings_return_type=pl.lit(["array"]),
        )
        return model_in_df.to_pandas().to_json(orient="split", force_ascii=False)

    def get_clean_outputs(self, prediction_dict: Dict, thresholds_dict: Dict) -> Dict:
        """
        Generates clean outputs
        """
        clean_predictions = {}
        for key, value in prediction_dict.items():
            if prediction_dict[key] >= thresholds_dict[key]:
                clean_predictions[key] = value

        return clean_predictions

    def get_model_outputs(self, excerpt: list) -> Tuple[list, list]:
        """
        Get the model outputs
        """
        model_preds_output = []
        model_embeddings_output = [[]]
        model_inputs = self._get_model_inputs(excerpt)
        outputs = invoke_model_endpoint(
            backbone_inputs=model_inputs,
            sagemaker_model=self.sagemaker_client,
            endpoint_name=self.endpoint_name,
        )
        if (
            self.prediction_generation
            and "raw_predictions" in outputs
            and "thresholds" in outputs
        ):
            predictions = outputs["raw_predictions"]
            thresholds = outputs["thresholds"]
            for prediction in predictions:
                clean_op = self.get_clean_outputs(prediction, thresholds)
                model_preds_output.append(clean_op)
        if self.embeddings_generation and "output_backbone" in outputs:
            model_embeddings_output = outputs["output_backbone"]

        return model_preds_output, model_embeddings_output

    def generate_outputs(self) -> pl.DataFrame:
        """
        Generates the dataframe consisting of predictions and embeddings based on settings
        """
        prediction_df = pl.DataFrame()
        embeddings_df = pl.DataFrame()

        for entries_batch in np.array_split(self.dataframe, self.batch):
            op_lst = []
            batch_model_pred_op, batch_model_emb_op = self.get_model_outputs(
                entries_batch.tolist()
            )
            if self.prediction_generation:
                for batch_model_output in batch_model_pred_op:
                    grouped_tags = group_tags(batch_model_output)
                    o = {
                        item: grouped_tags[item]
                        if item in grouped_tags.keys()
                        else []
                        for item in CATEGORIES
                    }
                    op_lst.append(o)
                if prediction_df.is_empty():
                    prediction_df = pl.DataFrame(op_lst)
                else:
                    prediction_df = pl.concat([prediction_df, pl.DataFrame(op_lst)])

            if self.embeddings_generation:
                if embeddings_df.is_empty():
                    embeddings_df = pl.DataFrame({"embeddings": batch_model_emb_op})
                else:
                    embeddings_df = pl.concat(
                        [
                            embeddings_df,
                            pl.DataFrame({"embeddings": batch_model_emb_op}),
                        ]
                    )

        prediction_df = prediction_df.rename({key: f"{key}_pred" for key in CATEGORIES})
        return pl.concat(
            [self.dataframe, prediction_df, embeddings_df], how="horizontal"
        )


if __name__ == "__main__":
    test_excerpt = [
        "There has been a health crisis in Ukraine",
        "Pesticides has been all around the year affecting Kenyan Health",
        "Lots of people are migrating due to violence in Sahara desert.",
        "There are air strikes due to which people are fleeing and many have been hospitalized.",
    ]
    dff = pl.DataFrame({"excerpt": test_excerpt})
    cm = ClassificationModelOutput(dff, endpoint_name="main-model-cpu-new-test")
    op = cm.generate_outputs()
