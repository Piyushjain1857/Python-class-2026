def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers."
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)


while True:
    print("----------------------------------------------")
    print("               MAIN MENU")
    print("----------------------------------------------")
    print("1 :- Factorial")
    print("2 :- Check Prime Number")
    print("3 :- Duplicate Elements of List")
    print("4 :- Exit")
    print("----------------------------------------------")

    choice = input("Enter Your Choice (1-4): ")

    if choice == "1":
        num = int(input("Enter an integer: "))
        result = factorial(num)
        print(f"Result: Factorial of {num} is {result}")

    elif choice == "2":
        num = int(input("Enter an integer: "))
        if check_prime(num):
            print(f"Result: {num} is a Prime Number.")
        else:
            print(f"Result: {num} is NOT a Prime Number.")

    elif choice == "3":
        lst = input("Enter elements of list: ").split()
        seen = set()
        duplicates = set()

        for x in lst:
            if x in seen:
                duplicates.add(x)
            seen.add(x)

        print("Duplicate elements:", duplicates if duplicates else "No duplicates found.")
        
    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")