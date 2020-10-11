from person import Person
import logging

logging.basicConfig(format='%(asctime)s- %(levelname)s- %(funcName)s- %(lineno)d \
:: %(message)s', level = logging.INFO , filename='sub.log')


def sub(a, b):
    if b != 0:
        return a / b
    logging.debug("a / b = " + str(a / b))
    logging.info("Divide by zero!")



print(sub(2, 3))
#print(sub(2, 0))
p1 = Person("ali", "alavi", 23)
p2 = Person("gholi", "gholami", -23)
