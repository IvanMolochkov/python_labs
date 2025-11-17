is_rectangle = lambda arr: len(set(list(map(len, arr)))) == 1


def transpose(arr):
    new_arr = []
    try:
        len_arr = list(map(len, arr))
    except:
        return "ValueError"
    if len(set(len_arr)) == 0:
        return []
    if not is_rectangle(arr):
        return "ValueError"
    max_x = len_arr[0]
    max_y = len(len_arr)
    for x in range(max_x):
        o = []
        for y in range(max_y):
            o.append(arr[y][x])
        new_arr.append(o)
    return new_arr


def row_sums(arr):
    sum_arr = []
    if not is_rectangle(arr):
        return "ValueError"
    len_arr = list(map(len, arr))
    max_x = len_arr[0]
    max_y = len(len_arr)
    for y in range(max_y):
        o = []
        for x in range(max_x):
            o.append(arr[y][x])
        sum_arr.append(sum(o))
    return sum_arr


def col_sums(arr):
    sum_arr = []
    if not is_rectangle(arr):
        return "ValueError"
    len_arr = list(map(len, arr))
    max_x = len_arr[0]
    max_y = len(len_arr)
    for x in range(max_x):
        o = []
        for y in range(max_y):
            o.append(arr[y][x])
        sum_arr.append(sum(o))
    return sum_arr


# функция transpose
print("функция transpose")

print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], 3]))

print("----------------------")

# функция row_sums
print("функция row_sums")

print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))

print("----------------------")

# функция col_sums
print("функция col_sums")

print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
