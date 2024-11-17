def calculator():
    operator = input("Enter an opeartor(+ - * /): ")
    first_num = float(input('Enter a number: '))
    second_num = float(input("Enter a second number: "))

    try:
        if operator == "+":
            result = first_num + second_num
            print(round(result))
        elif operator == "-":
            result = first_num - second_num
            print(round(result))
        elif operator == "*":
            result = first_num  * second_num
            print(round(result))
        elif operator == "/":
            result = first_num / second_num
            print(round(result))
        else:
            print(f"{operator} is not a valid operator!")
    except ZeroDivisionError:
        print(f"You cannot divide by zero!")

calculator()