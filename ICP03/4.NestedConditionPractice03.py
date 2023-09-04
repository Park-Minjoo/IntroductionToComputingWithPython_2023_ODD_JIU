# Input the body temperature
body_temperature = float(input("Enter your body temperature in Celsius: "))

# Check the body temperature range and print a message
if body_temperature >= 37.5:
    print("High fever.")
elif 35.5 <= body_temperature < 37.5:
    print("Normal temperature.")
elif body_temperature < 35.5:
    if body_temperature >= 34:
        print("Low temperature.")
    else:
        print("Very low temperature.")
