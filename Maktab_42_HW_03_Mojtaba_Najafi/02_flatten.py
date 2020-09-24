import ast


def read_list(input_str):  # parse the input to the list
    return ast.literal_eval(input_str)


def flatten(xs):  #

    result = []
    if isinstance(xs, list):  # find the sublist and call it recursivly
        for x in xs:
            result.extend(flatten(x))
    else:
        result.append(xs)
    return result


list2 = '[1, 2, [3,4], [5, [6, 7], 8]]'
# list1 = input('Please enter a hetrogenous list')

print(flatten(read_list(list2)))
