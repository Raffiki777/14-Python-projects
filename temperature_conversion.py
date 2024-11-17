
def convert_celcius(temp, unit):
        temp = (round((9 * temp) / 5 + 32, 1))
        print(f"The temperature in Fahreinheit is: {temp} F")
        return temp, unit

def convert_fahreinheit(temp, unit):
        temp = round((temp - 32) * 5 / 9)
        print(f"The temperature in Celcius is: {temp} C")
        return temp, unit

def main():
    while True:
        unit = input("Is this temperature in Celcius or Fahrenheit (C/F)?: ").upper()
        temp = input("Enter the temperature: ")

        if temp.isalpha():
            print("Invalid")
            break

        elif temp.isdigit():
            temp = int(temp)
            convert_celcius(temp, unit)
            convert_fahreinheit(temp, unit)
            break

        elif unit == 'C':
            convert_celcius(temp, unit)
        elif unit == 'F':
            convert_fahreinheit(temp, unit)
        else:
            print(f"'{unit}' is an invalid unit of measurement")
        break
   
if __name__ == '__main__':
    main()