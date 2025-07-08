# Модуль для чтения CSV-файлов
import csv

def read_csv(file_path: str) -> list[dict]:
    # Открываем файл c автозакрытием после
    with open(file_path, newline='', encoding='utf-8') as f:
        # Используем DictReader — строки будут словарями: {"name": "iPhone", "price": "999"}
        reader = csv.DictReader(f)
        return list(reader)