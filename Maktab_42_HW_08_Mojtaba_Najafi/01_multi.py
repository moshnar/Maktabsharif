from functools import reduce


def multi(*args, sign):
    # print(sign)
    for i in args:
        if type(i) == int:

            if sign == "+":
                return reduce((lambda x, y: x + y), args)
            elif sign == "-":
                try:
                    return reduce((lambda x, y: x - y), args)
                except:
                    raise TypeError
            elif sign == "*":
                return reduce((lambda x, y: x * y), args)
            elif sign == "/":
                return reduce((lambda x, y: x / y), args)


print(multi(1, 2, 3, 4, 5, sign="+"))
print(multi(1, 2, 3, 4, 5, sign="-"))
print(multi(1, 2, 3, 4, 5, sign="*"))
print(multi(1, 2, 3, 4, 5, sign="/"))
