import datetime
import warnings

from ast import literal_eval
from tqdm import tqdm
from typing import List, Optional

import numpy as np
import polars as pl
from evidently.report import Report
from evidently.metrics import DatasetDriftMetric

warnings.filterwarnings("ignore")


class FeatureDrift:
    """
    Calculates per project feature drift of excerpts
    Input: Dataframe with columns 'project_id', 'embeddings'
    Output: Dataframe containing columns
    """

    def __init__(self, ref_df: pl.DataFrame, cur_df: pl.DataFrame) -> None:
        self.reference_df = ref_df
        self.current_df = cur_df
        self.data_drift_dataset_report = Report(metrics=[DatasetDriftMetric()])

    def _process_embeddings(self, embeddings: pl.Series) -> List:
        """
        Reads the embeddings and gets the list
        Input: Embeddings Series
        Output: Embeddings List
        """
        if isinstance(embeddings[0], list):
            return embeddings.apply(np.array).to_list()
        return embeddings.apply(literal_eval).apply(np.array).to_list()

    def _project_id_based_mask(
        self, dataframe: pl.DataFrame, project_id: Optional[int] = None
    ) -> pl.DataFrame:
        if project_id:
            dataframe = dataframe.filter(pl.col("project_id") == project_id)
        return dataframe

    def compute_feature_drift(
        self,
        ref_n_samples: int = 500,
        cur_n_samples: int = 500,
        random_state: int = 5432,
    ) -> pl.DataFrame:
        """
        Computes the Feature drift on the excerpts embeddings at project level
        """
        final_result = []
        reference_project_ids = list(self.reference_df["project_id"].unique())
        current_project_ids = list(self.current_df["project_id"].unique())

        for project_id in tqdm(reference_project_ids):
            if project_id in current_project_ids:
                reference_df = self._project_id_based_mask(
                    self.reference_df, project_id
                )
                current_df = self._project_id_based_mask(self.current_df, project_id)

                if len(reference_df["embeddings"]) and len(current_df["embeddings"]):
                    reference_embedding_lst = self._process_embeddings(
                        reference_df["embeddings"]
                    )
                    current_embedding_lst = self._process_embeddings(
                        current_df["embeddings"]
                    )
                    # Note that sample size is less by 1 because it should less than population size
                    ref_n_samples = (
                        len(reference_embedding_lst) - 1
                        if ref_n_samples >= len(reference_embedding_lst)
                        else ref_n_samples
                    )
                    cur_n_samples = (
                        len(current_embedding_lst) - 1
                        if cur_n_samples >= len(current_embedding_lst)
                        else cur_n_samples
                    )

                    reference_df = (
                        pl.DataFrame(reference_embedding_lst)
                        .transpose()
                        .sample(n=ref_n_samples, seed=random_state)
                    )
                    current_df = (
                        pl.DataFrame(current_embedding_lst)
                        .transpose()
                        .sample(n=cur_n_samples, seed=random_state)
                    )

                    self.data_drift_dataset_report.run(
                        reference_data=reference_df.to_pandas(),
                        current_data=current_df.to_pandas(),
                    )

                    temp_result = {}
                    temp_result["reference_project_id"] = project_id
                    temp_result["current_project_id"] = project_id
                    temp_result["reference_dataset_len"] = len(reference_df)
                    temp_result["current_dataset_len"] = len(current_df)
                    data_drift_report = self.data_drift_dataset_report.as_dict()
                    # Note the keys might change in the future
                    temp_result["drift_share"] = data_drift_report["metrics"][0][
                        "result"
                    ]["drift_share"]
                    temp_result["number_of_columns"] = data_drift_report["metrics"][0][
                        "result"
                    ]["number_of_columns"]
                    temp_result["number_of_drifted_columns"] = data_drift_report[
                        "metrics"
                    ][0]["result"]["number_of_drifted_columns"]
                    temp_result["share_of_drifted_columns"] = temp_result[
                        "drift_share"
                    ] = data_drift_report["metrics"][0]["result"][
                        "share_of_drifted_columns"
                    ]
                    temp_result["dataset_drift"] = temp_result[
                        "drift_share"
                    ] = data_drift_report["metrics"][0]["result"]["dataset_drift"]
                    temp_result["generated_at"] = datetime.date.today()
                    final_result.append(temp_result)

        return pl.DataFrame._from_records(final_result)


if __name__ == "__main__":
    reference_data_path = "/home/rsh/projects/deepl/model-monitoring/csvfiles/data_with_embeddings_22000.csv"
    current_data_path = "/home/rsh/projects/deepl/model-monitoring/csvfiles/sampled_data_with_embeddings_testset.csv"

    reference_data_df = pl.read_csv(reference_data_path)
    current_data_df = pl.read_csv(current_data_path)

    feature_drift = FeatureDrift(reference_data_df, current_data_df)
    df = feature_drift.compute_feature_drift(ref_n_samples=5, cur_n_samples=5)
    print(df)
    print(df.columns)
