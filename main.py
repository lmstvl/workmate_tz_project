# Это главная точка входа — файл, который мы запускаем через терминал
# Здесь мы принимаем аргументы --file, --where и --aggregate

import argparse  # библиотека для чтения аргументов командной строки
from func.reader import read_csv  # импорт функции чтения CSV
from func.filter import filter_rows  # импорт функции фильтрации
from func.aggregate import aggregate  # импорт функции агрегации
from tabulate import tabulate  # библиотека для красивого вывода таблицы в терминал

# Вспомогательная функция для разбора выражения фильтрации: например "price>500"
def parse_where(expr: str):
    for op in [">=", "<=", ">", "<", "="]:  # поддерживаемые операторы
        if op in expr:
            parts = expr.split(op)
            return parts[0], op, parts[1]  # возвращаем колонку, оператор и значение
    raise ValueError("Неверный формат фильтра")

def main():
    parser = argparse.ArgumentParser() # создаем объект парсера
    parser.add_argument("--file", required=True, help="Путь до CSV-файла") # добавляем аргументы
    parser.add_argument("--where", help="Фильтрация, например rating>4.5")
    parser.add_argument("--aggregate", help="Агрегация, например price=avg")

    args = parser.parse_args() # сохраняем их в переменной

    # Читаем CSV-файл
    rows = read_csv(args.file)

    # Если указан аргумент фильтрации
    if args.where:
        col, op, val = parse_where(args.where)
        filtered = list(filter_rows(rows, col, op, val))
        print(tabulate(filtered, headers="keys"))  # печатаем таблицу

    # Если указана агрегация
    elif args.aggregate:
        col, func = args.aggregate.split("=")
        result = aggregate(rows, col, func)
        print(f"{func} of {col}: {result:.2f}")  # выводим результат

    else:
        print("Что-то пошло не так")

if __name__ == "__main__":
    main()
