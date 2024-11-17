import random

lowest_num = 1
highest_num = 50
answer = random.randint(lowest_num, highest_num)  # Use randint to randomly choose no. between l & h
guesses = 0  # Keep track of number of guesses
is_running = True

print("***************NUMBER GUESSING GAME*******************")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Enter your guess (0 to quit): ")

    if guess == "0":
        print("Thanks for playing!")
        break

    if guess.isdigit():  # To insure input is a digit
        guess = int(guess)  # Type cast guess str into int
        guesses = guesses + 1  # Increment each guess by 1

        if guess < lowest_num or guess > highest_num:
            print(f"{guess} out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low, try again!")
        elif guess > answer:
            print("Too high, try again!")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False

    else:
        print(f"Invalid guess! {guess} is not a valid number!")
        print(f"Please select a number between {lowest_num} and {highest_num}")