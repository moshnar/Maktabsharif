def meta_decorator(dec):
    """This can be applied to a regular decorator in order to add parameters"""
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer

@meta_decorator
def price_in_dollar(f, dollar_price):
    if dollar_price<=0:
        print('price cant be negative or zero')
    """takes a function and Divide the return value with the decorator argument"""
    def aux(*xs, **kws):
        return  f(*xs, **kws) / dollar_price
    return aux

@price_in_dollar(10)
def fee(price):
 return 1.09 * price

print (fee(30))