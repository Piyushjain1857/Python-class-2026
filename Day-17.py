# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def start(self):
#         print(f"{self.color} {self.brand} is starting... vroom!")

# car1 = Car("Honda", "Red")
# car2 = Car("Toyota", "Blue")
# car3 = Car("Tesla", "White")

# car1.start()
# car2.start()
# print(car3.brand)

# class Student:
#     def __init__(self):
#         self.__marks = 90

# s1 = Student()

# print(s1._Student__marks)  # Accessing the private attribute using name mangling

# class Employee:

#     def __init__(self):
#         self.__salary = 50000

#     def display_salary(self):
#         print("Salary:", self.__salary)


# emp = Employee()
# emp.display_salary()
# print(f"Salary: {emp._Employee__salary}")  # Accessing the private attribute using name mangling


# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)


# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year

#     def welcome(self, anothername):
#         print(
#             "Welcome",
#             self.firstname,
#             self.lastname,
#             "to the class of",
#             self.graduationyear, anothername
#         )


# x = Student("Piyush", "Jain", 2026)
# x.welcome('Alice')  # Output: Welcome Piyush Jain to the class of 2026 Alice

# Create the Animal class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)


# Create the Dog class (inherits from Animal)
class Dog(Animal):
    pass


# Create an object
d1 = Dog("Rex")
# Call the speak method
d1.speak()



