# from math import sqrt
# from statistics import mean
#
# fun1 = lambda a, b, c: a + b + c / 3
# print(f'sum of three numbers is : {fun1(2, 4, 5)}')
#
# func2 = lambda *args: mean(args)
#
# print(f'The mean of args ar : {func2(1, 2, 3, 4, 5, 6, 7, 10)}')
#
# func3 = lambda *args, n=2: sum(i ** n for i in args) ** (1 / n)
#
# print(f'norm of n is : {func3(3, 2, 4, 7, 8, n=3)}')
#
# func4 = lambda x : x.sort(reverse=True)
# l = [1,2,3,4,5]
# e = []
# func4(l)
# func4(e)
# print(l)
#
# func5 = lambda x : sorted(x,reverse=True )
# s = 'a','b','c','d','z'
# print(func5(s))


# def warp (fun , arg):
#     return fun(arg)
#
#
#
# high_ord = lambda f , y : f(y) + y
# print(high_ord(lambda x : x + 3,12))
# print(high_ord(lambda x : x**2,12))
import functools


def debug(func):
    @functools.wraps(func)
    def wrapper(*func_args, **func_kwargs):
        print(f'Calling :   {func.__name__}  ()')
        print(f'function args are : {func_args}')
        retval = func(*func_args,**func_kwargs)
        print(f'function   {func.__name__}  () returns  {repr(retval)}')
        return retval
    return wrapper

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, youare growing up!"


make_greeting('Mamad',22)

