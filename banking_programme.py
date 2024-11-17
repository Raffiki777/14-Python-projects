def show_balance(balance):
    print(f"Your current balance is R{balance:.2f}")

    if balance < 100:
        print("You broke as hell! TF!")
        return 0
    elif balance > 10000:
        print(f"R{balance}, that's looking good!")
        return 0
    else:
        return balance

def deposit():
    amount = float(input("Enter an amount to deposit: "))

    if amount < 0:
        print("That is not a valid amount! What you tryna deposit ghost currency!")
        return 0
    else:
        print(f"Amount deposited: R{amount:.2f}")
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))

    if amount > balance:
        print(f"Tf you tryna withdraw! Balance is R{balance:.2f}!")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        print(f"Amount withdrawn: R{amount:.2f}")
        return amount

def main():
    balance = 0
    is_running = True  # Set boolean value to true

    while is_running:
        print()
        print("****STANDARD BANK*****")
        print()
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice(1 - 4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance = balance + deposit()
        elif choice == '3':
            balance = balance - withdraw(balance)
        elif choice == '4':
            is_running = False  # Reset boolean value to False to exit the loop
        else:
            print("Tf you tryna do! Enter a valid choice!")

    print("Thank you! Have a nice day!")

if __name__ == '__main__':  # To call the main function block of code
    main()