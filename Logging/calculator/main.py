import sys
import time

from logic.calc import *
from logic.parse import *

operator_dict = {"*": mul, "+": add, "-": sub, "/": div}

while True:
    try:
        usr_input = input("Start a math operation \n").split(" ")

        if usr_input[0] == "exit":
            break
        else:
            animation = "|/-\\"
            print('Processing a heavy operation...')
            for i in range(100):
                time.sleep(0.1)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()
            print('\n', end='')
            print('The answer is : ')
            check_format(usr_input)
            first_operand, operator, second_operand = usr_input[0], usr_input[1], usr_input[2]

            check_operator(operator)
            operands = check_operand(first_operand, second_operand)

            print(operator_dict[operator](operands[0], operands[1]))

    except InvalidFormatException:
        print("format is invalid")
    except InvalidNumberException:
        print("operands are not number")
    except InvalidOperatorException:
        print("operation is not valid")
    except ZeroDivisionError:
        print("Division by Zero")
