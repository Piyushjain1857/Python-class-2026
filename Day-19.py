# a = int(input("Pl enter a number:- "))

# for i in range(11):
#     if i == a:
#         continue
#     print(i)
#     print("Hello")

# # class and object


# class Bmi:
#     def __init__(self, h, w):
#         self.hight = h
#         self.weight = w

#     def calculator(self):
#         return self.weight / (self.hight ** 2)

# class HealthCheckup(Bmi):
#     def __init__(self, h, w, age):
#         super().__init__(h, w)
#         self.age = age

#     def health_status(self):
#         bmi_value = self.calculator()
#         if bmi_value < 18.5:
#             return "Underweight"
#         elif 18.5 <= bmi_value < 24.9:
#             return "Normal weight"
#         elif 25 <= bmi_value < 29.9:
#             return "Overweight"
#         else:
#             return "Obesity"

# person1 = HealthCheckup(1.75, 70, 30)
# print("BMI:- ", person1.calculator())
# print("Health Status:- ", person1.health_status())


# exception handling
# l = [1, 2, 3]
# n = int(input("Enter a number:- "))

# try:
#     print(l[n])
# except IndexError:
#     print("Index out of range.")

bal = 500
amount = int(input("Enter the amount to withdraw:- "))
if amount < 0:
    raise ValueError("Amount cannot be negative")
if amount > bal:
    raise ValueError("Insufficient balance")
else:
    try:
        bal -= amount
        print("Withdrawal successful. Remaining balance:", bal)
    except ValueError as e:
        print(e)
