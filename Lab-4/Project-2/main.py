import os
from datetime import datetime

CUSTOMER_FILE = "customers.txt"
TRANSACTION_FILE = "transactions.txt"

def log_transaction(account_number, txn_type, amount, new_balance):
    try:
        with open(TRANSACTION_FILE, "a") as f:
            f.write(f"{datetime.now()},{account_number},{txn_type},{amount},{new_balance}\n")
    except Exception as e:
        print(f"Error logging transaction: {e}")

def load_customers():
    customers = {}
    try:
        with open(CUSTOMER_FILE, "r") as f:
            for line in f:
                name, acc_num, balance = line.strip().split(",")
                customers[acc_num] = [name, float(balance)]
    except FileNotFoundError:
        pass  # No customers yet
    return customers

def save_customers(customers):
    try:
        with open(CUSTOMER_FILE, "w") as f:
            for acc_num, (name, balance) in customers.items():
                f.write(f"{name},{acc_num},{balance}\n")
    except Exception as e:
        print(f"Error saving customers: {e}")

def add_customer():
    customers = load_customers()
    name = input("Enter customer name: ").strip()
    acc_num = input("Enter account number: ").strip()
    if acc_num in customers:
        print("Account already exists.")
        return
    customers[acc_num] = [name, 0.0]
    save_customers(customers)
    print("Customer added successfully.")

def deposit():
    customers = load_customers()
    acc_num = input("Enter account number: ").strip()
    if acc_num not in customers:
        print("Account not found.")
        return
    amount = float(input("Enter amount to deposit: "))
    customers[acc_num][1] += amount
    save_customers(customers)
    log_transaction(acc_num, "Deposit", amount, customers[acc_num][1])
    print("Deposit successful.")

def withdraw():
    customers = load_customers()
    acc_num = input("Enter account number: ").strip()
    if acc_num not in customers:
        print("Account not found.")
        return
    amount = float(input("Enter amount to withdraw: "))
    if amount > customers[acc_num][1]:
        print("Insufficient balance.")
        return
    customers[acc_num][1] -= amount
    save_customers(customers)
    log_transaction(acc_num, "Withdraw", amount, customers[acc_num][1])
    print("Withdrawal successful.")

def view_customers():
    customers = load_customers()
    if not customers:
        print("No customers found.")
        return
    print("\n--- Customer List ---")
    for acc_num, (name, balance) in customers.items():
        print(f"Name: {name}, Account: {acc_num}, Balance: {balance}")

def main():
    while True:
        print("\n--- Banking System ---")
        print("1. Add Customer")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Customers")
        print("5. Exit")
        choice = input("Enter choice: ").strip()
        
        if choice == "1":
            add_customer()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            view_customers()
        elif choice == "5":
            print("Exiting Banking System...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
