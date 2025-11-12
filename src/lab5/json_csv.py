import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    p = Path(json_path)
    if not p.exists(): raise FileNotFoundError("файл не найден")
    if p.stat().st_size == 0: raise ValueError("пустой JSON или неподдерживаемая структура")
    if p.suffix.lower() != '.json': raise ValueError("файл не является JSON-файлом")
    if Path(csv_path).suffix.lower() != '.csv': raise ValueError("файл не является csv-файлом")
    with p.open('r', encoding='utf-8') as f:
        data = json.load(f)
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data): raise ValueError("JSON должен содержать список словарей")
    h = set()
    for item in data:
        h.update(item.keys())
    h = sorted(h)
    with Path(csv_path).open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=h)
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    p = Path(csv_path)
    if not p.exists(): raise FileNotFoundError(f"ошибка при открытии")
    if p.stat().st_size == 0: raise ValueError(f"файл пустой")
    if p.suffix.lower() != '.csv': raise ValueError("файл не является csv-файлом")
    if Path(json_path).suffix.lower() != '.json': raise ValueError("файл не является JSON-файлом")
    with p.open('r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    with Path(json_path).open('w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    json_to_csv("data/lab5/samples/people.json", "data/lab5/out/people_from_json.csv")
    csv_to_json("data/lab5/samples/people.csv", "data/lab5/out/people_from_csv.json")