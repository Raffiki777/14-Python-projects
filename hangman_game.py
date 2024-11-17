import random
import time

words = ("apple", "orange", "banana", "coconut", "mango") # Tuple of words

# Dict of key: () # Each key corresponds to the no. of incorrect guesses  # Each value tuple corresponds to the no. of key incorrect guesses
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}  # Tuple value containing 3 strings

print()
print("WELCOME TO HANGMAN!\n")
print("Guess the name of fruit hidden in the game!\n")
def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))  # For each char in hint, join it by an empty space " "

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)  # Randomly choose element in the tuple of words
    hint = ["_"] * len(answer) # No. of _ must be equal to no. of chars in the word in words tuple chosen at random
    wrong_guesses = 0
    guessed_letters = set({})  # Set of letters
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) > 1 or not guess.isalpha():  # Not more than 1 letter and no numbers
            print("Invalid input! Enter a letter!")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed!")
            continue

        guessed_letters.add(guess)  # Add the already guessed guess into set

        if guess in answer:
            for index in range(len(answer)):
                if answer[index] == guess:
                    hint[index] = guess
        else:
            wrong_guesses = wrong_guesses + 1  # Increment wrong guesses by 1 to move along the dict

        if "_" not in hint:  # _ spaces all guessed
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False  # To break out of the while loop
        elif wrong_guesses >= len(hangman_art) - 1: # No. of wrong guesses equal to length of dic keys, minus 1 to equal 6
            print("******HANGMAN!*******")
            display_man(wrong_guesses)
            print(f"The answer was:")
            display_answer(answer)
            time.sleep(3)
            print("YOU LOSE!")
            is_running = False

if __name__ == '__main__':
    main()