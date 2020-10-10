import logging

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d \
:: %(message)s', level = logging.WARNING , filename='person.log')


class Person:
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
        logging.warning("Person created! {} {}".format(self.name, self.family))
        logging.debug()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a):
        if a > 0:
            self._age = a
        else:
            logging.critical("invalid age!")
            self._age = 0
