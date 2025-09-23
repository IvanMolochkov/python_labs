fio = input()
arr = []
new_fio = ""
for e in fio.split():
    arr.append(e[0])
    new_fio += f"{e} "
ini = "".join(arr)
new_fio = new_fio.strip()
print(f"ФИО: {new_fio}")
print(f"Инициалы: {ini}")
print(f"Длина (символов): {len(new_fio)}")

