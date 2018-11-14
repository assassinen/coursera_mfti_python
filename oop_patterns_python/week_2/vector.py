import math

class Vec2d:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def __add__(self, v):
        return v.x + self.x, v.y + self.y

    def __sub__(self, v):
        return self.x - v.x, self.y - v.y

    def __mul__(self, k):
        return self.x * k, self.y * k

    def __len__(self):
        return int(math.sqrt(self.x * self.x + self.y * self.y))

    def __repr__(self):
        return f'x: {self.x}, y: {self.y}'

def main():
    v1 = Vec2d((1,1))
    v2 = Vec2d((1,2))
    print(v1 + v2)
    print(v1 - v2)
    print(v2 - v1)
    print(v2 * 5)
    print(len(v1))


if __name__ == "__main__":
    main()