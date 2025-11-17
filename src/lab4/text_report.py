from ..lib.text import normalize, tokenize, count_freq, top_n
from ..lab4.io_txt_csv import read_text, write_csv


def main():
    text = tokenize(normalize(read_text("data/input")))
    arr = [("Всего слов", len(text)), ("Уникальных слов", len(set(text)))]
    for e in top_n(count_freq(text), 5):
        arr.append((e[0], e[1]))
    write_csv(arr, "data/lab4/f/report.json")


if __name__ == "__main__":
    main()


# python3 -m src.lab4.text_report
