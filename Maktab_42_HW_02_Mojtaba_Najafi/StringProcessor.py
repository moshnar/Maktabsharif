import string
def StringSpliter(n):
    n = n.split()
    return n


def Cleaner (str):

    str=StringSpliter(str)
    list = [x[0] for x in str]




    for i in list:

        if i in string.ascii_letters:
            print(i)

print(Cleaner("Hi my name is moj@34 54 ** 7    !"))