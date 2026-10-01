# circle,rectangle ,square, triangele area
def circle(r):
    return 3.14 * a * a


def rectangle(a, b):
    return a * b


def square(a):
    return a * a


def triangle(a, b):
    return 0.5 * a * b


while True:
    print("Area Calculator")
    print("1 :- Circle")
    print("2 :- Rectangle")
    print("3 :- Square")
    print("4 :- Triangle")
    print("5 :- Exit")
    choice = int(input("Enter Your choice:- "))

    if choice == 1:
        a = float(input("Enter radius: "))
        print("Result:-", circle(a))

    elif choice == 2:
        a = float(input("Enter the 1st Value:- "))
        b = float(input("Enter the 2nd Value:- "))
        print("Result:-", rectangle(a, b))

    elif choice == 3:
        a = float(input("Enter the Value:- "))
        print("Result:-", square(a))

    elif choice == 4:
        a = float(input("Enter base: "))
        b = float(input("Enter height: "))
        print("Result:-", triangle(a, b))

    else:
        print("Exited")
        break
