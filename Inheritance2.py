# Q10. Product Billing System
# Create a parent class Product with product ID, product name, and price.
# Create a child class Electronics with warranty period.
# Create another child class Clothing with size.
# Display product details and calculate the final price after applying a discount.

class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

    def display_details(self):
        print("Product ID:", self.product_id)
        print("Product Name:", self.product_name)
        print("Price:", self.price)

    def final_price(self, discount):
        return self.price - (self.price * discount / 100)


class Electronics(Product):
    def __init__(self, product_id, product_name, price, warranty):
        super().__init__(product_id, product_name, price)
        self.warranty = warranty

    def display_details(self):
        super().display_details()
        print("Warranty:", self.warranty, "years")


class Clothing(Product):
    def __init__(self, product_id, product_name, price, size):
        super().__init__(product_id, product_name, price)
        self.size = size

    def display_details(self):
        super().display_details()
        print("Size:", self.size)


e1 = Electronics(101, "Laptop", 50000, 2)
c1 = Clothing(102, "Shirt", 1500, "M")

print("Electronics Details:")
e1.display_details()
print("Final Price:", e1.final_price(10))

print("\nClothing Details:")
c1.display_details()
print("Final Price:", c1.final_price(20))