from collections import namedtuple
from enum import Enum

version = "1.0"

FirstLevelCategories = namedtuple(
    "FirstLevelCategories", ["id", "key", "version", "has_parent", "parent_id", "alias"]
)


class FirstLevel(Enum):
    SubsectorsTag = FirstLevelCategories(
        id="1",
        key="subsectors",
        version=version,
        has_parent=False,
        parent_id=None,
        alias="Subsectors",
    )
    FirstLevelTag = FirstLevelCategories(
        id="2",
        key="first_level_tags",
        version=version,
        has_parent=False,
        parent_id=None,
        alias="First Level Tags",
    )
    Subpillars1DTag = FirstLevelCategories(
        id="3",
        key="subpillars_1d",
        version=version,
        has_parent=False,
        parent_id=None,
        alias="Subpillars 1D",
    )
    Subpillars2DTag = FirstLevelCategories(
        id="4",
        key="subpillars_2d",
        version=version,
        has_parent=False,
        parent_id=None,
        alias="Subpillars 2D",
    )
    SecondaryTags = FirstLevelCategories(
        id="5",
        key="secondary_tags",
        version=version,
        has_parent=False,
        parent_id=None,
        alias="Secondary Tags",
    )

    @classmethod
    def first_level_lst(cls):
        return [
            t.value._asdict()
            for t in [
                FirstLevel.SubsectorsTag,
                FirstLevel.FirstLevelTag,
                FirstLevel.Subpillars1DTag,
                FirstLevel.Subpillars2DTag,
                FirstLevel.SecondaryTags,
            ]
        ]
