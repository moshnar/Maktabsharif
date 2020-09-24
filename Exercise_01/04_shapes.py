def egg():
    top()
    bottom()
    print()


def cup():
    bottom()
    line()
    print()


def stop():
    top()
    print("| STOP |")
    bottom()
    print()


def hat():
    top()
    line()
    print()


def top():
    print("        ")
    print("/------\\")
    print("/      \\")


def bottom():
    print("\\      /")
    print(" \______/")


def line():
    print("+______+")


egg()
cup()
stop()
hat()
