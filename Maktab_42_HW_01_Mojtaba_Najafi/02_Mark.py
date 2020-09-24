while True:
    n = int(input("enter your Mark"))
    if n < 10:
        print("failed")
    elif n >= 10 and n < 15:
        print("not bad")
    elif n >= 15 and n < 18:
        print("good")
    elif n >= 18:
        print("excellent")
