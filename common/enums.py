from enum import Enum


class Columns(Enum):
    PACKAGE_ID = 'ID пакета'
    APPLICATION_STATE = 'Состояние заявки'
    APPLICATION_STATUS = 'Статус заявки'
    APPLICATION_AUTHOR = 'Автор заявки'
    DATE_OF_CREATION = 'Дата создания заявки'


class CalculatingValues(Enum):
    DUPLICATE = 'Дубликат'
    ADDITION = 'ДОБАВЛЕНИЕ'
    EXTENSION = 'РАСШИРЕНИЕ'
    PROCESSING = 'Отправлена в обработку'
    PENDING = 'Возвращена на уточнение'
    SUCCESS_PROCESSING = 'Обработка завершена'
