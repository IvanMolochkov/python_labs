def min_max(arr): return [min(arr), max(arr)] if len(arr) > 0 else "ValueError"
def unique_sorted(arr): 
    a = []
    for e in set(arr):
        a.append(e)
    return sorted(a)
def flatten(arr):
    a = []
    for e in arr: 
        for el in e: 
            if type(el) != int: return "TypeError"
            a.append(el)
    return a


# функция min_max
print("функция min_max")

print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))

print("----------------------")

# функция unique_sorted
print("unique_sorted")

print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

print("----------------------")

# функция flatten
print("flatten")

print(flatten([[1, 2], [3, 4]]))
print(flatten(([1, 2], (3, 4, 5))))
print(flatten([[1], [], [2, 3]]))

print(flatten([[1, 2], "ab"]))

print("----------------------")
