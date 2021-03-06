import logging

person = logging.Logger(__name__, level=logging.INFO)

fileformat = logging.Formatter('%(asctime)s | %(name)-10s | %(levelname)-16s | %(msecs)s | %(message)s')

l = logging.FileHandler('person.log')
l.setFormatter(fileformat)

person.addHandler(l)


class Person():
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
        person.warning("Person created! {} {}".format(self.name, self.family))

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a):
        if a > 0:
            self._age = a
        else:
            person.critical("invalid age!")
            self._age = 0
