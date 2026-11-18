class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Animal Sound"

    def display(self):
        print(f"The name of animal is {self.name}.")


class Dog(Animal):
    # def sound(self):
    #     return "Woof!"

    def walk(self):
        print(f"{self.name} walk on 4 legs.")


class Cat(Animal):
    def sound(self):
        return "Meow!"


class Bird(Animal):
    def sound(self):
        return "Tweet!"


dog1 = Dog("Buddy")
print(dog1.name)
print(dog1.sound())
dog1.display()
dog1.walk()

animal1 = Animal("Bunny")
# animal1.walk()  # This will raise an AttributeError since 'animal' class does not have a 'walk' method
animals = [Dog("Buddy"), Cat("Kitty"), Bird("Tweety")]
for animal in animals:
    print(f"{animal.name} makes sound: {animal.sound()}")

"""
class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


s1 = Square(4)
print(s1.area())
"""
