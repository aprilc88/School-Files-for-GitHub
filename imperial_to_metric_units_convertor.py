'''
This program demonstrates the conversion of the user inputted values and prints
the converted values with the appropriate unit.
Author: April Carchedi

The following questions are asked:

Enter Fahrenheit to be converted to Celsius and Kelvin:
Enter Pounds to be converted to Kilograms and Grams:
Enter Miles to be converted to Kilometers and Meters:
Enter Gallons to be converted to Liters and Milliliter:
'''

print("This program converts imperial units to metric units.\n")

# Temperature Fahrenheit to Celsius and Kelvin.
temp_fahren = eval(input("Enter Fahrenheit to be converted to Celsius and Kelvin: "))
temp_cels = (temp_fahren - 32) * (5 / 9)
temp_kelv = temp_cels + 273.15

# Mass Pounds to Kilograms and Grams.
mass_pounds = eval(input("Enter Pounds to be converted to Kilograms and Grams: "))
mass_kgrams = mass_pounds / 2.205
mass_grams = mass_pounds * 453.592

# Distance Miles to Kilometers and Meters.
distance_miles = eval(input("Enter Miles to be converted to Kilometers and Meters: "))
distance_kmeters = distance_miles * 1.609
distance_meters = distance_miles * 1609.344

# Volume Gallons to Liters and Milliliter. 
volume_gallons = eval(input("Enter Gallons to be converted to Liters and Milliliter: "))
volume_liters = volume_gallons * 3.785
volume_mliters = volume_gallons * 3785.412

# Formatted output of converted units.
print("\nConverting imperial to metric units...\n")
print("Fahrenheit conversions loaded.")
print("User entered ", temp_fahren, "F.\n")

print("Celsius conversion: %.4f" % temp_cels, "C")
print("Kelvin conversion: %.4f" % temp_kelv, "K\n") 

print("Pound conversions loaded.")
print("User entered ", mass_pounds, "lbs.\n")

print("Kilograms conversion: %.4f" % mass_kgrams, "kg")
print("Grams conversion: %.4f" % mass_grams, "g\n")

print("Miles conversions loaded.")
print("User entered ", distance_miles, "mi.\n")

print("Kilometers conversion: %.4f" % distance_kmeters, "km")
print("Meters conversion: %.4f" % distance_meters, "m\n")

print("Gallon conversions loaded.")
print("User entered ", volume_gallons, "gal.\n")

print("Liter conversion: %.4f" % volume_liters, "L")
print("Milliliter conversion: %.4f" % volume_mliters, "mL\n")

