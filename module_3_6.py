def calculate_structure_sum(*args):
    total_sum = 0  # Создаем переменную для хранения суммы

    # Проходим по каждому элементу в аргументах
    for item in args:
        if isinstance(item, (int, float)):  # Если элемент - число
            total_sum += item
        elif isinstance(item, str):  # Если элемент - строка
            total_sum += len(item)
        elif isinstance(item, (list, tuple, set)):  # Если элемент - коллекция
            total_sum += calculate_structure_sum(*item)  # Рекурсивный вызов
        elif isinstance(item, dict):  # Если элемент - словарь
            total_sum += calculate_structure_sum(*item.values())  # Суммируем значения
            total_sum += calculate_structure_sum(*item.keys())  # Суммируем ключи

    return total_sum  # Возвращаем общую сумму

# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(*data_structure)
print(result)  # Вывод: 99