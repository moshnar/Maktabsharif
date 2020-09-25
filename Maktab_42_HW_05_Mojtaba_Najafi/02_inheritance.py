class A:
    def do_job(self, *args, **kwargs):
        if type(self) in [E, C]:
            super().do_job(*args, **kwargs)
        print('I am walking ...')


class Z:
    def do_job(self, n, *args, **kwargs):
        if type(self) == F:

            super().do_job(*args, **kwargs)
        print(f'I am counting from 1 to {n}: {list(range(1, n + 1))}')


class B(A):
    def do_job(self, s, *args, **kwargs):
        super().do_job(*args, **kwargs)
        print(f'I am printing your string : "{s}"')


class C(A, Z):
    def do_job(self, *args, **kwargs):
        super().do_job(*args, **kwargs)
        print('I am jumping ...')


class D(B):
    def do_job(self, *args, **kwargs):
        super().do_job(*args, **kwargs)
        print('I am speaking ...')


class E(D, C):
    def do_job(self, s, n):
        super().do_job(s, n)
        print('I am laughing ...')


class F(Z, B):
    def do_job(self, s, n):
        super().do_job(n, s)
        print('I am playing ...')

obja = A()
obja.do_job()
print()

objz = Z()
objz.do_job(3)
print()

obje = E()
obje.do_job('Python', 5)
print()

objf = F()
objf.do_job('Python', 6)
