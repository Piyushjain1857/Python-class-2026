def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


while True:
    print("Calculator")
    print("+ :- Addition")
    print("- :- Subtraction")
    print("* :- Multiplication")
    print("/ :- Division")
    print("_ :- Exit")
    value = str(input("Exter Your operator."))
    a = float(input("Enter the 1st Value:- "))
    b = float(input("Enter the 2nd Value:- "))

    if value == "+":
        print("Result:-", addition(a, b))
    elif value == "-":
        print("Result:-", subtraction(a, b))
    elif value == "*":
        print("Result:-", multiplication(a, b))
    elif value == "/":
        print("Result:-", division(a, b))
    else:
        print("Exited")
        break
