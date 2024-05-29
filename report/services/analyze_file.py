import pandas as pd
from dateutil import tz

from common.enums import Columns


class ExcelDataProcessor:
    """
    Класс для обработки данных из Excel-файла.

    Атрибуты:
        TIMEZONE (tzinfo): Временная зона, используемая для обработки дат (Европа/Москва).
        data_frame (DataFrame): Исходный DataFrame с данными из Excel.
        filter_date (Timestamp): Дата для фильтрации данных.

    Методы:
        __init__(data_frame, filter_date):
            Инициализирует объект ExcelDataProcessor.

        get_applications_count(is_filtered_by_date):
            Возвращает количество заявок.

        get_definite_columns_count(column, value, is_filtered_by_date):
            Возвращает количество записей, содержащих определенное значение в указанном столбце.

        get_unique_columns_count(value, is_filtered_by_date):
            Возвращает количество уникальных значений в указанном столбце.
    """
    TIMEZONE = tz.gettz('Europe / Moscow')

    def __init__(self, data_frame: pd.DataFrame, filter_date: str):
        """
        Инициализирует объект ExcelDataProcessor с данными и датой фильтрации.

        Аргументы:
            data_frame (DataFrame): Исходный DataFrame с данными из Excel.
            filter_date (str): Дата для фильтрации данных в формате 'год-месяц-день'.
        """
        self.data_frame = data_frame
        self.filter_date = pd.Timestamp(filter_date, tzinfo=self.TIMEZONE)
        self.data_frame[Columns.DATE_OF_CREATION.value] = pd.to_datetime(
            self.data_frame[Columns.DATE_OF_CREATION.value], dayfirst=True)

    def get_applications_count(self, is_filtered_by_date: bool = False):
        """
        Возвращает количество заявок.

        Аргументы:
            is_filtered_by_date (bool): Если True, учитываются только заявки после filter_date.

        Возвращает:
            int: Количество заявок.
        """
        if is_filtered_by_date:
            filtered_df = self.data_frame[self.data_frame[Columns.DATE_OF_CREATION.value] > self.filter_date]
            return filtered_df.shape[0]
        return self.data_frame.shape[0]

    def get_definite_columns_count(self, column: str, value: str, is_filtered_by_date: bool = False):
        """
        Возвращает количество записей, содержащих определенное значение в указанном столбце.

        Аргументы:
            column (str): Название столбца для поиска значений.
            value (str): Значение для поиска в столбце.
            is_filtered_by_date (bool): Если True, учитываются только записи после filter_date.

        Возвращает:
            int: Количество записей, содержащих указанное значение.
        """
        contains_filter = self.data_frame[column].str.contains(value,
                                                               na=False)
        if is_filtered_by_date:
            date_filter = self.data_frame[Columns.DATE_OF_CREATION.value] > self.filter_date
            combined_filter = contains_filter & date_filter
            return combined_filter.sum()
        return contains_filter.sum()

    def get_unique_columns_count(self, value: str, is_filtered_by_date: bool = False):
        """
        Возвращает количество уникальных значений в указанном столбце.

        Аргументы:
            value (str): Название столбца для поиска уникальных значений.
            is_filtered_by_date (bool): Если True, учитываются только записи после filter_date.

        Возвращает:
            int: Количество уникальных значений в столбце.
        """
        unique_filter = self.data_frame[value].nunique()

        if is_filtered_by_date:
            date_filter = self.data_frame[self.data_frame[Columns.DATE_OF_CREATION.value] > self.filter_date]
            number = date_filter[value].nunique()
            return number

        return unique_filter
