from django.db import models


class Report(models.Model):
    application_count = models.FloatField()
    application_count_filtered = models.FloatField()
    duplicate_count = models.FloatField()
    duplicate_count_filtered = models.FloatField()
    addition_count = models.FloatField()
    addition_count_filtered = models.FloatField()
    extension_count = models.FloatField()
    extension_count_filtered = models.FloatField()
    pending_count = models.FloatField()
    pending_count_filtered = models.FloatField()
    processing_count = models.FloatField()
    processing_count_filtered = models.FloatField()
    package_count = models.FloatField()
    package_count_filtered = models.FloatField()
    success_processing_count = models.FloatField()
    success_processing_count_filtered = models.FloatField()
    auth_count = models.FloatField()
    auth_count_filtered = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

