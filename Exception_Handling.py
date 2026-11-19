# Normal Question
"""
num = int(input("Enter a number: "))
result = 100 / num
print("Result is", result)
"""

# excrption handling
"""
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("That wasn't a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result is", result)
finally:
    print("Done trying.")
"""


# Raising Exceptions
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age


try:
    print(set_age(-5))
except ValueError as e:
    print(e)
