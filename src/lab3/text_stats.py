import sys

sys.path.append('/Users/ivanmolochkov/Documents/python_labs/src/lib')

from text import normalize, tokenize, count_freq, top_n

def main():
    a = sys.stdin.read()
    print(f"Всего слов: {len(tokenize(a))}")
    print(f"Уникальный слов: {len(set(tokenize(a)))}")
    print("Топ-5:")
    for e in top_n(count_freq(tokenize(normalize(a))), 5):
        print(f"{e[0]}: {e[1]}")

if __name__ == "__main__":
    main()
    
# $ echo 'Привет, мир! Привет!!!' | python3 src/lab3/text_stats.py
