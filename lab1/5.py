fio = input().strip()
arr = []
for e in fio.split():
    arr.append(e[0])
ini = "".join(arr)
print(f"ФИО: {fio}")
print(f"Инициалы: {ini}")
print(f"Длина (символов): {len(fio)}")

