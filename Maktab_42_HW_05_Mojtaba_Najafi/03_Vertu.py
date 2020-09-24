class Paper:
    def __init__(self, title, owner=[]):
        self.title = title
        if self.__is_valid():
            type(self.owner) == owner
        else:
            print("invalid owner")

    def __repr__(self):
        return str({'title': self.title, 'owner': self.owner})
    def __str__(self):
        return str(self.title)

    def __is_valid(self,owners):
        # if Article.owner ==isinstance(Researcher) and Book.owner ==isinstance(Author) and Poetry.owner ==isinstance(Poet):
        #     return True
        # else:
        #     return False
        return True


class Person:
    def __init__(self, name, email=None, gender=None):
        self.name = name
        self.email = email
        self.gender = gender

    def __repr__(self):
        return str({'name': self.name, 'email': self.email, 'gender': self.gender})

    def __str__(self):
        return str(self.name)
class Article(Paper):
    def __init__(self, journal, year, title, owner):
        super(Article, self).__init__(title, owner)
        self.journal = journal
        self.year = year

    def __repr__(self):
        return str({'journal': self.journal, 'year': self.year, 'title': self.title, 'owner': self.owner})


class Poetry(Paper):
    def __init__(self, title, owner, poem_format=None):
        super(Poetry, self).__init__(title, owner)
        self.poem_format = poem_format
        if owner < 1: print("Invalid parameter for poetry")

    def __repr__(self):
        return str({'title': self.title, 'owner': self.owner, 'poem_format': self.poem_format})


class Book(Paper):
    def __init__(self, title, owner, isbn, publisher=None):
        super(Book, self).__init__(title, owner)
        self.ISBN = isbn
        self.publisher = publisher
        self.count += 1

    def __del__(self):
        self.count -= 1

    def __repr__(self):
        return str({'title': self.title, 'owner': self.owner, 'isbn': self.isbn, 'publisher': self.publisher})


class Researcher(Person):
    def __init__(self, name, email, gender, field, university=None):
        super(Researcher, self).__init__(name, email, gender)
        self.field = field
        self.university = university

    def __repr__(self):
        return str({'name': self.name, 'email': self.email, 'gender': self.gender, 'field': self.field,
                'university': self.university})


class Poet(Person):
    def __init__(self, name, email, gender, style=None):
        super(Poet, self).__init__(name, email, gender)
        self.style = style

    def __repr__(self):
        return str({'name': self.name, 'gender': self.gender, 'style': self.style})


class Author(Person):
    def __init__(self, name, email, gender, code, genre=None):
        super(Author, self).__init__(name, email, gender)
        self.code = code
        self.genre = genre

    def __repr__(self):
        return str({'name': self.name, 'email': self.email, 'gender': self.gender, 'code': self.code, 'genre': self.genre})
    # def __str__(self):
    #     return {'name' : self.name}

b = Author('me', 'me@mail.com', 'male', 123, 'Drama')
c = Author('me1', 'me@mail.com', 'male', 123, 'Drama')
d = Author('me2', 'me@mail.com', 'male', 123, 'Drama')
e = Author('me3', 'me@mail.com', 'male', 123, 'Drama')
l = [b,c,d,e]
A = Article("nature", 2020, 'Python', l)
print(A.owner)
