import json
from typing import List, Dict
import pandas as pd

from .first_level_tags import FirstLevel
from .second_level_tags import SecondLevel
from .third_level_tags import ThirdLevel
from .classification_inference_postprocessing import get_outputs_from_endpoint
# from .utils import get_tag_ids

from .postprocess_tags import convert_current_dict_to_previous_one
from .tags_to_ids import get_model_tags_mappings

total_tags = [
    FirstLevel.first_level_lst(),
    SecondLevel.second_level_lst(),
    ThirdLevel.third_level_lst(),
]


class ModelTagsPrediction:
    """
    Class to get the prediction from the classification model
    """

    def __init__(self, endpoint_name: str = "main-model-cpu"):
        """
        Input: endpoint_name: Name of the endpoint in sagemaker where the model is deployed
        """
        self.endpoint_name = endpoint_name

    def get_model_predictions(self, input_df: pd.DataFrame) -> Dict:
        """
        Gets the Model tags predictions
        """
        model_outputs = get_outputs_from_endpoint(input_df, self.endpoint_name)
        if not model_outputs:
            return []
        raw_outputs = json.loads(model_outputs)
        raw_preds = raw_outputs["raw_predictions"]
        thresholds = raw_outputs["thresholds"]

        tags_pred = convert_current_dict_to_previous_one(raw_preds[0])
        tags_threshold = convert_current_dict_to_previous_one(thresholds)
        preds = get_model_tags_mappings(tags_pred, tags_threshold)

        return preds

        # tag_preds_lst = []

        # for pred in raw_preds:
        #     tag_preds = {}
        #     for label, prob in pred.items():
        #         firstlabel, secondlabel, thirdlabel = get_tag_ids(
        #             total_tags, label.split("->")
        #         )
        #         if not (firstlabel and secondlabel and thirdlabel):
        #             continue
        #         if firstlabel not in tag_preds:
        #             tag_preds[firstlabel] = {}
        #         if secondlabel not in tag_preds[firstlabel]:
        #             tag_preds[firstlabel][secondlabel] = {}
        #         if thirdlabel not in tag_preds[firstlabel][secondlabel]:
        #             tag_preds[firstlabel][secondlabel][thirdlabel] = {
        #                 "prediction": prob,
        #                 "threshold": thresholds[label],
        #                 "is_selected": prob > thresholds[label],
        #             }
        #     tag_preds_lst.append(tag_preds)

        # final_tag_preds_lst = []
        # for entry_id, preds in zip(input_df["client_id"], tag_preds_lst):
        #     final_tag_preds_lst.append({"client_id": entry_id, "model_preds": preds})

        # return final_tag_preds_lst

    def __call__(self, excerpts: List[Dict]):
        return self.get_model_predictions(
            pd.DataFrame(excerpts).rename(columns={"entry": "excerpt"})
        )
