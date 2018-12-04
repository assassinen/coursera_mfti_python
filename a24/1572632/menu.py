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

def create_rect():
    args = input('Введите координаты левой точки, ширину и высотв прямоугольника '
                 '(пример: 1, 2, 5, 3)\n').split(',')
    return Rectangle(*args)



def main():
    ans = True
    while ans:
        print("""
        1. Создать прямоугольник
        2. Посмотреть сущетсвующий прямоугольник
        3. Изменить высоты прямоугольника
        4. 
        4. Exit/Quit
        """)
        ans = input("What would you like to do? ")
        if ans == "1":
            rect = create_rect()
            print(f'Создан прямоугольник: \n{rect}')
        elif ans == "2":
            print("\n Student Deleted")
        elif ans == "3":
            print("\n Student Record Found")
        elif ans == "4":
            print("\n Goodbye")
        elif ans != "":
            print("\n Not Valid Choice Try again")

if __name__ == '__main__':
    main()