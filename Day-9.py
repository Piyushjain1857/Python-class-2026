# accept any number of positional arguments

def total_marks(*marks):
    return sum(marks)

print(total_marks(40, 80, 89))
print(total_marks(20, 25, 35, 55))
