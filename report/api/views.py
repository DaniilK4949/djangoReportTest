from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ViewSet

from report.api.serializers import UploadFileSerializer, ReportSerializer
from report.models import Report
from report.services.process_request import create_excel_response


class ReportViewSet(ViewSet):
    """
        ViewSet для загрузки файла и генерации отчета.

        Методы:
            post(request):
                Обрабатывает POST-запрос для загрузки файла,
                выполнения вычислений и возврата отчета в формате Excel.
        """
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = UploadFileSerializer

    @extend_schema(
        request={
            'multipart/form-data': {
                'type': 'object',
                'properties': {
                    'file': {
                        'type': 'string',
                        'format': 'binary',
                    },
                    'time_filter': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'A datetime filter for processing the file'
                    }
                },
                'required': ['file', 'time_filter']
            }
        },
        responses={
            status.HTTP_200_OK: {
                'type': 'object',
                'properties': {
                    'file': {
                        'type': 'file',
                    }
                }
            }
        },
        examples=[
            OpenApiExample(
                'File Upload Example',
                summary='Example of file upload',
                description='Upload a file with description and a datetime filter',
                value={
                    'file': '(binary content)',
                    'time_filter': '2024-05-28'
                }
            )
        ]
    )
    def post(self, request):
        serializer = UploadFileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        time_filter = serializer.validated_data.get('time_filter')
        response = create_excel_response(request=request, time_filter=time_filter)
        return response


class ReportListView(ModelViewSet):
    """
    Эндпоинт для получения всех данных отчетов.

    Attributes:
        queryset: Запрос к модели Report для получения всех данных отчетов.
        serializer_class: Класс сериализатора для отчетов.
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    http_method_names = ['get']
