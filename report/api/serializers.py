import re

from rest_framework import serializers


class UploadFileSerializer(serializers.Serializer):
    file = serializers.FileField()
    time_filter = serializers.CharField(max_length=10)

    def validate_time_filter(self, value):
        pattern = r'^\d{4}-\d{2}-\d{2}$'
        if re.match(pattern, value):
            return value
        raise serializers.ValidationError('Строка должно иметь формат год-месяц-день.')
