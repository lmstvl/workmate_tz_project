# Модуль для фильтрации строк по заданному условию

#результат у нас массив из словарей-строк
def filter_rows(rows: list[dict], column: str, operator: str, value: str) -> list[dict]:
    # Проверяем, существует ли колонка
    if column not in rows[0]:
        raise ValueError(f"Колонка '{column}' не найдена в файле")

    # анонимные функции для операторов сравнения
    ops = {
        '>': lambda x, y: x > y,
        '<': lambda x, y: x < y,
        '=': lambda x, y: x == y,
        '>=': lambda x, y: x >= y,
        '<=': lambda x, y: x <= y,
    }

    op_func = ops[operator]  # одно из условий пользования анонимной функции - быть в переменной

    for row in rows:
        val = row[column]
        try:
            # Пробуем сравнить как числа
            val = float(val)
            value_cmp = float(value)
        except ValueError:
            # Иначе сравниваем как строки
            value_cmp = value

        if op_func(val, value_cmp):
            yield row  # если условие выполняется, то возвращаем строку