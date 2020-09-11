import math
class Shape:

    def area(self):#Abstract method for calculating the area
        raise NotImplementedError()

    def perimeter (self):#Abstract method for calculating the perimeter
        raise NotImplementedError()

    def sketch(self):#Abstract method for sketching the shape in star pattern
        raise NotImplementedError()




class Rectangle(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def area (self):
        return self.x * self.y

    def perimeter (self):
        return (self.x * self.y) * 2

    def sketch(self):
        print('\n'.join(('*' * self.x) for _ in range(self.y)))



class Square(Rectangle):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area (self):
        return self.x ** 2

    def perimeter (self):
        return self.x * 4

    def sketch(self):
        print('\n'.join(('*' * self.x) for _ in range(self.y)))

class Parallelogram(Shape):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area (self):
        return self.x * self.y

    def perimeter (self):
        return (self.x * self.y) * 2

    def sketch(self):
        for i in range(0, self.x):
            for j in range(1, i + 1):
                print(" ", end="")
            for j in range(0, self.y):
                print("*", end="")
            print()

class Rhombus(Parallelogram):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area (self):
        return (self.x * self.y)//2

    def perimeter(self):
        return self.x * 4

    def sketch(self):
        for i in range(self.x):
            print(" " * (self.x - i), "*" * (i * 2 + 1))
        for i in range(self.x - 2, -1, -1):
            print(" " * (self.x - i), "*" * (i * 2 + 1))

class Diamond(Rhombus,Square):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return (self.x * self.y) // 2

    def perimeter(self):
        return self.x * 4

    def sketch(self):
        for i in range(self.x):
            print(" " * (self.x - i), "*" * (i * 2 + 1))
        for i in range(self.x - 2, -1, -1):
            print(" " * (self.x - i), "*" * (i * 2 + 1))


r = Rectangle(20,10)
s = Square(4,4)
print(r.area(),r.perimeter())
d = Diamond(4,4)
d.sketch()
#r.sketch()
#s.sketch()


