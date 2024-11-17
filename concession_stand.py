def concession_stand():
    menu = {"pizza": 48.00,
            "cheeseballs": 37.00,
            "popcorn": 87.50,
            "chips": 35.00,
            "pretzel": 60.50,
            "cooldrink": 25.00,
            "juice": 15.50}  # Dict for menu

    cart = []  # List to append chosen food into
    total = 0

    print("__________MENU__________")

    for key, value in menu.items():  # Iterate over dictionary items
        print(f"{key:12}: R{value:.2f}")

    print("__________________________________________")

    while True:  # While True boolean
        food = input("Select an item from the menu (q to quit): ").lower()
        if food == "q":
            break  # break out of the loop
        elif menu.get(food):  # Get food item key associated value in dict menu 
            cart.append(food)  # Append the food item into cart list
        else:
            print(f"{food.capitalize()} is not on the menu, please select items on the menu!")
    print()
    print("Your item(s) are:")

    for food in cart:  # For every food item in cart list
        total = total + menu.get(food)  # Add the food item price in the menu dict into the total
        print(food.capitalize(), end=" ")

    print()
    print(f"Your total is: R{total:.2f}")

concession_stand()