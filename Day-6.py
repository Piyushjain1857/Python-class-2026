# For loop
"""
fruits = ["Apple", "Banana", "Vherry"]
for i in fruits:
    print(i)
"""

# While loop
"""
count = 1
while count <= 5:
    print(f"Count is:- {count}")
    count += 1
"""

# range() function
# range(start)
"""
for i in range(5):
    print(i)
"""

# range(Start,Stop)
"""
for i in range(2, 6):
    print(i)
"""

# range(Start,Stop,Step)
"""
for i in range(10, 0, -2):
    print(i)
"""

# Real World Examples
# an e-commerce app calculates the total bill for items in a shopping cart.
"""
prices = [299, 150, 499, 999]
total = 0
for price in prices:
    total += price
print("Total bill: Rs.", total)
"""

# Attendance / Login Retry System
"""
attempts = 0
correct_password = "python123"

while attempts < 3:
    entered = input("Enter password: ")
    if entered == correct_password:
        print("Access granted")
        break
    attempts += 1
else:
    print("Account locked")
"""

# Weekly Report Dates
"""
for day in range(1, 8):
    print("Day", day, "- Sales report generated")
"""

# Write a program to find the sum of the first n natural numbers using a for loop.
"""
n = 10
total = 0
for i in range(1, n + 1):
    total += i
print("Sum:", total)
"""

# Print the multiplication table of a given number using range().
"""
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
"""
