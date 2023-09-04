# Input the current temperature in Celsius
temperature_celsius = float(input("Enter the current temperature in Celsius: "))

# Check the temperature range and print a message
if temperature_celsius >= 35:
    print("It's very hot.")
elif 28 <= temperature_celsius < 35:
    print("It's hot.")
elif 15 <= temperature_celsius < 28:
    print("It's warm.")
elif 5 <= temperature_celsius < 15:
    print("It's pleasant.")
else:
    print("It's chilly.")
