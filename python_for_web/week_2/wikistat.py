from bs4 import BeautifulSoup
import networkx as nx
import re
import os


# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_tree(start, end, path):
    link_re = re.compile(r"(?<=/wiki/)[\w()]+")  # Искать ссылки можно как угодно, не обязательно через re
    files = dict.fromkeys(os.listdir(path))  # Словарь вида {"filename1": None, "filename2": None, ...}
    # TODO Проставить всем ключам в files правильного родителя в значение, начиная от start
    for file in files:
        files[file] = set()
        with open("{}{}".format(path, file)) as data:
            for i in re.findall(link_re, data.read()):
                if i in files and i != file:
                    files[file].add(i)
    return files


# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_bridge(start, end, path):
    files = build_tree(start, end, path)
    # bridge = []
    # TODO Добавить нужные страницы в bridge
    DG = nx.DiGraph()
    for start_point, end_points in files.items():
        weight = 1
        for end_point in end_points:
            DG.add_edge(start_point, end_point, weight=weight)
            weight += 1
    bridge = nx.shortest_path(DG, start, end)
    bridge = ['Stone_Age']
    return bridge


def parse(start, end, path):
    """
    Если не получается найти список страниц bridge, через ссылки на которых можно добраться от start до end, то,
    по крайней мере, известны сами start и end, и можно распарсить хотя бы их: bridge = [end, start]. Оценка за тест,
    в этом случае, будет сильно снижена, но на минимальный проходной балл наберется, и тест будет пройден.
    Чтобы получить максимальный балл, придется искать все страницы. Удачи!
    """

    bridge = build_bridge(start, end, path)  # Искать список страниц можно как угодно, даже так: bridge = [end, start]

    # Когда есть список страниц, из них нужно вытащить данные и вернуть их
    out = {}
    for file in bridge:
        print("{}{}".format(path, file))
        with open("{}{}".format(path, file)) as data:
            soup = BeautifulSoup(data, "lxml")

        body = soup.find(id="bodyContent")

        # print(body)
        imgs = sum(1 for img in body('img') if int(img.get('width')) >= 200)
        print(imgs)
        # headers = body
        # for i in body:
        #     print(i.string)
        # print(soup.h1)
        # print(soup.h1.renderContents())

        # for item in soup.contents:
        #     print(type(item), item)

        # print(body.h2)
        # print(soup.h2.contents[0])
        # print(soup.h3)
        # print(soup.h4)
        # print(soup.h5)
        # print(soup.h6)
        # for i in soup.li.find_next_siblings():
        #     print(type(i))
        n = 0
        for i in soup.find_all('li'):
            print()
            print(i)
            print(i.parent())


        print(n)

        # for img in imgs:
        #     print(img.get('width'))



        # TODO посчитать реальные значения
        imgs = 5  # Количество картинок (img) с шириной (width) не меньше 200
        headers = 10  # Количество заголовков, первая буква текста внутри которого: E, T или C
        linkslen = 15  # Длина максимальной последовательности ссылок, между которыми нет других тегов
        lists = 20  # Количество списков, не вложенных в другие списки

        out[file] = [imgs, headers, linkslen, lists]

    return out
