import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def sketch(self):
        pass

    @staticmethod
    def concat_area(l: list):
        area = 0
        for i in l:
            if type(i) == Rectangle:
                area += i.area
            else:
                print('invalid parameter')
        return area


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

    def sketch(self):
        for _ in range(self.height):
            print('*' * self.width)


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

    @staticmethod
    def draw_concat(l):# will draw squares next to eachother
        for i in range(max(l)):
            for j in l:
                if type(j) == int:
                    if j - i > 0:
                        print('*' * j, end='')
                    else:
                        print(' ' * j, end='')
                else:
                    raise TypeError
            print()


class Parallelogram(Shape):
    def __init__(self, a, b, height): # both are equal
        self.height = height
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.h * self.a

    @property
    def perimeter(self):
        return 2 * (self.b + self.a)

    def sketch(self):
        for i in range(self.h - 1, -1, -1):
            print(i * (int(math.sqrt(self.b ** 2 - self.h ** 2)) // self.h) * ' ' + self.a * '*')


class Rhombus(Parallelogram):
    def __init__(self, a: int, h: int):
        super().__init__(a, a, h)


class Diamond(Square, Rhombus):
    def __init__(self, a):
        Square.__init__(self, a)

    def sketch(self):
        n = self.w * 1.7
        n = math.ceil(n) if math.ceil(n) % 2 == 1 else math.floor(n)

        for i in range(1, n + 1):
            i = i - (n // 2 + 1)
            if i < 0:
                i = -i
            print(' ' * i + '*' * (n - i * 2))


Square.concat_area([3, 5, 10, 9, 10])
