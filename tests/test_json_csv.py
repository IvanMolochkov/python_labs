import json
import csv
from pathlib import Path
from src.lab5.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    len_data = len(data)
    h = set()
    for item in data:
        h.update(item.keys())
    h = sorted(h)
    with src.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=h)
        writer.writeheader()
        writer.writerows(data)
    csv_to_json(str(src), str(dst))

    with dst.open("r", encoding="utf-8") as f:
        json_data = json.load(f)

    assert isinstance(json_data, list) or all(
        isinstance(item, dict) for item in json_data
    )
    for obj_json_data in json_data:
        assert len_data == len(obj_json_data)

        arr = list(e for e in obj_json_data)
        age, name = arr
        assert age == "age"
        assert name == "name"


" pytest "
" pytest tests/test_json_csv.py "
" pytest tests/test_json_csv.py::test_csv_to_json_roundtrip "
" pytest --cov=src --cov-report=term-missing "
" black --check . "
