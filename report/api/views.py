import io

import pandas
from django.http import HttpResponse
from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ViewSet

from report.api.serializers import UploadFileSerializer
from report.services.generate_excel_file import GenerateExcelFile


class ReportViewSet(ViewSet):
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
        file = request.FILES['file']
        df = pandas.read_excel(io.BytesIO(file.read()))
        solver = GenerateExcelFile(data_frame=df, filter_date=serializer.validated_data.get('time_filter'))
        bio = solver.generate_excel_file()
        response = HttpResponse(bio, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=myfile.xlsx'
        return response
