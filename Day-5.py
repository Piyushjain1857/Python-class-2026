purchase_amount = 1200
premium_member = True

if purchase_amount >= 1000:
    if premium_member:
        print("25% Discount Applied")
    else:
        print("10% Discount Applied")
else:
    print("No Discount")
