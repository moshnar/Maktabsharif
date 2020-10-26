import logging

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d \
:: %(message)s', level=logging.INFO, filename='name.log')
logger = logging.getLogger(__name__)

logging.debug('print debug')
logging.info('infor printed')


def Fibonacci(n):
    logging.info(f'n is {n} ')
    if n <= 0:
        logging.error("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


# print(Fibonacci(10))
print(Fibonacci(-10))
