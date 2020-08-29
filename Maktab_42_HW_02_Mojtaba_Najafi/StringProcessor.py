import string
def StringSpliter(n):
    n = n.split()
    return n


def Cleaner (str):

    str=StringSpliter(str)
    list = [x[0] for x in str]
    print(list)

    for i in list:

        if i in string.ascii_letters:
            print(''.join(i.capitalize()))

print(Cleaner("Hi my name is moj@34 54 ** 7   bb ! * * * n"))