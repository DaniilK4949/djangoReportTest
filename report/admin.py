from django.contrib import admin

from report.models import Report


@admin.register(Report)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ['processing_count']
