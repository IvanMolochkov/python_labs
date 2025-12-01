import json
from models import Student

def students_to_json(students, path):
    data = [s.to_dict() for s in students]
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [Student.from_dict(d) for d in data]


if __name__ == "__main__":
    students_to_json([
        Student("Иванов Иван Иванович", "2000/05/15", "ИУ5-41", 8.5),
        Student("Петрова Мария Сергеевна", "2001/03/20", "ИУ5-41", 9.2),
        Student("Сидоров Петр Александрович", "1999/12/10", "ИУ5-42", 7.8),
    ], "data/lab8/students_output.json")
    for student in students_from_json("data/lab8/students_input.json"):
        print(student)