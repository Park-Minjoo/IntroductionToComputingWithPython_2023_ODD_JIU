x = int(input("Enter an integer: "))
if x > 100:
    print("Cannot process this number.")
elif x >= 80:
    print("Excellent grade.")
elif x >= 70:
    print("Average grade.")
elif x >= 60:
    print("Satisfactory grade.")
else:
    print("Needs improvement.")
