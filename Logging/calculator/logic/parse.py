from exceptions import InvalidNumberException, InvalidOperatorException, InvalidFormatException


def check_format(math_operation):
    if len(math_operation) != 3:
        raise InvalidFormatException()


def check_operator(a_operator):
    if a_operator not in ["*", "/", "-", "+"]:
        raise InvalidOperatorException()


def is_num(n):
    try:
        float(n)
        return True
    except ValueError:
        raise InvalidNumberException()


def is_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def check_operand(*args):
    operands = []

    for i in args:
        if is_num(i):
            operands.append(int(i)) if is_int(i) else operands.append(float(i))
    return operands
