balance = 0


def deposit(amount):
    global balance
    balance = balance + amount
    print("Amount Deposited:", amount)


def withdraw(amount):
    global balance

    if amount <= balance:
        balance = balance - amount
        print("Amount Withdrawn:", amount)
    else:
        print("Insufficient Balance")


def check_balance():
    print("Current Balance:", balance)


while True:
    print("Banking System")
    print("1 :- Deposit")
    print("2 :- Withdraw")
    print("3 :- Check Balance")
    print("4 :- Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        amount = float(input("Enter Amount to Deposit: "))
        deposit(amount)

    elif choice == "2":
        amount = float(input("Enter Amount to Withdraw: "))
        withdraw(amount)

    elif choice == "3":
        check_balance()

    elif choice == "4":
        print("Thank you for using Banking System!")
        break

    else:
        print("Invalid Choice")