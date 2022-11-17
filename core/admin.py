from django.contrib import admin

from core.models import (
    ToFetchProject,
    Lead,
    Entry,
    AFMapping,
    Organization,
    Project,
)


admin.site.register(ToFetchProject)
admin.site.register(Lead)
admin.site.register(Entry)
admin.site.register(AFMapping)
admin.site.register(Organization)
admin.site.register(Project)
