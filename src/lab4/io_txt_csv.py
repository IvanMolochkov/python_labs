import csv
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    unicode_decode_error = (
        "UnicodeDecodeError\nВыберите существующую кодировку\nНапример: utf-8"
    )
    try:
        return Path(path).read_text(encoding=encoding)
    except FileNotFoundError:
        return "FileNotFoundError"
    except LookupError:
        return unicode_decode_error
    except UnicodeDecodeError:
        return unicode_decode_error


def write_csv(
    rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    p = Path(path)
    rows = list(rows)

    # try: p.open("w", newline="", encoding="utf-8")
    # except FileNotFoundError: p = Path(ensure_parent_dir(path))

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)


# def ensure_parent_dir(path: str | Path) -> None:
#     path = str(path)
#     new_path = ""

#     for part in path.split("/"):
#         new_path = os.path.join(new_path, part) if new_path else part
#         if os.path.exists(new_path):
#             if os.path.isfile(new_path):
#                 raise ValueError(f"Путь '{new_path}' является файлом, нельзя создать директорию")
#             continue
#         else:
#             if new_path != path:
#                 os.mkdir(new_path)


# print(read_text("data/lab4/a"))
# print(write_csv([("cake", 10),("test",3)], "data/lab4/a.csv", ["hghyg"]))
