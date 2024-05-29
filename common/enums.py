from enum import Enum


class Columns(Enum):
    """
    Перечисление, представляющее различные столбцы в наборе данных.

    Атрибуты:
        PACKAGE_ID (str): Идентификатор пакета.
        APPLICATION_STATE (str): Состояние заявки.
        APPLICATION_STATUS (str): Статус заявки.
        APPLICATION_AUTHOR (str): Автор заявки.
        DATE_OF_CREATION (str): Дата создания заявки.
    """
    PACKAGE_ID = 'ID пакета'
    APPLICATION_STATE = 'Состояние заявки'
    APPLICATION_STATUS = 'Статус заявки'
    APPLICATION_AUTHOR = 'Автор заявки'
    DATE_OF_CREATION = 'Дата создания заявки'


class CalculatingValues(Enum):
    """
    Перечисление, представляющее различные возможные значения для состояния и статуса заявок.

    Атрибуты:
        DUPLICATE (str): Заявка является дубликатом.
        ADDITION (str): Заявка на добавление.
        EXTENSION (str): Заявка на расширение.
        PROCESSING (str): Заявка отправлена в обработку.
        PENDING (str): Заявка возвращена на уточнение.
        SUCCESS_PROCESSING (str): Обработка заявки завершена.
    """
    DUPLICATE = 'Дубликат'
    ADDITION = 'ДОБАВЛЕНИЕ'
    EXTENSION = 'РАСШИРЕНИЕ'
    PROCESSING = 'Отправлена в обработку'
    PENDING = 'Возвращена на уточнение'
    SUCCESS_PROCESSING = 'Обработка завершена'
