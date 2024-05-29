import io

import pandas as pd

from common.enums import Columns, CalculatingValues
from report.services.analyze_file import ExcelDataProcessor
from report.models import Report


class GenerateExcelFile:
    """
    Класс для генерации Excel файла на основе данных из DataFrame и фильтрации по дате.

    Атрибуты:
        excel_solver (ExcelDataProcessor): Объект для обработки данных из DataFrame.

    Методы:
        __init__(data_frame, filter_date):
            Инициализирует объект GenerateExcelFile с данными и датой фильтрации.

        _generate_dict_with_repost():
            Генерирует словарь с результатами анализа данных.

        _prepare_data():
            Подготавливает данные для генерации Excel файла и сохраняет результаты в базу данных.

        generate_excel_file():
            Генерирует Excel файл и возвращает его в виде байтового потока.
    """
    def __init__(self, data_frame, filter_date):
        """
        Инициализирует объект GenerateExcelFile с данными и датой фильтрации.

        Аргументы:
            data_frame (DataFrame): Исходный DataFrame с данными из Excel.
            filter_date (str): Дата для фильтрации данных в формате 'год-месяц-день'.
        """
        self.excel_solver = ExcelDataProcessor(data_frame=data_frame, filter_date=filter_date)

    def _generate_dict_with_repost(self):
        """
        Генерирация словаря с результатами анализа данных.
        """
        methods = [
            ('application_count', lambda: self.excel_solver.get_applications_count()),
            ('application_count_filtered', lambda: self.excel_solver.get_applications_count(is_filtered_by_date=True)),
            ('duplicate_count',
             lambda: self.excel_solver.get_definite_columns_count(column=Columns.APPLICATION_STATE.value,
                                                                  value=CalculatingValues.DUPLICATE.value)),
            ('duplicate_count_filtered',
             lambda: self.excel_solver.get_definite_columns_count(column=Columns.APPLICATION_STATE.value,
                                                                  value=CalculatingValues.DUPLICATE.value,
                                                                  is_filtered_by_date=True)),
            ('addition_count',
             lambda: self.excel_solver.get_definite_columns_count(column=Columns.APPLICATION_STATE.value,
                                                                  value=CalculatingValues.ADDITION.value)),
            ('addition_count_filtered',
             lambda: self.excel_solver.get_definite_columns_count(column=Columns.APPLICATION_STATE.value,
                                                                  value=CalculatingValues.ADDITION.value,
                                                                  is_filtered_by_date=True)),
            ('extension_count',
             lambda: self.excel_solver.get_definite_columns_count(column=Columns.APPLICATION_STATE.value,
                                                                  value=CalculatingValues.EXTENSION.value)),
            ('extension_count_filtered',
             lambda: self.excel_solver.get_definite_columns_count(column=Columns.APPLICATION_STATE.value,
                                                                  value=CalculatingValues.EXTENSION.value,
                                                                  is_filtered_by_date=True)),
            ('pending_count',
             lambda: self.excel_solver.get_definite_columns_count(column=Columns.APPLICATION_STATUS.value,
                                                                  value=CalculatingValues.PENDING.value)),
            ('pending_count_filtered',
             lambda: self.excel_solver.get_definite_columns_count(column=Columns.APPLICATION_STATUS.value,
                                                                  value=CalculatingValues.PENDING.value,
                                                                  is_filtered_by_date=True)),
            ('success_processing_count',
             lambda: self.excel_solver.get_definite_columns_count(column=Columns.APPLICATION_STATUS.value,
                                                                  value=CalculatingValues.SUCCESS_PROCESSING.value)),
            ('success_processing_count_filtered',
             lambda: self.excel_solver.get_definite_columns_count(column=Columns.APPLICATION_STATUS.value,
                                                                  value=CalculatingValues.SUCCESS_PROCESSING.value,
                                                                  is_filtered_by_date=True)),
            ('processing_count',
             lambda: self.excel_solver.get_definite_columns_count(column=Columns.APPLICATION_STATUS.value,
                                                                  value=CalculatingValues.PROCESSING.value)),
            (
                'processing_count_filtered',
                lambda: self.excel_solver.get_definite_columns_count(column=Columns.APPLICATION_STATUS.value,
                                                                     value=CalculatingValues.PROCESSING.value,
                                                                     is_filtered_by_date=True)),
            ('package_count', lambda: self.excel_solver.get_unique_columns_count(value=Columns.PACKAGE_ID.value)),
            (
                'package_count_filtered',
                lambda: self.excel_solver.get_unique_columns_count(value=Columns.PACKAGE_ID.value,
                                                                   is_filtered_by_date=True)),
            ('auth_count', lambda: self.excel_solver.get_unique_columns_count(value=Columns.APPLICATION_AUTHOR.value)),
            ('auth_count_filtered',
             lambda: self.excel_solver.get_unique_columns_count(value=Columns.APPLICATION_AUTHOR.value,
                                                                is_filtered_by_date=True))
        ]
        self.results = dict()

        for key, method in methods:
            self.results[key] = method()

    def _prepare_data(self):
        self._generate_dict_with_repost()
        Report.objects.create(**self.results)

        data = {
            'Название': [
                'Загруженных заявок', 'Дубли', 'На создание', 'На расширение', 'Возвращена на уточнение',
                'Отправлена в обработку', 'Пакетов', 'Пользователей', 'Обработка завершена'
            ],
            'За указанный период': [self.results.get('application_count_filtered'),
                                    self.results.get('duplicate_count_filtered'),
                                    self.results.get('addition_count_filtered'),
                                    self.results.get('extension_count_filtered'),
                                    self.results.get('pending_count_filtered'),
                                    self.results.get('processing_count_filtered'),
                                    self.results.get('package_count_filtered'),
                                    self.results.get('auth_count_filtered'),
                                    self.results.get('success_processing_count_filtered'),
                                    ],
            'За все время': [self.results.get('application_count'), self.results.get('duplicate_count'),
                             self.results.get('addition_count'), self.results.get('extension_count'),
                             self.results.get('pending_count'), self.results.get('processing_count'),
                             self.results.get('package_count'), self.results.get('auth_count'),
                             self.results.get('success_processing_count'),
                             ]
        }
        self.results = data

    def generate_excel_file(self):
        """
        Генерирует Excel файл и возвращает его в виде байтового потока.

        Возвращает:
            BytesIO: Байтовый поток с данными Excel файла.
        """
        self._prepare_data()
        df = pd.DataFrame(self.results)
        bio = io.BytesIO()
        writer = pd.ExcelWriter(bio, engine='xlsxwriter')
        df.to_excel(writer, index=False)
        writer._save()
        bio.seek(0)
        return bio
