import sys

sys.path.append("/Users/ivanmolochkov/Documents/python_labs/src/lib")

from text import normalize, tokenize, count_freq, top_n


def table(arr: list[tuple[str, int]], isTable: bool = True):
    s = str()
    if isTable:
        ot = (
            8
            if max(map(len, [e[0] for e in arr])) < 5
            else max(map(len, [e[0] for e in arr])) + 3
        )
        s += "слово" + (" " * (ot - len("слово")) + "| частота")
        s += "\n" + "-" * ot + "-" * len("| частота")
        for e in arr:
            s += "\n" + e[0] + (" " * (ot - len(e[0]))) + "| " + f"{e[1]}"
        return s
    else:
        for e in arr:
            s += "\n" + f"{e[0]}: {e[1]}" if s != "" else f"{e[0]}: {e[1]}"
        return s


def main():
    a = tokenize(normalize(sys.stdin.read()))
    print(f"Всего слов: {len(a)}")
    print(f"Уникальных слов: {len(set(a))}")
    print("Топ-5:")
    print(table(top_n(count_freq(a), 5), True))


if __name__ == "__main__":
    main()

# echo 'Привет, мир! Привет!!!' | python3 src/lab3/text_stats.py
