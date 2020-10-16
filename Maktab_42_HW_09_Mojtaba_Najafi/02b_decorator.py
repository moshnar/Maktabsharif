def decorator(*args,**kwargs):

    def inner(func):

        func(*args,kwargs)



    return inner






@decorator(10)
def fee(price):
    return 1.09 * price

print(fee(20))