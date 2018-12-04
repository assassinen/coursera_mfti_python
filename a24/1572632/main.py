'''
Составить описание класса прямоугольников со сторонами, параллельными осям координат.
Предусмотреть возможность перемещения прямоугольников на плоскости,
изменения размеров,
построения наименьшего прямоугольника, содержащего два заданных прямоугольника,
и прямоугольника, являющегося общей частью (пересечением) двух прямоугольников.
Написать программу, демонстрирующую работу с этим классом.
Программа должна содержать меню, позволяющее осуществить проверку всех методов класса.
(Программа должна быть реализована на языке Python, вывод в консоль)
'''

class Rectangle:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.diagonal_x = x + width
        self.diagonal_y = y + height

    def __repr__(self):
        return f'Координаты левой нижней точки {self.x}:{self.y}. Ширина: {self.width}. Высота: {self.height}.'

    def move(self, x, y):
        self.x += x
        self.y += y

    def resize(self, action, x):
        if action == 'more':
            self.width *= x
            self.height *= x
        elif action == 'less':
            self.width //= x
            self.height //= x

    def set_diagonal_point(self):
        self.diagonal_x = self.x + self.width
        self.diagonal_y = self.y + self.height

    def set_width(self, width):
        self.width = width
        self.set_diagonal_point()

    def set_height(self, height):
        self.height = height
        self.set_diagonal_point()

    def union(self, rect):
        x = self.x if self.x < rect.x else rect.x
        y = self.y if self.y < rect.y else rect.y
        diagonal_x = self.diagonal_x if self.diagonal_x > rect.diagonal_x else rect.diagonal_x
        diagonal_y = self.diagonal_y if self.diagonal_y > rect.diagonal_y else rect.diagonal_y
        width = diagonal_x - x
        height = diagonal_y - y
        return Rectangle(x, y, width, height)

    def intersection(self, rect):
        x = self.x if self.x > rect.x else rect.x
        y = self.y if self.y > rect.y else rect.y
        diagonal_x = self.diagonal_x if self.diagonal_x < rect.diagonal_x else rect.diagonal_x
        diagonal_y = self.diagonal_y if self.diagonal_y < rect.diagonal_y else rect.diagonal_y
        width = diagonal_x - x
        height = diagonal_y - y
        return Rectangle(x, y, width, height)





def main():
    rect = Rectangle(1, 1, 2, 3)
    print(rect)
    print('Переместим прямоугольник на 2 по x и 3 по y')
    rect.move(2, 3)
    print(rect)
    print('Зададим новую высоту прямоугольника. Высота = 5')
    rect.set_height(5)
    print(rect)
    print('Зададим новую штрину прямоугольника. Ширина = 8')
    rect.set_width(8)
    print(rect)
    rect_1 = Rectangle(4, 3, 10, 3)
    print('Имеем два прямоугольника:')
    print(f'Первый прямоугольник: {rect}')
    print(f'Второй прямоугольник: {rect_1}')
    rect_3 = rect.union(rect_1)
    print(f'Hаименьший прямоугольника, содержащего два заданных прямоугольника: {rect_3}')
    rect_4 = rect.intersection(rect_1)
    print(f'Прямоугольника, являющийся общей частью (пересечением) двух прямоугольников: {rect_4}')






if __name__ == '__main__':
    main()
