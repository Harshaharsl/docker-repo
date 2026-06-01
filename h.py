# hello welcome to bank service
balance = 10000

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Your balance is: ₹{balance}")

    elif choice == "2":
        amount = float(input("Enter deposit amount: ₹"))
        balance += amount
        print(f"₹{amount} deposited successfully.")
        print(f"New balance: ₹{balance}")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= balance:
            balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            print(f"Remaining balance: ₹{balance}")
        else:
            print("Insufficient balance!")

    elif choice == "4":
        print("Thank you for using our ATM.")
        break

    else:
        print("Invalid choice! Please select 1-4.")
