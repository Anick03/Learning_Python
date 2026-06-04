print("\n===== SIMPLE BANKING SYSTEM =====")
account_name = input("Enter the Account Holder Name: ")
pin = input("Set a 4-digit PIN: ")
balance = 0
access_granted = False

#PIN Verification
for _ in range(5):
    entered_pin = input("Enter your PIN: ")
    if entered_pin == pin:
        print("Access Granted!")
        access_granted = True
        break
    else:
        print("Incorrect PIN. Try again.")

if not access_granted:
    print("Too many incorrect attempts. Access Denied.")

while access_granted == True:
    print(f"\nWelcome, {account_name}!\n")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    #Choosing Section
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        print(f"Current Balance: Rs.{balance}")
    elif choice == "2":
        amount = float(input("Enter the amount to deposit: Rs."))
        if amount > 0:
            balance += amount
            print(f"Deposit Successful!")
            print(f"New Balance: Rs. {balance}")
        else:
            print("Invalid amount!")
    elif choice == "3":
        amount = float(input("Enter the amount to withdraw: Rs."))
        if amount <= 0:
            print("Invalid amount.")
        elif amount > balance:
            print("Insufficient Balance!")
        else:
            balance -= amount
            print("Withdrawal Successful!")
            print(f"Remaining Balance: Rs. {balance}")
    elif choice == "4":
        print("Thank you for using the Banking System.")
        break
    else:
        print("Please enter a number between 1 and 4.")