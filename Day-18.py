# 2. Create a Rectangle class with length and breadth. Add methods to calculate area and perimeter. Create an object and display both values.
"""
class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

    def perimeter(self):
        return 2 * (self.l + self.b)


r = Rectangle(10, 5)

print("Area:", r.area())
print("Perimeter:", r.perimeter())
"""

# 3. Create a Car class with brand, model, and color. Add a method display_info() to print the car details. Create two objects with different values.
"""
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Color:", self.color)


car1 = Car("Toyota", "Camry", "Blue")
car2 = Car("Honda", "Civic", "Red")

car1.display_info()
car2.display_info()
"""

# 4. Create a Circle class with radius. Add methods to calculate area and circumference. Create an object and display the results (use 3.14 for π).
"""
class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r**2

    def circumference(self):
        return 2 * 3.14 * self.r


c = Circle(7)
print("Area:", c.area())
print("Circumference:", c.circumference())
"""

# 5. Create a Book class with title, author, and price. Add a method to display all details. Create three objects for three different books.
"""
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 12.99)
book3 = Book("1984", "George Orwell", 9.99)

book1.display_details()
book2.display_details()
book3.display_details()
"""

# 6. Create an Employee class with name, employee_id, and monthly_salary. Use a constructor to initialize the values. Add a method to calculate and display annual salary.
"""
class Employee:
    def __init__(self, name, employee_id, monthly_salary):
        self.name = name
        self.employee_id = employee_id
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12

    def display_info(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Monthly Salary:", self.monthly_salary)
        print("Annual Salary:", self.annual_salary())


person1 = Employee("Piyush Jain", "E123", 100000)
person1.display_info()
"""

# 7. Create a BankAccount class with account_holder and balance. Add deposit(amount), withdraw(amount), and display_balance() methods. Do not allow withdrawal if the balance is insufficient.
"""
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance for withdrawal.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.balance}")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}, Balance: {self.balance}")

person1 = BankAccount("Piyush Jain", 10000)
person1.display_balance()
person1.deposit(5000)
person1.withdraw(2000)
"""

# 8. Create a Laptop class with brand, RAM, and price. Use a constructor to initialize these attributes. Add a method that displays the laptop details.
"""
class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price

    def display_details(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram)
        print("Price:", self.price)

laptop1 = Laptop("Apple", "16 GB", 99900)
laptop1.display_details()
"""

# 9. Create a Temperature class with temperature in Celsius. Add methods to convert it to Fahrenheit and Kelvin. Display both converted values.
"""
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    def to_kelvin(self):
        return self.celsius + 273.15

    def display_conversions(self):
        print(f"Temperature in Celsius: {self.celsius}")
        print(f"Temperature in Fahrenheit: {self.to_fahrenheit()}")
        print(f"Temperature in Kelvin: {self.to_kelvin()}")

temp1 = Temperature(25)
temp1.display_conversions()
"""

# 10. Create a Rectangle class with length and breadth. Add a method to return its area. Create two objects and display which rectangle has the larger area, or whether both areas are equal.
"""
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


r1 = Rectangle(10, 5)
r2 = Rectangle(8, 7)

if r1.area() > r2.area():
    print("Rectangle 1 has a larger area")
elif r2.area() > r1.area():
    print("Rectangle 2 has a larger area")
else:
    print("Both rectangles have equal areas")
"""

# 11. Create a LibraryBook class with title, author, and availability. Add issue_book() and return_book() methods. Display a suitable message when a book is already issued.
"""
class LibraryBook:
    def __init__(self, title, author, availability=True):
        self.title = title
        self.author = author
        self.availability = availability

    def issue_book(self):
        if self.availability:
            self.availability = False
            print(self.title, "has been issued")
        else:
            print(self.title, "is already issued")

    def return_book(self):
        if not self.availability:
            self.availability = True
            print(self.title, "has been returned")
        else:
            print(self.title, "is already available")


book1 = LibraryBook("Python Basics", "John Smith")

book1.issue_book()
book1.issue_book()
book1.return_book()
"""

# 12. Create an Item class with item_name, price, and quantity. Add a method to calculate the total cost. Create objects for at least two items and display each total.
"""
class Item:
    def __init__(self, item_name, price, quantity):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity


item1 = Item("Pen", 10, 5)
item2 = Item("Notebook", 50, 3)

print(item1.item_name, "Total Cost:", item1.total_cost())
print(item2.item_name, "Total Cost:", item2.total_cost())
"""

'''

class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def purchase(self, quantity):
        if quantity <= 0:
            print("Quantity must be positive")
        elif quantity <= self.stock:
            self.stock -= quantity
            print("Updated Stock:", self.stock)
        else:
            print("Not enough stock")

    def restock(self, quantity):

        if quantity > 0:
            self.stock += quantity
            print("Updated Stock:", self.stock)
        else:
            print("Quantity must be positive")


p1 = Product(101, "Pen", 10, 20)
p1.purchase(5)
p1.restock(10)
p1.purchase(30)
'''

