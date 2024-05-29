import re

from rest_framework import serializers

from report.models import Report


class UploadFileSerializer(serializers.Serializer):
    """
    Сериализатор для загрузки файла и фильтрации по дате.

    Атрибуты:
        file (FileField): Поле для загрузки файла.
        time_filter (CharField): Поле для фильтрации по дате в формате 'год-месяц-день'.

    Методы:
        validate_time_filter(value):
            Проверяет, что строка имеет формат 'год-месяц-день'.
            Возвращает значение, если оно соответствует формату.
            Вызывает ValidationError, если строка не соответствует формату.
    """

    file = serializers.FileField()
    time_filter = serializers.CharField(max_length=10)

    def validate_time_filter(self, value):
        """
        Проверяет, что строка имеет формат 'год-месяц-день'.

        Аргументы:
            value (str): Значение строки, которую необходимо проверить.

        Возвращает:
            str: Исходное значение, если оно соответствует формату.

        Вызывает:
            ValidationError: Если строка не соответствует формату.
        """
        pattern = r'^\d{4}-\d{2}-\d{2}$'
        if re.match(pattern, value):
            return value
        raise serializers.ValidationError('Строка должно иметь формат год-месяц-день.')


class ReportSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Report.
    """

    class Meta:
        model = Report
        fields = [
            'id',
            'application_count', 'application_count_filtered',
            'duplicate_count', 'duplicate_count_filtered',
            'addition_count', 'addition_count_filtered',
            'extension_count', 'extension_count_filtered',
            'pending_count', 'pending_count_filtered',
            'processing_count', 'processing_count_filtered',
            'package_count', 'package_count_filtered',
            'success_processing_count', 'success_processing_count_filtered',
            'auth_count', 'auth_count_filtered',
            'created_at'
        ]
