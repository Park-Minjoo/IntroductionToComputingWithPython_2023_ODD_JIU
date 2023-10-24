import sys

while True:
    try:
        x = int(input("Please enter an integer: "))
        y = x / (x - x)
        break
    except ZeroDivisionError as err:
        print("Handling run-time error:", err)
print("Finish checking errors")