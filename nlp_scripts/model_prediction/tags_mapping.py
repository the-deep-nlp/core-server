from pathlib import Path
from typing import List, Dict
from .nlp_matching_algorithm import af2nlp_matching

from .first_level_tags import FirstLevel
from .second_level_tags import SecondLevel
from .third_level_tags import ThirdLevel
from .utils import get_tag_ids


class AF2NLPMapping:
    """
    Generates the AF-NLP tags mapping
    """

    def __init__(self, mapping_file: str = "mapping_tags_nlp2original.json"):
        self.mapping_file = Path(__file__).parent / mapping_file
        self.total_tags = [
            FirstLevel.first_level_lst(),
            SecondLevel.second_level_lst(),
            ThirdLevel.third_level_lst(),
        ]

    def input_transform(self, inputs: List[Dict]):
        """
        Transforms the input data
        """
        result = []
        for item in inputs:
            tag_hierarchy = "->".join(
                filter(
                    None, [item["widget_title"], item["parent_label"], item["label"]]
                )
            )
            result.append({"client_id": item["client_id"], "input_text": tag_hierarchy})
        return result

    def compute_af2nlp_tags(self, inputs, full_output: bool) -> List[Dict]:
        """
        Computes the DEEP AF to NLP tags
        """
        results = af2nlp_matching(inputs, self.mapping_file)
        temp_items = []
        for item in results.copy():
            if not item["output_text"]:
                temp_items.append(
                    {
                        "client_id": item["client_id"],
                        "input_text": item["input_text"].split("->")[-1],
                    }
                )
                results.remove(item)

        partial_results = af2nlp_matching(temp_items, self.mapping_file)
        results.extend(partial_results)

        for res in results:
            if "output_tagids" not in res:
                res["output_tagids"] = []
            for item in res["output_text"]:
                processed_tags_op = get_tag_ids(self.total_tags, item.split("->"))
                res["output_tagids"].append(
                    processed_tags_op[-1] if not full_output else processed_tags_op
                )
        return results

    def __call__(self, data_inputs: List[Dict], full_output: bool = False):
        """
        Produce the mapped tags results
        """
        transformed_input_data = self.input_transform(data_inputs)
        return self.compute_af2nlp_tags(transformed_input_data, full_output=full_output)


if __name__ == "__main__":
    # Sample
    data = [
        {
            "client_id": "1",
            "label": "nutritional status",
            "widget_title": None,
            "parent_label": "nutrition->",
        },
        {
            "client_id": "2",
            "label": "!health.",
            "widget_title": None,
            "parent_label": None,
        },
        {
            "client_id": 3,
            "label": "subpillars_2d->CONTEXT->Basic infrastructure and social services",
            "widget_title": None,
            "parent_label": None,
        },
    ]

    af2nlp_map = AF2NLPMapping()
    res2 = af2nlp_map(data, full_output=False)
    print(res2)
