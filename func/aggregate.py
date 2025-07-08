# Модуль для агрегации avg (среднее), min, max

def aggregate(rows: list[dict], column: str, func: str) -> float:
    # Проверяем, существует ли колонка
    if column not in rows[0]:
        raise ValueError("Колонка не найдена")

    # Извлекаем все значения и превращаем в числа
    values = [float(row[column]) for row in rows]

    if func == "avg":
        return sum(values) / len(values)
    elif func == "min":
        return min(values)
    elif func == "max":
        return max(values)
    else:
        raise ValueError("Функция агрегации не поддерживается")