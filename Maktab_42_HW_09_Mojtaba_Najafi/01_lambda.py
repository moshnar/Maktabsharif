import timeit

"""Creating a function with lambda is slightly faster than creating it with def.
 The difference is due to def creating a name entry in the locals table.
  The resulting function has the same execution speed."""


def f(x): return x + 2
g = lambda x: x + 2

print(timeit.timeit('f(3)', globals=globals()))
print(timeit.timeit('g(3)', globals=globals()))