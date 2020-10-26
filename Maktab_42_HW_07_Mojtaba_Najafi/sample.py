import logging

from level_counter import level_counter
from person import Person

sample = logging.Logger(__name__, level=logging.INFO)

fileformat = logging.Formatter('%(asctime)s | %(name)-10s | %(levelname)-16s | %(msecs)s | %(message)s')
streamformat = logging.Formatter('%(asctime)s | %(name)-10s | %(message)s')

file_handler = logging.FileHandler('sample.log')
file_handler.setFormatter(fileformat)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(streamformat)
stream_handler.setLevel(logging.ERROR)

sample.addHandler(file_handler)
sample.addHandler(stream_handler)


def sub(a, b):
    if b != 0:
        sample.debug('a / b = ' + str(a / b), exc_info=1)
        return a / b

    else:
        sample.info('Divide by zero!')


print(sub(2, 3))
print(sub(2, 0))

p1 = Person('ali', 'alavi', 23)
p2 = Person('gholi', 'gholami', -23)

try:
    print(level_counter('person.log', logging.WARNING))
    print(level_counter('sample.log', logging.INFO))

except FileNotFoundError:
    sample.error('File not found for checking levels', exc_info=True)

except:
    print('Instance of log level not found')
