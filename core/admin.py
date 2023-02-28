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
    ProjectWisePerfMatrices,
    AllProjectPerfMatrics,
    CategoryWiseMatchRatios,
    ProjectWiseMatchRatios,
    TagWisePerfMatrics,
    ClassificationModel,
    ComputedFeatureDrift,
)


admin.site.register(ToFetchProject)
admin.site.register(Lead)
admin.site.register(Entry)
admin.site.register(AFMapping)
admin.site.register(Organization)
admin.site.register(Project)
admin.site.register(DeepDataFetchTracker)


admin.site.register(ClassificationPredictions)
admin.site.register(ProjectWisePerfMatrices)
admin.site.register(CategoryWiseMatchRatios)

admin.site.register(ProjectWiseMatchRatios)
admin.site.register(TagWisePerfMatrics)
admin.site.register(ClassificationModel)
admin.site.register(ComputedFeatureDrift)


class AllProjectMatrics(admin.ModelAdmin):
    list_display=['categories', 'precision', 'recall', 'support', 'f1score', 'generated_at']

admin.site.register(AllProjectPerfMatrics, AllProjectMatrics)