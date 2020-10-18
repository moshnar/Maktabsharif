def exception_handler(func):
    """generic decorator for exception handling"""
    def func_wrapper(*args, **kwargs):

        try:
           return func(*args, **kwargs)

        except Exception as e:

            print(f'Error : {e}')
            return None

    return func_wrapper


@exception_handler
def area_square(length):
    print(length * length)


@exception_handler
def area_circle(radius):
    print(3.14 * radius * radius)


@exception_handler
def area_rectangle(length, breadth):
    print(length * breadth)

@exception_handler
def div(x,y):
    return x/y


area_square(2)
area_circle(2)
area_rectangle(2, 4)
area_square("some_str")
area_circle("some_other_str")
area_rectangle("some_other_rectangle")
div(0,0)


