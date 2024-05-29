import pandas as pd
import pytest

from common.enums import CalculatingValues, Columns
from report.services.analyze_file import ExcelDataProcessor


class TestExcelDataProcessor:
    """
    Класс для тестирования методов класса ExcelDataProcessor.
    """

    @pytest.fixture
    def dataframe(self):
        """
        Фикстура для загрузки тестового датафрейма.
        """
        file_path = 'dataframe_for_test.xlsx'
        dataframe = pd.read_excel(file_path)
        return dataframe

    @pytest.fixture
    def date_filter(self):
        """
        Фикстура для установки даты фильтрации.
        """
        return '2023-08-22'

    @pytest.fixture
    def processor(self, dataframe, date_filter):
        """
        Фикстура для инициализации объекта ExcelDataProcessor.
        """
        processor = ExcelDataProcessor(dataframe, date_filter)
        return processor

    @pytest.mark.parametrize("time_filter", [
        True,
        False
    ])
    def test_get_applications_count(self, dataframe, date_filter, time_filter, processor):
        """
        Тест метода get_applications_count.

        Проверяет возврат корректного количества записей в датафрейме в зависимости от наличия временного фильтра.

        :param dataframe: тестовый датафрейм
        :param date_filter: временной фильтр
        :param time_filter: флаг использования временного фильтра
        :param processor: экземпляр ExcelDataProcessor
        """
        count = 22 if not time_filter else 12

        data = processor.get_applications_count(is_filtered_by_date=time_filter)  # act

        assert data == count

    @pytest.mark.parametrize("time_filter", [
        True,
        False
    ])
    def test_get_definite_columns_count(self, dataframe, date_filter, time_filter, processor):
        """
        Тест метода get_definite_columns_count.

        Проверяет возврат корректного количества записей в датафрейме по указанным столбцам и значениям в зависимости от наличия временного фильтра.

        :param dataframe: тестовый датафрейм
        :param date_filter: временной фильтр
        :param time_filter: флаг использования временного фильтра
        :param processor: экземпляр ExcelDataProcessor
        """
        count = 2 if not time_filter else 0

        data = processor.get_definite_columns_count(value=CalculatingValues.DUPLICATE.value,
                                                    column=Columns.APPLICATION_STATE.value,
                                                    is_filtered_by_date=time_filter)  # act

        assert data == count

    @pytest.mark.parametrize("time_filter", [
        True,
        False
    ])
    def test_get_unique_columns_count(self, dataframe, date_filter, time_filter, processor):
        """
        Тест метода get_unique_columns_count.

        Проверяет возврат корректного количества уникальных записей в указанном столбце в зависимости от наличия временного фильтра.

        :param dataframe: тестовый датафрейм
        :param date_filter: временной фильтр
        :param time_filter: флаг использования временного фильтра
        :param processor: экземпляр ExcelDataProcessor
        """
        count = 7 if not time_filter else 4

        data = processor.get_unique_columns_count(value=Columns.PACKAGE_ID.value,
                                                  is_filtered_by_date=time_filter)  # act

        assert data == count
