def mask_account_card(info: str) -> str:
    """Разделяем строку на тип и номер по последнему пробелу"""
    type_and_number = info.rsplit(" ", 1)
    type_ = type_and_number[0]
    number = type_and_number[1]

    """ Проверяем, относится ли это к карте или счету """
    if type_.lower().startswith("счет"):
        """Маскировка для счета"""
        masked_number = "**" + number[-4:]
    else:
        """Маскировка для карты"""
        masked_number = number[:4] + " " + number[4:6] + "** **** " + number[-4:]

    """ Возврат замаскированной строки """
    return f"{type_} {masked_number}"
