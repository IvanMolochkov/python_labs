import datetime
from datetime import date
from dataclasses import dataclass

@dataclass
class Student:
    fio: str
    birthdate: str 
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.datetime.strptime(self.birthdate, "%Y/%m/%d")
        except ValueError:
            raise ValueError("warning: birthdate format might be invalid")
        
        if not (0 <= self.gpa <= 10):
            raise ValueError("gpa must be between 0 and 10")

    def age(self) -> int:
        birth = datetime.datetime.strptime(self.birthdate, "%Y/%m/%d").date()
        today = date.today()
        
        age = today.year - birth.year
        if (today.month, today.day) < (birth.month, birth.day):
            age -= 1
        return age

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=d["gpa"]
        )

    def __str__(self):
        return f"{self.fio}, {self.group}, {self.gpa}"