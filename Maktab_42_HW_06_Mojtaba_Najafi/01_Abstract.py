from abc import abstractmethod, ABC


class Shape(ABC):
    def __int__(self, x, y=None):
        self.x = x
        self.y = y

    @staticmethod
    @abstractmethod
    def perimiter():
        pass

    @staticmethod
    @abstractmethod
    def area(self):
        pass

    def sketch(self):
        pass

    # def concat_area(self,rectangle=[]):
    #     total_area = 0
    #     for i in rectangle:
    #          total_area += area(i)
    #     return total_area

class Square(Shape):
    def __int__(self, x):
        super(Square, self).__int__(x)


    def perimiter(self,x):
        return self.x * 4

    def area(self,x):
        return self.x**2

    def sketch(self,x):
        for i in range(x):
            for i in range(x):
                print('*', end='  ')
            print()
    # @staticmethod
    # def con (a):
    #     t = 0
    #     for i in len(a):
    #         t = sum(a(i))
    #     return t

    @staticmethod
    def draw_concat(a, b, c):
        for i in range(a):
            for i in range(a):
                print('*', end='  ')
            print()
        for j in range(b):
            for j in range(b):
                print('*', end='  ')
            print()

        for k in range(c):
            for k in range(c):
                print('*', end='  ')
            print()


s = Square()
#s.draw_concat(2, 5, 3)
l = [2,3,4,5]
#print(s.con(l))


