def calculate(first_number, operator, second_number):
    if operator == "+":
        return first_number + second_number
    if operator == "-":
        return first_number - second_number
    if operator == "*":
        return first_number * second_number
    if operator == "/":
        if second_number == 0:
            raise ValueError("Cannot divide by zero")
        return first_number / second_number
    raise ValueError("Invalid operator")


try:
    first_number = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ").strip()
    second_number = float(input("Enter the second number: "))
    print("Result:", calculate(first_number, operator, second_number))

except ValueError as error:
    print("Error:", error)
