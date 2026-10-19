# # for i in range(1,6):
# #     for j in range(1,i+1):
# #         print(j, end=" ")
# #     print()

# s = "INFORMATIONTECH"
# # print(s[0:5])
# # print(s[-4::]) #last 4 characters of the string
# # print(s[2:7]) #characters from index 2 to 6

# l1=list(s)
# t1=tuple(s)
# print(l1)
# print(t1)

# fabonacci series

a, b = 0, 1
n = int(input("Enter the number of terms: "))
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence up to", n, ":")
    print(a)
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# with recursion
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series