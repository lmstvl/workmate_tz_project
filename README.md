# CSV Processor (Тестовое задание)

Скрипт обрабатывает CSV-файлы:
- агрегация: `--aggregate column=avg|min|max`
- фильтрация: `--where column>value`


## Примеры запуска:

```
python main.py --file tests/sample.csv --where price>500
python main.py --file tests/sample.csv --aggregate rating=max
```

## Установка зависимостей

```
pip install -r requirements.txt
```
