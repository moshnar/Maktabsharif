from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def add(self, p):
        return Point(p.x + self.x, p.y + self.y)

    def __calc_norm(self):
        self.__norm = sqrt(self.x ** 2 + self.y ** 2)

    def get_norm(self):
        return self.__norm

    def display(self):
        print((self.x, self.y))


p1 = Point(2, 3)
p2 = Point(1, 4)
#print(p1)
#print(p1.add(p2))
#p1.add(p2).display()
#print(p1.__norm)
#print(p1.__calc_norm())
#print(p1.get_norm())