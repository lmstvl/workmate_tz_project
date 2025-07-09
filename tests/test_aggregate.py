from func.aggregate import aggregate
import pytest

def test_aggregate_avg():
    rows = [
        {"price": "100"},
        {"price": "200"},
        {"price": "300"}
    ]
    result = aggregate(rows, "price", "avg")
    assert result == 200.0

def test_aggregate_min():
    rows = [
        {"rating": "4.8"},
        {"rating": "4.2"},
        {"rating": "4.6"}
    ]
    result = aggregate(rows, "rating", "min")
    assert result == 4.2

def test_aggregate_max():
    rows = [
        {"rating": "4.8"},
        {"rating": "4.2"},
        {"rating": "4.6"}
    ]
    result = aggregate(rows, "rating", "max")
    assert result == 4.8

def test_aggregate_unknown_function():
    rows = [{"value": "10"}, {"value": "20"}]
    with pytest.raises(ValueError, match="Функция агрегации не поддерживается"):
        aggregate(rows, "value", "sum")

def test_aggregate_missing_column():
    rows = [{"value": "10"}]
    with pytest.raises(ValueError, match="Колонка не найдена"):
        aggregate(rows, "unknown", "avg")
