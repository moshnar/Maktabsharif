import string
import random
def password_generator(length=10):
    L,N,P = string.ascii_letters,string.digits,string.punctuation


    printable = f'{L}{N}{P}'

    # convert printable from string to list and shuffle
    printable = list(printable)
    random.shuffle(printable)

    # generate random password and convert to string
    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)
    return random_password

print(password_generator(10))