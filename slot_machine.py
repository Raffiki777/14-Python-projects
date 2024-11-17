import random
import time

def spin_row():
    symbols = ['#', '$','%', '@']  # List of symbols

    results = []
    for symbol in range(3):  # Iterate 3 times
        results.append(random.choice(symbols))  # Append random choice from list of symbols into list of results
    return results
# OR Use list comprehension
    #return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("-".join(row))  # Use the join meth to join iterable row list items by a space

def get_payout(row, bet):
    if row[0] == row[1] == row[2]: # Use indexing to check each element at each index
        if row[0] == '#':  # If element at given index is equal to given symbol
            return bet * 3
        elif row[0] == '%':
            return bet * 4
        elif row[0] == '@':
            return bet * 5
        elif row[0] == '$':
            return bet * 10
    return 0

def main():
    balance = 100

    print("******Ka-Ching Slot Machine!******\n")
    time.sleep(3)
    print("Symbols: # $ % @")

    while balance > 0:
        print(f"Current balance: R{balance:.2f}")

        bet = input("Enter amount to bet: ")

        if not bet.isdigit():
            print("Please enter a valid amount")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds!")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance = balance - bet

        row = spin_row()
        print("Spinning...\n")
        time.sleep(3)
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won R{payout:.2f}!")
        else:
            print("Toche! You lost this round!")

        balance = balance + payout

        play_again = input("Do you wish to spin again? (Y/N): ").upper()

        if play_again != 'Y':
            break
    print("*************GAME OVER!**************")
    time.sleep(3)
    print("*************************************")
    print(f"Your final balance is R{balance:.2f}")
    print("*************************************")

if __name__ == '__main__':
    main()