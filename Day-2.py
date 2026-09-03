# Bill calculator

Product_1 = int(input("Enter the price of product 1: "))
Product_2 = int(input("Enter the price of product 2: "))
Product_3 = int(input("Enter the price of product 3: "))

Sum = Product_1 + Product_2 + Product_3
Discounted_bill = Sum - 0.20 * Sum 
Total = Discounted_bill + 0.05 * Discounted_bill

print("The total bill is: ", Total)
