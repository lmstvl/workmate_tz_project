import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from func.reader import read_csv

def test_read_csv():
    rows = read_csv("tests/sample.csv")
    assert isinstance(rows, list)
    assert isinstance(rows[0], dict)
    assert rows[0]["name"] == "iphone 15 pro"
