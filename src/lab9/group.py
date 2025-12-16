import csv
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.lab8.models import Student


class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)

    def _read_all(self):
        rows = []
        with open(self.path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
        return rows

    def list(self):
        rows = self._read_all()
        students = []
        for row in rows:
            student = Student(
                fio=row["fio"],
                birthdate=row["birthdate"],
                group=row["group"],
                gpa=float(row["gpa"]),
            )
            students.append(student)
        return students

    def add(self, student: Student):
        with open(self.path, "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(
                [student.fio, student.birthdate, student.group, student.gpa]
            )

    def find(self, substr: str):
        rows = self._read_all()
        found = [r for r in rows if substr.lower() in r.get("fio", "").lower()]
        students = []
        for row in found:
            s = Student(
                fio=row["fio"],
                birthdate=row["birthdate"],
                group=row["group"],
                gpa=float(row["gpa"]),
            )
            students.append(s)
        return students

    def remove(self, fio: str):
        rows = self._read_all()
        for i, r in enumerate(rows):
            if r["fio"] == fio:
                rows.pop(i)
                break
        with open(self.path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
            writer.writeheader()
            writer.writerows(rows)

    def update(self, fio: str, **fields):
        rows = self._read_all()
        for row in rows:
            if row["fio"] == fio:
                for key, value in fields.items():
                    if key in row:
                        row[key] = str(value)
                break
        with open(self.path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
            writer.writeheader()
            writer.writerows(rows)
    def stats(self) -> dict:
        students = self.list()
        
        if not students:
            return {
                "count": 0,
                "min_gpa": None,
                "max_gpa": None,
                "avg_gpa": None,
                "groups": {},
                "top_5_students": []
            }
        
        gpas = [s.gpa for s in students]
        
        min_gpa = min(gpas)
        max_gpa = max(gpas)
        avg_gpa = sum(gpas) / len(gpas)
        
        groups_count = {}
        for student in students:
            groups_count[student.group] = groups_count.get(student.group, 0) + 1
        
        sorted_students = sorted(students, key=lambda s: s.gpa, reverse=True)
        top_5 = [
            {"fio": s.fio, "gpa": s.gpa}
            for s in sorted_students[:5]
        ]
        
        return {
            "count": len(students),
            "min_gpa": round(min_gpa, 2),
            "max_gpa": round(max_gpa, 2),
            "avg_gpa": round(avg_gpa, 2),
            "groups": groups_count,
            "top_5": top_5
        }


if __name__ == "__main__":
    group = Group("data/lab9/students.csv")

    group.add(Student("Иванов Иван", "2003/10/10", "БИВТ-21-1", 4.3))
    group.add(Student("Петров Пётр", "2003/05/15", "БИВТ-21-1", 4.8))
    group.add(Student("Сидорова Анна", "2002/12/20", "БИВТ-21-2", 4.5))

    print("Все студенты:")
    for student in group.list():
        print(f"{student.fio} | {student.group} | GPA: {student.gpa}")

    print("\n")
    print("Поиск Иван:")
    for student in group.find("Иван"):
        print(f"{student.fio}")

    print("\n")
    print("Обновление GPA для Петрова:")
    group.update("Петров Пётр", gpa=5.0)
    found = group.find("Петров")
    if found:
        print(f"  Новый GPA: {found[0].gpa}")

    print("\n")
    print("Удаление 'Иванов Иван':")
    group.remove("Иванов Иван")
    print(f"Осталось студентов: {len(group.list())}")
    
    print("\n")
    print("Статистика по gpa:")
    for gpa, e in group.stats().items():
        print(f"{gpa}: {e}")
