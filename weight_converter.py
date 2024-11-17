
weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds?(Kg or lbs): ").lower()

if unit == 'kg':
    weight = float(weight)
    weight = weight * 2.205
    unit = "lbs"
elif unit == 'lbs':
    weight = float(weight)
    weight = weight / 2.205
    unit = "Kgs"
else:
    print(f"{unit} was not valid! (Kg or lbs)")

print(f"Your weight is: {weight:.1f} {unit}.")