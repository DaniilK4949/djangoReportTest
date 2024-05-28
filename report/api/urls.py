from django.urls import path

from report.api.views import ReportViewSet

urlpatterns = [
    path('upload-file/', ReportViewSet.as_view({"post": "post"}), name="upload-file")
]
