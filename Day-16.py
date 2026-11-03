def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)

print(sum(5))  # Output: 15


# what is gcd:- Greatest Common Divisor
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

gcd_result = gcd(48, 18)
print(gcd_result)  # Output: 6