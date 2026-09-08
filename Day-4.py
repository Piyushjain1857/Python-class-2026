# Q1. ATM Withdrawal 💳
balance = float(input("Enter account balance: Rs. "))
withdrawal = float(input("Enter withdrawal amount: Rs. "))
if withdrawal <= balance:
    balance -= withdrawal
    print(f"Withdrawal successful. Remaining balance: Rs. {balance}")
else:
    print("Insufficient Balance")
