import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from func.filter import filter_rows
import pytest

def test_filter_rows_greater_than():
    rows = [
        {"name": "A", "price": "100"},
        {"name": "B", "price": "300"},
        {"name": "C", "price": "500"}
    ]
    filtered = list(filter_rows(rows, "price", ">", "200"))
    assert len(filtered) == 2
    assert filtered[0]["name"] == "B"
    assert filtered[1]["name"] == "C"

def test_filter_rows_equal_string():
    rows = [
        {"name": "A", "brand": "apple"},
        {"name": "B", "brand": "samsung"}
    ]
    filtered = list(filter_rows(rows, "brand", "=", "apple"))
    assert len(filtered) == 1
    assert filtered[0]["name"] == "A"

def test_filter_invalid_column():
    rows = [{"name": "test", "price": "100"}]
    with pytest.raises(ValueError, match="Колонка 'nonexistent' не найдена"):
        list(filter_rows(rows, "nonexistent", "=", "value"))
