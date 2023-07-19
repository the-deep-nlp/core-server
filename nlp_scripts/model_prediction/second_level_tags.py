from collections import namedtuple
from enum import Enum
from .first_level_tags import FirstLevel

SecondLevelCategories = namedtuple(
    "SecondLevelCategories",
    ["id", "key", "version", "has_parent", "parent_id", "alias"],
)
version = "1.0"


class SecondLevel(Enum):
    EducationTag = SecondLevelCategories(
        id="101",
        key="Education",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.SubsectorsTag.value, "id"),
        alias="Education",
    )
    HealthTag = SecondLevelCategories(
        id="102",
        key="Health",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.SubsectorsTag.value, "id"),
        alias="Health",
    )
    LivelihoodsTag = SecondLevelCategories(
        id="103",
        key="Livelihoods",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.SubsectorsTag.value, "id"),
        alias="Livelihoods",
    )
    LogisticsTag = SecondLevelCategories(
        id="104",
        key="Logistics",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.SubsectorsTag.value, "id"),
        alias="Logistics",
    )
    ShelterTag = SecondLevelCategories(
        id="105",
        key="Shelter",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.SubsectorsTag.value, "id"),
        alias="Shelter",
    )
    NutritionTag = SecondLevelCategories(
        id="106",
        key="Nutrition",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.SubsectorsTag.value, "id"),
        alias="Nutrition",
    )
    ProtectionTag = SecondLevelCategories(
        id="107",
        key="Protection",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.SubsectorsTag.value, "id"),
        alias="Protection",
    )
    WashTag = SecondLevelCategories(
        id="108",
        key="Wash",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.SubsectorsTag.value, "id"),
        alias="Wash",
    )
    SectorsTag = SecondLevelCategories(
        id="201",
        key="sectors",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.FirstLevelTag.value, "id"),
        alias="Sectors",
    )
    Pillars1DTag = SecondLevelCategories(
        id="202",
        key="pillars_1d",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.FirstLevelTag.value, "id"),
        alias="Pillars 1D",
    )
    Pillars2DTag = SecondLevelCategories(
        id="203",
        key="pillars_2d",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.FirstLevelTag.value, "id"),
        alias="Pillars 2D",
    )
    AffectedTag = SecondLevelCategories(
        id="204",
        key="Affected",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.FirstLevelTag.value, "id"),
        alias="Affected",
    )
    CasualtiesTag = SecondLevelCategories(
        id="301",
        key="Casualties",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.Subpillars1DTag.value, "id"),
        alias="Casualties",
    )
    ContextTag = SecondLevelCategories(
        id="302",
        key="Context",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.Subpillars1DTag.value, "id"),
        alias="Context",
    )
    Covid19Tag = SecondLevelCategories(
        id="303",
        key="Covid-19",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.Subpillars1DTag.value, "id"),
        alias="COVID-19",
    )
    DisplacementTag = SecondLevelCategories(
        id="304",
        key="Displacement",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.Subpillars1DTag.value, "id"),
        alias="Displacement",
    )
    HumanitarianAccessTag = SecondLevelCategories(
        id="305",
        key="Humanitarian access",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.Subpillars1DTag.value, "id"),
        alias="Humanitarian Access",
    )
    InfoAndCommTag = SecondLevelCategories(
        id="306",
        key="Information and communication",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.Subpillars1DTag.value, "id"),
        alias="Information and Communication",
    )
    ShockEventTag = SecondLevelCategories(
        id="307",
        key="Shock/event",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.Subpillars1DTag.value, "id"),
        alias="Shock/Event",
    )
    AtRiskTag = SecondLevelCategories(
        id="401",
        key="At risk",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.Subpillars2DTag.value, "id"),
        alias="At Risk",
    )
    CapacitiesAndResponseTag = SecondLevelCategories(
        id="402",
        key="Capacities & response",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.Subpillars2DTag.value, "id"),
        alias="Capacities And Response",
    )
    HumanitarianConditionsTag = SecondLevelCategories(
        id="403",
        key="Humanitarian conditions",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.Subpillars2DTag.value, "id"),
        alias="Humanitarian Conditions",
    )
    ImpactTag = SecondLevelCategories(
        id="404",
        key="Impact",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.Subpillars2DTag.value, "id"),
        alias="Impact",
    )
    PriorityInterventionsTag = SecondLevelCategories(
        id="405",
        key="Priority interventions",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.Subpillars2DTag.value, "id"),
        alias="Priority Interventions",
    )
    PriorityNeedsTag = SecondLevelCategories(
        id="406",
        key="Priority needs",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.Subpillars2DTag.value, "id"),
        alias="Priority Needs",
    )
    DisplacedTag = SecondLevelCategories(
        id="501",
        key="Displaced",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.SecondaryTags.value, "id"),
        alias="Displaced",
    )
    NonDisplacedTag = SecondLevelCategories(
        id="502",
        key="Non displaced",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.SecondaryTags.value, "id"),
        alias="Non Displaced",
    )
    AgeTag = SecondLevelCategories(
        id="503",
        key="Age",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.SecondaryTags.value, "id"),
        alias="Age",
    )
    GenderTag = SecondLevelCategories(
        id="504",
        key="Gender",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.SecondaryTags.value, "id"),
        alias="Gender",
    )
    ReliabilityTag = SecondLevelCategories(
        id="505",
        key="reliability",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.SecondaryTags.value, "id"),
        alias="Reliability",
    )
    SeverityTag = SecondLevelCategories(
        id="506",
        key="severity",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.SecondaryTags.value, "id"),
        alias="Severity",
    )
    SpecificNeedsGroupsTag = SecondLevelCategories(
        id="507",
        key="specific_needs_groups",
        version=version,
        has_parent=True,
        parent_id=getattr(FirstLevel.SecondaryTags.value, "id"),
        alias="Specific Needs Groups",
    )

    @classmethod
    def second_level_lst(cls):
        return [
            t.value._asdict()
            for t in [
                SecondLevel.EducationTag,
                SecondLevel.HealthTag,
                SecondLevel.LivelihoodsTag,
                SecondLevel.LogisticsTag,
                SecondLevel.ShelterTag,
                SecondLevel.NutritionTag,
                SecondLevel.ProtectionTag,
                SecondLevel.WashTag,
                SecondLevel.SectorsTag,
                SecondLevel.Pillars1DTag,
                SecondLevel.Pillars2DTag,
                SecondLevel.AffectedTag,
                SecondLevel.CasualtiesTag,
                SecondLevel.ContextTag,
                SecondLevel.Covid19Tag,
                SecondLevel.DisplacementTag,
                SecondLevel.HumanitarianAccessTag,
                SecondLevel.InfoAndCommTag,
                SecondLevel.ShockEventTag,
                SecondLevel.AtRiskTag,
                SecondLevel.CapacitiesAndResponseTag,
                SecondLevel.HumanitarianConditionsTag,
                SecondLevel.ImpactTag,
                SecondLevel.PriorityInterventionsTag,
                SecondLevel.PriorityNeedsTag,
                SecondLevel.DisplacedTag,
                SecondLevel.NonDisplacedTag,
                SecondLevel.AgeTag,
                SecondLevel.GenderTag,
                SecondLevel.ReliabilityTag,
                SecondLevel.SeverityTag,
                SecondLevel.SpecificNeedsGroupsTag,
            ]
        ]
