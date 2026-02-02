from datetime import datetime


def filter_by_state(operations, state='EXECUTED'):
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param operations: список словарей с данными о операциях
    :param state: значение ключа 'state' для фильтрации (по умолчанию 'EXECUTED')
    :return: новый список словарей, где 'state' == state
    """
    return [op for op in operations if op.get('state') == state]


def sort_by_date(operations, reverse=True):
    """
    Сортирует список словарей по дате (ключу 'date').

    :param operations: список словарей с данными о операциях
    :param reverse: порядок сортировки (True — убывание, False — возрастание; по умолчанию True)
    :return: новый отсортированный список словарей
    """
    def parse_date(date_str):
        # Преобразуем строку даты в объект datetime для корректной сортировки
        return datetime.fromisoformat(date_str.replace('Z', '+00:00'))

    return sorted(
        operations,
        key=lambda op: parse_date(op['date']),
        reverse=reverse
    )
