from string import ascii_letters

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
    if casefold: text = text.casefold()
    if yo2e: text = text.replace("ё", "е").replace("Ë", "Е")
    new_text = []
    for e in text.split():
        new_text.append(e + " ")
    new_text = "".join(new_text)
    return new_text.strip()


def tokenize(text: str):
    text += " "
    new_text = []
    o = []
    for e in text:
        if e in ascii_letters or (e == "-" and o[-1] != " ") or e in "АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя" or e in "0123456789":
            o.append(e)
        else:
            if len(o) != 0: 
                o = "".join(o)
                new_text.append(o)
                o = []
            else: continue
    return new_text


def count_freq(tokens: list[str]): 
    tokens = sorted(tokens)
    k = 0
    slovar = dict()
    for e in tokens:
        for el in tokens:
            if e == el: 
                k+=1
        if k != 0:
            slovar[e] = k
            k = 0
        else: continue
    return slovar


def top_n(freq: dict[str, int], n: int = 5):
    kor = []
    i = n
    for e in freq:
        if i == 0: break
        kor.append((e, freq[e]))
        i -= 1
    return kor


# print("---------------------------------")

# print(normalize("ПрИвЕт\nМИр\t"))
# print(normalize("ёжик, Ёлка"))
# print(normalize("Hello\r\nWorld"))
# print(normalize("  двойные   пробелы  "))

# print("---------------------------------")

# print(tokenize("привет мир"))
# print(tokenize("hello,world!!!"))
# print(tokenize("по-настоящему круто"))
# print(tokenize("2025 год"))
# print(tokenize("emoji 😀 не слово"))

# print("---------------------------------")

# print(count_freq(["a","b","a","c","b","a"]))
# print(count_freq(["bb","aa","bb","aa","cc"]))

# print("---------------------------------")

# print(top_n(count_freq(["a","b","a","c","b","a"]), 2))
# print(top_n(count_freq(["bb","aa","bb","aa","cc"]), 2))

# print("---------------------------------")