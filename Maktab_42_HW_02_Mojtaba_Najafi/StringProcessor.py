import string


# using built-in function to split the arg
def StringSpliter(n):
    n = n.split()
    return n


def Cleaner(str):
    str = StringSpliter(str)
    # taking first letter of the each item in the list using list comprehension
    list = [x[0] for x in str]

    for i in list:
        # cheking if the letter is either lower or upper case
        if i in string.ascii_letters:
            # joing the the letters and make the capital
            print(''.join(i.capitalize()))


print(Cleaner("Hi my name is moj@34 54 ** 7   bb ! * * * n"))
