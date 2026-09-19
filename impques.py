# 1. Check even/odd
n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")


# 2. Check positive/negative
n = int(input("Enter a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")


# 3. Find largest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a)
else:
    print(b)


# 4. Find largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)


# 5. Check leap year
year = int(input("Enter year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


# 6. Calculate factorial
n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print(factorial)


# 7. Reverse a number
n = int(input("Enter a number: "))
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print(reverse)


# 8. Check palindrome number
n = int(input("Enter a number: "))
original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


# 9. Check prime number
n = int(input("Enter a number: "))
prime = True

if n < 2:
    prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

if prime:
    print("Prime")
else:
    print("Not Prime")


# 10. Print prime numbers
limit = int(input("Enter limit: "))

for n in range(2, limit + 1):
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print(n, end=" ")

print()


# 11. Find sum of digits
n = int(input("Enter a number: "))
sum_digits = 0

while n > 0:
    digit = n % 10
    sum_digits = sum_digits + digit
    n = n // 10

print(sum_digits)


# 12. Count digits
n = int(input("Enter a number: "))
count = 0

if n == 0:
    count = 1
else:
    while n > 0:
        count = count + 1
        n = n // 10

print(count)


# 13. Armstrong number
n = int(input("Enter a number: "))
original = n
count = len(str(n))
sum_digits = 0

while n > 0:
    digit = n % 10
    sum_digits = sum_digits + digit ** count
    n = n // 10

if original == sum_digits:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


# 14. Fibonacci series
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()


# 15. Multiplication table
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)