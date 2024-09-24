name = input("Enter your Name:")
balance = 1000 #initial balance
# Function to display the menu and handle transactions
print(f"\nHello{name} Please select your desired option:") #f to add variables, comma separators, do padding with zeros and date format
print("1. Withdraw")
print("2. Deposit")
print("3. Check Balance")
        # Getting the user's option
opt=int(input("Enter your desired option: (1-3)"))
if opt==1:
    amount=int(input("Enter your withdrawal amount: "))
    if amount>balance:
     print("insufficient balance! Your current balance is: ", amount)
    else:
      print("Your with-drawl amount is: ", amount)
      amount=balance-amount
      print("Your remaining balance is: ", amount)
elif opt==2:
        amount=int(input("Enter your deposit amount: "))
        print("Your deposit amount is:", amount)
        amount=balance+amount
        print("Your remaining balance is:", amount)
elif opt==3:
      print("Your balance is:", balance)
else:
       print("Invalid option: try again later")