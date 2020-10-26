def hailstone(n):
    """ takes n as an argument and yield a number from hailstone sequence"""
    yield n
    while n > 1:
        n = n // 2 if n % 2 == 0 else n * 3 + 1
        yield n


def square(*args):
    """takes args and returns square of each args once at a time"""
    for p in args:
        yield p ** 2


def sum_hs_square(*args):
    """combines square and hs to sum up values"""
    sum1 = []
    for e in args:
        x = square(e)
        for t in x:
            sum1.append(next(hailstone(t)))

    print(sum(sum1))


# s = square(1,2,3,4,5)
# print(next(s))
# print(next(s))
# print(next(s))

sum_hs_square(1, 2, 3, 4, 5)
