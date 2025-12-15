def get_mask_card_number(card_number: str) -> str:
    """Проверяем, что длина номера карты равна 16"""
    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать ровно 16 цифр.")

    """ Разбиваем номер карты на части """
    part1 = card_number[:4]
    part2 = card_number[4:6]
    part3 = "**"
    part4 = "****"
    part5 = card_number[-4:]

    """ Собираем в нужном формате """
    mask_card_number = f"{part1} {part2}{part3} {part4} {part5}"

    """ Возвращам маскированный номер """
    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """Проверяем, что длина номера счета равна 20"""
    if len(account_number) != 20:
        raise ValueError("Номер счета должен содержать ровно 20 цифр.")

    """ Получаем последние 4 цифры номера счета"""
    mask_account = account_number[-4:]

    """ Возвращам маскированный номер """
    return f"**{mask_account}"
