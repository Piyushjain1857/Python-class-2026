# accept any number of positional arguments
"""
def total_marks(*marks):
    return sum(marks)

print(total_marks(40, 80, 89,100,150))
print(total_marks(20, 25, 35, 55))
"""

# accept any number of key-word arguments
"""
def info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

info(name="Piyush", sur_name="Jain")
"""

# Calling a Function Recursively
"""
def factorial(n):
    if n == 0:  
        return 1
    return n * factorial(n - 1) 

n=int(input("Enter A number:-"))
print(factorial(n))
"""

# Q1. Write a function greet_user() that takes no arguments and prints “Hello, Python learner!”. Call it twice. (No-argument call)


def greet_user():
    print("Hello,Python Learner!")


greet_user()
greet_user()
