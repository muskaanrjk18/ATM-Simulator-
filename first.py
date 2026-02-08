# ATM Simulator 

import sys

balance = 5000
pin = "1234"

def check_pin():
    user_pin = input("Enter your 4-digit PIN: ")
    if user_pin == pin:
        return True
    else:
        print("❌ Incorrect PIN!")
        return False

def show_menu():
    print("\n ATM MENU ")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def check_balance():
    print(f" Your current balance is: ₹{balance}")

def deposit_money():
    global balance
    amount = int(input("Enter amount to deposit: ₹"))
    if amount > 0:
        balance += amount
        print(f"✅ ₹{amount} deposited successfully!")
        print(f"New Balance: ₹{balance}")
    else:
        print("❌ Invalid amount!")

def withdraw_money():
    global balance
    amount = int(input("Enter amount to withdraw: ₹"))
    if amount <= 0:
        print("❌ Invalid amount!")
    elif amount > balance:
        print("❌ Insufficient balance!")
    else:
        balance -= amount
        print(f"✅ ₹{amount} withdrawn successfully!")
        print(f"Remaining Balance: ₹{balance}")

def main():
    print("🏧 Welcome to Python ATM Simulator")

    if not check_pin():
        return

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            print(" Thank you for using the ATM. Goodbye!")
            sys.exit()
        else:
            print("❌ Invalid choice! Try again.")

main()
