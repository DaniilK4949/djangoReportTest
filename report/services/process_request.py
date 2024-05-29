import io

import pandas as pd
from django.http import HttpResponse

from report.services.generate_excel_file import GenerateExcelFile


def create_excel_response(request, time_filter):
    """
       Обрабатывает запрос на создание Excel файла на основе загруженного файла и фильтра по дате.

       Аргументы:
           request (Request): HTTP запрос, содержащий загруженный файл.
           time_filter (str): Дата в формате 'год-месяц-день', используемая для фильтрации данных.

       Возвращает:
           HttpResponse: Ответ с файлом Excel, содержащим отфильтрованные данные.

       Пример использования:
           response = create_excel_response(request, '2023-08-18')
           Возвращает HTTP ответ с прикрепленным файлом myfile.xlsx
    """
    file = request.FILES['file']
    df = pd.read_excel(io.BytesIO(file.read()))
    solver = GenerateExcelFile(data_frame=df, filter_date=time_filter)
    bio = solver.generate_excel_file()
    response = HttpResponse(bio, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=myfile.xlsx'
    return response
