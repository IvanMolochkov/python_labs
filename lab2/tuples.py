def format_record(kor):
    if len(kor[0]) == 0: return "ValueError"
    if len(kor[1]) == 0: return "ValueError"
    if type(kor[2]) != float: return "TypeError"
    res = f", гр. {kor[1]}, GPA {kor[2]:.2f}"
    a = kor[0].split()
    if len(a) == 3: res = f"{a[0][0].upper()}{a[0][1:]} {a[1][0].upper()}. {a[2][0].upper()}.".strip() + res
    elif len(a) == 2: res = f"{a[0][0].upper()}{a[0][1:]}. {a[1][0].upper()}." + res
    else: return "ValueError"
    return res

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
# print(format_record(("", "ABB-01", 3.999)))
# print(format_record(("Иванов Иван Иванович", "", 3.999)))
# print(format_record(("Иванов Иван Иванович", "123", "ab")))