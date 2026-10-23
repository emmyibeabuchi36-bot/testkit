# PROJECT 6: UNIT CONVERTER

# Conversion factors to metres
units = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
    "in": 0.0254,
    "ft": 0.3048,
    "mile": 1609.344
}

# Ask the user to enter the length
value = float(input("Enter the length value: "))

# Ask for the source unit
source = input(
    "Enter the source unit (mm, cm, m, km, in, ft, mile): "
).lower()

# Ask for the destination unit
destination = input(
    "Enter the destination unit (mm, cm, m, km, in, ft, mile): "
).lower()

# Check that the units are valid
if source not in units or destination not in units:
    print("Invalid unit. Please use one of: mm, cm, m, km, in, ft, mile")

else:
    # Convert the source value to metres
    value_in_metres = value * units[source]

    # Convert from metres to the destination unit
    converted_value = value_in_metres / units[destination]

    # Display the result
    print(
        f"{value} {source} = {converted_value:.2f} {destination}"
    )
