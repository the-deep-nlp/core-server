"""core_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from analysis_module.views.analysis_module import (
    topic_modeling,
    summarization,
    ngrams,
    geolocation,
    request_status,
)
from analysis_module.views.predictions import (
    tags_mapping,
    entry_classification,
    nlp_tags,
)
from analysis_module.views.text_extraction import text_extraction
from core.views import token_auth_dummy_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/topicmodel/", topic_modeling),
    path("api/v1/summarization/", summarization),
    path("api/v1/text-extraction/", text_extraction),
    path("api/v1/ngrams/", ngrams),
    path("api/v1/geolocation/", geolocation),
    path("api/v1/tags-mapping/", tags_mapping),
    path("api/v1/nlp-tags/", nlp_tags),
    path("api/v1/entry-classification/", entry_classification),
    path("api/v1/analysismodule/status/<uuid:unique_id>/", request_status),
    path("api/v1/test-auth/", token_auth_dummy_view),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
