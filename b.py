# Initial balance
balance = 1000
def display_menu():
    print("\nPlease choose an option:")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Exit")
def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print(f"Withdrawal successful! You withdrew {amount}. Remaining balance is {balance}.")
    return balance
def deposit(balance):
    amount = float(input("Enter the amount to deposit: "))
    balance += amount
    print(f"Deposit successful! You deposited {amount}. Now your current balance is {balance}.")
    return balance
def check_balance(balance):
    print(f"Your current balance is: {balance}")
def banking_system():
    global balance
    while True:
        display_menu()
        choice = input("Select an option (1-4): ")
        if choice == '1':
            balance = withdraw(balance)
        elif choice == '2':
            balance = deposit(balance)
        elif choice == '3':
            check_balance(balance)
        elif choice == '4':
            print("Exiting the banking system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
# Start the banking system
banking_system()