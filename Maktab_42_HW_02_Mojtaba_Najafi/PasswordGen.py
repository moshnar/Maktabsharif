import random
import string


class passwordGen():
    pass


def password_generator(length=10):
    # Initializing all items
    L, N, P, U = string.ascii_letters, string.digits, string.punctuation, string.ascii_uppercase

    # make a string of all items
    printable = f'{L}{N}{P}'

    # convert printable from string to list and shuffle
    printable = list(printable)
    random.shuffle(printable)

    # generate random password and convert to string
    random_password1 = random.choices(U, k=2)
    random_password2 = random.choices(N, k=1)
    random_password3 = random.choices(P, k=1)
    random_password4 = random.choices(printable, k=length - 4)
    # join all requirment
    random_password = random_password1 + random_password2 + random_password3 + random_password4
    # make sure 2 uppercase 1 digit and 1 Punctuation distribute randomly along the password
    random_password = ''.join(random.sample(random_password, len(random_password)))

    return random_password


if __name__ == '__main__':
    print(password_generator(22))
