def add(a, b):
    c = a + b
    return c, "+"


def subtract(a, b):
    c = a - b
    return c, "-"

def multiply(a, b):
    c = a * b
    return c, "*"
def divide(a, b):
    c = a / b
    return c, "/"


if __name__ == "__main__":
    a = 47
    b = 7
    answer, symbol = add(a, b)
    print("{} {} {} = {}".format(a, symbol, b, answer))
    answer, symbol = subtract(a, b)
    print("{} {} {} = {}".format(a, symbol, b, answer))
    answer, symbol = multiply(a, b)
    print("{} {} {} = {}".format(a, symbol, b, answer))
    answer, symbol = divide(a, b)
    print("{} {} {} = {}".format(a, symbol, b, answer))
    d = float(input("Enter First Number: "))
    e = float(input("Enter Second Number: "))
    answer, symbol = add(d, e)
    print("{} {} {} = {}".format(d, symbol, e, answer))
    answer, symbol = subtract(d, e)
    print("{} {} {} = {}".format(d, symbol, e, answer))
    answer, symbol = multiply(d, e)
    print("{} {} {} = {}".format(d, symbol, e, answer))
    answer, symbol = divide(d, e)
    print("{} {} {} = {}".format(d, symbol, e, answer))

