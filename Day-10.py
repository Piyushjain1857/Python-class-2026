"""
def greet():
    message="Hello,Piyush"
    print(message)

greet()

# print(message) #It will show name error
"""

"""
for i in range(1,6):
    count=0
    count+=1
    print(count)

print(count)
"""

"""
count = 100

def display():
    print(count)
def increament():
    global count
    count += 1  

increament()
display()
"""

"""
score = 0


def add_points():
    global score
    score += 10

def reduce_points():
    global score
    score -= 10


add_points()
add_points()
# reduce_points()
print(score)
"""


def outer():
    name = "Piyush Jain"

    def inner():
        print(name)

    inner()


outer()
