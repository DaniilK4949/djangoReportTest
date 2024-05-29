from django.urls import path
from rest_framework.routers import DefaultRouter

from report.api.views import ReportViewSet, ReportListView

router = DefaultRouter()
router.register(r'results', ReportListView, basename='report')

urlpatterns = [
    path('upload-file/', ReportViewSet.as_view({"post": "post"}), name="upload-file"),
    *router.urls,
]
