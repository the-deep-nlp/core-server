from django.contrib import admin

from core.models import (
    ToFetchProject,
    Lead,
    Entry,
    AFMapping,
    Organization,
    Project,
    DeepDataFetchTracker,
    ClassificationPredictions,
    ProjectWisePerfMetrics,
    AllProjectPerfMetrics,
    CategoryWiseMatchRatios,
    ProjectWiseMatchRatios,
    TagWisePerfMetrics,
    ClassificationModel,
    ComputedFeatureDrift,
)


class ToFetchProjectAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "original_project_id",
        "status",
        "is_added_manually",
    ]


class AfmappingAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "af_name",
        "original_af_id",
        "original_af_tags",
        "nlp_tags",
        "is_mapped_manually",
    ]


class OrganizationAdmin(admin.ModelAdmin):
    search_fields = ['original_organization_id']
    list_display = [
        "id",
        "original_organization_id",
        "name",
        "short_name",
        "long_name",
        "extra",
    ]


class LeadAdmin(admin.ModelAdmin):
    autocomplete_fields = ["project", "authoring_org", "publishing_org"]
    search_fields = ["id"]
    list_display = [
        "id",
        "original_lead_id",
        "title",
        "extraction_status",
        "project",
        "authoring_org",
        "publishing_org",
        "confidentiality",
    ]


class ClassificationModelAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = [
        "name",
        "version",
        "model_uri",
        "description",
        "train_data_uri",
    ]


class ProjectAdmin(admin.ModelAdmin):
    search_fields = ['original_entry_id']
    list_display = [
        "id",
        "original_project_id",
        "af_mapping",
        "title",
        "location",
        "description",
    ]


class EntryAdmin(admin.ModelAdmin):
    search_fields = ['original_entry_id']
    autocomplete_fields = ["lead"]
    list_display = [
        "id",
        "original_entry_id",
        "lead",
        "excerpt_en",
        "original_af_tags"
    ]


class AllProjectMetricsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "categories",
        "precision",
        "recall",
        "support",
        "f1score",
        "generated_at",
    ]


class ClassificationPredictionsAdmin(admin.ModelAdmin):
    autocomplete_fields = ['entry', 'project', 'model']
    list_display = [
        "id",
        "entry",
        "project",
        "subpillars_1d",
        "sectors",
        "subpillars_2d",
        "affected_groups",
        "specific_needs_groups",
        "severity",
    ]


class ProjectWisePerfMetricsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "project_id",
        "sectors_f1score",
        "sectors_precision",
        "sectors_recall",
        "sectors_support",
        "subpillars_1d_f1score",
        "subpillars_1d_precision",
        "subpillars_1d_recall",
        "subpillars_1d_support",
    ]


class CategoryWiseMatchRatiosAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "project_id",
        "entry_id",
        "sectors_completely_matched",
        "sectors_missing",
        "sectors_wrong",
        "subpillars_1d_completely_matched",
        "subpillars_1d_missing",
        "subpillars_1d_wrong",
        "subpillars_2d_completely_matched",
        "subpillars_2d_missing",
        "subpillars_2d_wrong",
    ]


class TagWisePerfMetricsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "tags",
        "precision",
        "recall",
        "f1score",
        "support",
        "generated_at",
    ]


class ProjectWiseMatchRatiosAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "project_id",
        "sectors_completely_matched_mean",
        "sectors_missing_mean",
        "sectors_wrong_mean",
        "subpillars_1d_completely_matched_mean",
        "subpillars_1d_missing_mean",
        "subpillars_1d_wrong_mean",
        "subpillars_2d_completely_matched_mean",
        "subpillars_2d_missing_mean",
        "subpillars_2d_wrong_mean",
        "generated_at",
    ]


class ComputedFeatureDriftAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "reference_project_id",
        "current_project_id",
        "reference_dataset_len",
        "current_dataset_len",
        "drift_share",
        "number_of_columns",
        "number_of_drifted_columns",
        "share_of_drifted_columns",
        "dataset_drift",
        "generated_at",
    ]


admin.site.register(ToFetchProject, ToFetchProjectAdmin)
admin.site.register(AFMapping, AfmappingAdmin)
admin.site.register(DeepDataFetchTracker)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Lead, LeadAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(ClassificationPredictions, ClassificationPredictionsAdmin)
admin.site.register(AllProjectPerfMetrics, AllProjectMetricsAdmin)
admin.site.register(ProjectWisePerfMetrics, ProjectWisePerfMetricsAdmin)
admin.site.register(CategoryWiseMatchRatios, CategoryWiseMatchRatiosAdmin)
admin.site.register(TagWisePerfMetrics, TagWisePerfMetricsAdmin)
admin.site.register(ProjectWiseMatchRatios, ProjectWiseMatchRatiosAdmin)
admin.site.register(ClassificationModel, ClassificationModelAdmin)
admin.site.register(ComputedFeatureDrift, ComputedFeatureDriftAdmin)
