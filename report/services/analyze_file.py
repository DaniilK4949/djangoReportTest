import pandas as pd
from dateutil import tz

from common.enums import Columns


class ExcelDataProcessor:
    MOSCOW = tz.gettz('Europe / Moscow')

    def __init__(self, data_frame: pd.DataFrame, filter_date: str):
        self.data_frame = data_frame
        self.filter_date = pd.Timestamp(filter_date, tzinfo=self.MOSCOW)
        self.data_frame[Columns.DATE_OF_CREATION.value] = pd.to_datetime(
            self.data_frame[Columns.DATE_OF_CREATION.value], dayfirst=True)

    def get_applications_count(self, is_filtered_by_date: bool = False):
        if is_filtered_by_date:
            filtered_df = self.data_frame[self.data_frame[Columns.DATE_OF_CREATION.value] > self.filter_date]
            return filtered_df.shape[0]
        return self.data_frame.shape[0]

    def get_definite_columns_count(self, column: str, value: str, is_filtered_by_date: bool = False):
        contains_filter = self.data_frame[column].str.contains(value,
                                                               na=False)
        if is_filtered_by_date:
            date_filter = self.data_frame[Columns.DATE_OF_CREATION.value] > self.filter_date
            combined_filter = contains_filter & date_filter
            return combined_filter.sum()
        return contains_filter.sum()

    def get_unique_columns_count(self, value: str, is_filtered_by_date: bool = False):
        unique_filter = self.data_frame[value].nunique()

        if is_filtered_by_date:
            date_filter = self.data_frame[self.data_frame[Columns.DATE_OF_CREATION.value] > self.filter_date]
            number = date_filter[value].nunique()
            return number

        return unique_filter
