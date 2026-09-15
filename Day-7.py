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

# method-3
"""
num = int(input("Enter a number: "))
if num <= 1:
    print("Not a prime number")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")
"""
# reverce count down withh while loop
n = 5
while n >= 1:
    print(n)
    n -= 1
print("Light OFF")
