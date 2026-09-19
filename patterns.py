# ==================================================
# 1. RIGHT TRIANGLE - STAR PATTERN
# ==================================================
#
# *
# * *
# * * *
# * * * *
# * * * * *
#

n = int(input("Enter rows: "))

for i in range(1, n + 1):
    print("* " * i)


# ==================================================
# 2. INVERTED RIGHT TRIANGLE - STAR PATTERN
# ==================================================
#
# * * * * *
# * * * *
# * * *
# * *
# *
#

n = int(input("Enter rows: "))

for i in range(n, 0, -1):
    print("* " * i)


# ==================================================
# 3. PYRAMID - STAR PATTERN
# ==================================================
#
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
#

n = int(input("Enter rows: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)


# ==================================================
# 4. INVERTED PYRAMID - STAR PATTERN
# ==================================================
#
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
#

n = int(input("Enter rows: "))

for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)


# ==================================================
# 5. SQUARE - STAR PATTERN
# ==================================================
#
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
#

n = int(input("Enter rows: "))

for i in range(n):
    print("* " * n)


# ==================================================
# 6. RIGHT TRIANGLE - NUMBER PATTERN
# ==================================================
#
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
#

n = int(input("Enter rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# ==================================================
# 7. INVERTED - NUMBER PATTERN
# ==================================================
#
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
#

n = int(input("Enter rows: "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# ==================================================
# 8. PYRAMID - NUMBER PATTERN
# ==================================================
#
#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5
#

n = int(input("Enter rows: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for j in range(1, i + 1):
        print(j, end=" ")

    print()


# ==================================================
# 9. REPEATED NUMBER PATTERN
# ==================================================
#
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
#

n = int(input("Enter rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()


# ==================================================
# 10. FLOYD'S TRIANGLE - NUMBER PATTERN
# ==================================================
#
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
#

n = int(input("Enter rows: "))

num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1

    print()
