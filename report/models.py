from django.db import models


class Report(models.Model):
    """
    Модель для хранения данных отчета.

    Атрибуты:
        application_count (int): Количество загруженных заявок.
        application_count_filtered (int): Количество загруженных заявок за указанный период.
        duplicate_count (int): Количество дубликатов.
        duplicate_count_filtered (int): Количество дубликатов за указанный период.
        addition_count (int): Количество заявок на создание.
        addition_count_filtered (int): Количество заявок на создание за указанный период.
        extension_count (int): Количество заявок на расширение.
        extension_count_filtered (int): Количество заявок на расширение за указанный период.
        pending_count (int): Количество заявок, возвращенных на уточнение.
        pending_count_filtered (int): Количество заявок, возвращенных на уточнение за указанный период.
        success_processing_count (int): Количество успешно обработанных заявок.
        success_processing_count_filtered (int): Количество успешно обработанных заявок за указанный период.
        processing_count (int): Количество заявок, отправленных в обработку.
        processing_count_filtered (int): Количество заявок, отправленных в обработку за указанный период.
        package_count (int): Количество уникальных пакетов.
        package_count_filtered (int): Количество уникальных пакетов за указанный период.
        auth_count (int): Количество уникальных авторов заявок.
        auth_count_filtered (int): Количество уникальных авторов заявок за указанный период.
    """
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

