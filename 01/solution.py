# Usando dictionary comprehension
def count_vowels1(text: str) -> dict:
    return dict(sorted({el: text.count(el) for el in text.lower() if el in "aeiou"}.items()))

# Uma solução prática e simples
def count_vowels2(text: str) -> str:
    vowels = "aeiou"
    result = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

    for el in text.lower():
        if el in vowels:
            result[el] = result[el] + 1

    return result

if __name__ == "__main__":
    print(count_vowels1("Programação é Divertida"))
    print(count_vowels2("Programação é Divertida"))
