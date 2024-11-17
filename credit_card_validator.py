sum_odd_digits = 0
sum_even_digits= 0
total = 0

#Step 1
card_number = input("Enter a credit card no.: ")
card_number = card_number.replace("-", "")  # Replace every instance of - with an empty string
card_number = card_number.replace(" ", "")  # Replace every instance of space with an empty string
card_number = card_number[::-1]  # Reverse the user input string by using indexing

#Step 2
for x in card_number[::2]:  # For every element in card no. string, add the digits in the odd places from right to left
    sum_odd_digits = sum_odd_digits + int(x)

# Step 3
for x in card_number[1::2]:  # Iterate over every sec digit, set step = 2, begin at second digit at index = 1
    x = int(x) * 2  # Doubling every sec digit
    if x >= 10:  # Check if x is a 2 digit no.
        sum_even_digits = sum_even_digits + (1 + (x % 10))  # Add the two-digit no. together to get a single digit
    else:
        sum_even_digits = sum_even_digits + x

# Step 4
total = sum_even_digits + sum_odd_digits  # Sum the totals of steps 2 & 3

# Step 5
if total % 10 == 0: # If sun is divisible by 10, credit card is valid
    print("VALID")
else:
    print("INVALID")