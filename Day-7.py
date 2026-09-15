## Prime no
# method-1
"""
num = int(input("Enter a number: "))
if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
"""

# method-2 (num div by 2)
"""
num = int(input("Enter a number: "))
if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
"""
