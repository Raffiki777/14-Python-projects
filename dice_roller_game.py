import random

# ● ┌ ─ ┐ │ └ ┘  # Dice ascci art

dice_art = {
    1: ("┌─────────┐", 
        "│         │", 
        "│    ●    │", 
        "│         │", 
        "└─────────┘"),
    2: ("┌─────────┐", 
        "│ ●       │", 
        "│         │", 
        "│       ● │", 
        "└─────────┘"),
    3: ("┌─────────┐", 
        "│ ●       │", 
        "│    ●    │", 
        "│       ● │", 
        "└─────────┘"),
    4: ("┌─────────┐", 
        "│ ●     ● │", 
        "│         │", 
        "│ ●     ● │", 
        "└─────────┘"),
    5: ("┌─────────┐", 
        "│ ●     ● │", 
        "│    ●    │", 
        "│ ●     ● │", 
        "└─────────┘"),
    6: ("┌─────────┐", 
        "│ ●     ● │", 
        "│ ●     ● │", 
        "│ ●     ● │", 
        "└─────────┘")
    }  # Dictionary containing tuples made of strings as values and intergers as keys

dice = [] # List of dice
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):  # Iterate over dice elements within the range of the num of dice chosen by player
    dice.append(random.randint(1, 6))  # Append a random number between 1 & 6 into dice list

   # Simple loop for printing horizontally
#for die in range(num_of_dice):
    #for line in dice_art.get(dice[die]):
        #print(line)

   # Complex loop for printing vertically
for line in range(5):  # Iterate over the tuple elements 5 times
    for die in dice:
        print(dice_art.get(die)[line], end=" ")
    print()

for die in dice:
    total = total + die
print(f"Total dice rolled: {total}")