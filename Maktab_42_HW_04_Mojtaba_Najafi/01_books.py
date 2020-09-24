class Books:
    total = 0

    def __init__(self, title, price, author):  # initializing the variables
        self.title = title
        self.price = price
        if type(author) == list:

            self.author = author
        else:
            self.author = [author]
        Books.total += 1

    def show_info(self):  # print out the book info
        print(f' The title is {self.title} and the price is  {self.price} written by {self.author} Books')

    # def author(self, name, email, gender):  # creat an author
    #     self.name = name
    #     self.email = email
    #     self.gender = gender

    def total_books(self):  # shows  the total number of books which are instantiated
        print(Books.total)


class Author:
    def __init__(self, name, email, gender):  # creat an author
        self.name = name
        self.email = email
        self.gender = gender


a1 = Author('J.K. rowling', 'j@mail.com', 'F')

b1 = Books('Harry potter', 10, 'J.K. rowling')
b2 = Books('War and Peace', 15, 'Leo Tolstoy')

b1.show_info()
b2.show_info()
b2.total_books()
