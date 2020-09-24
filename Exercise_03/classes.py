class Smith:
    surname = 'Smith'
    profession = 'smith'

    def __init__(self, name, profession=None):
        self.name = name
        if profession is not None:
            self.profession = profession


John = Smith('John')
print(John.name)
print(John.surname)
print(John.profession)

mike = Smith('Mike', 'Employee')
print(mike.name)
print(mike.surname)
print(mike.profession)
