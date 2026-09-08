# 1. ATM Withdrawal 💳
"""
balance = float(input("Enter account balance: Rs. "))
withdrawal = float(input("Enter withdrawal amount: Rs. "))
if withdrawal <= balance:
    balance -= withdrawal
    print(f"Withdrawal successful. Remaining balance: Rs. {balance}")
else:
    print("Insufficient Balance")
"""

# 2. Electricity Bill ⚡
"""
units = float(input("Enter electricity units used: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
print("Total electricity bill: Rs.", bill)
"""

# 3. Student Grade 🎓
"""
marks = float(input("Enter marks (0-100): "))
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")
"""

# Online Shopping Discount 🛒
"""
amount = float(input("Enter total shopping amount: Rs. "))
if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.15
elif amount >= 1000:
    discount = amount * 0.10
else:
    discount = 0
print("Final amount after discount: Rs.", amount - discount)

"""

# 5. Traffic Signal 🚦
"""
signal = input("Enter traffic signal color: ").lower()
if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Get Ready")
elif signal == "green":
    print("Go")
else:
    print("Invalid Signal")
"""

# 6. Movie Ticket Price 🎬
"""
age = int(input("Enter age: "))
if age < 5:
    price = 0
elif age <= 12:
    price = 100
elif age <= 59:
    price = 200
else:
    price = 120
print("Ticket price: Rs.", price)
"""

# 7. Login System 🔐
"""
saved_username = "Piyush_Jain"
saved_password = "Piyush@123"
username = input("Enter username: ")
password = input("Enter password: ")
if username != saved_username:
    print("Invalid Username")
elif password != saved_password:
    print("Invalid Password")
else:
    print("Login Successful")
"""

# 8. Food Delivery Charge 🍕
"""
amount = float(input("Enter order amount: Rs. "))
if amount >= 1000:
    delivery_charge = 0
elif amount >= 500:
    delivery_charge = 50
else:
    delivery_charge = 100
print("Final payable amount: Rs.", amount + delivery_charge)
"""

# 9. Leap Year 📅
"""
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
"""

# 10. Smart Parking System 🚗
"""
spaces = int(input("Enter available parking spaces: "))
if spaces > 0:
    print("Parking Available")
else:
    print("Parking Full")
"""

# 11. Bank Loan Eligibility 🏦
"""
salary = float(input("Enter monthly salary: Rs. "))
credit_score = int(input("Enter credit score: "))
if salary >= 40000 and credit_score >= 700:
    print("Loan Approved")
else:
    print("Loan Not Approved")
"""

# 12. Temperature Warning 🌡️
"""
temperature = float(input("Enter temperature in Celsius: "))
if temperature < 10:
    print("Very Cold")
elif temperature <= 25:
    print("Cold")
elif temperature <= 35:
    print("Normal")
elif temperature <= 45:
    print("Hot")
else:
    print("Extreme Heat")
"""
# 13. Food Delivery Coupon System
"""
amount = float(input("Enter order amount: Rs. "))
coupon = input("Enter coupon code: ").strip().upper()
if amount >= 2000 and coupon == "SAVE20":
    discount = amount * 0.20
elif amount >= 1000 and coupon == "SAVE10":
    discount = amount * 0.10
else:
    discount = 0
print("Original amount: Rs.", amount)
print("Discount: Rs.", discount)
print("Final amount: Rs.", amount - discount)
"""
