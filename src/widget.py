from datetime import datetime
from masks import get_mask_card_number, get_mask_account


def mask_account_card(info: str) -> str:
    """Разделяем строку на тип и номер по последнему пробелу"""
    type_and_number = info.rsplit(" ", 1)
    type_ = type_and_number[0]
    number = type_and_number[1]

    """ Проверяем, относится ли это к карте или счету """
    if type_.lower().startswith("счет"):
        """Маскировка для счета"""
        masked_number = get_mask_account(number)
    else:
        """Маскировка для карты"""
        masked_number = get_mask_card_number(number)

    """ Возврат замаскированной строки """
    return f"{type_} {masked_number}"


def get_date(date_string: str) -> str:
    """Преобразуем строку в объект datetime"""
    date_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")
    """ Форматируем объект datetime в строку нужного формата """
    return date_object.strftime("%d.%m.%Y")
