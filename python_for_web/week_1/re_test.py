import re

def find_all_digits(text):
    exp = r'(\d+)'  #Тут напишите своё регулярное выражение
    return re.findall(exp, text)


def find_no_null(text):
    exp = "[a-z]\d[a-z][\da-z]"
    return re.search(exp, text)

def find_exp(exp):
    text = "мама вымыла 2 рамы"
    return exp if len(re.findall(exp, text)) == 2 else None


if __name__ == "__main__":
    test = 'a123b45с6d'
    print(find_all_digits(test))
    print()

    exp = "м.*ы"
    print(find_exp(exp))

    exp = r"\d+"
    print(find_exp(exp))

    exp = r"а.\D"
    print(find_exp(exp))

    exp = "мы"
    print(find_exp(exp))

    exp = "....мы"
    print(find_exp(exp))

    exp = "м.*?ы"
    print(find_exp(exp))

    exp = "м.+?ы"
    print(find_exp(exp))


    sw = "r2d2"
    print(find_no_null(sw))

    sw = "c3po"
    print(find_no_null(sw))


    sw = "luke"
    print(find_no_null(sw))


    sw = "f0rce"
    print(find_no_null(sw))


    sw = "ev9d9"
    print(find_no_null(sw))


    sw = "bb8"
    print(find_no_null(sw))
