import sys

while True:
    try:
        x = int(input("Please enter an integer: "))
        break

    except ValueError:
        print("Oops! That was no valid number. Try again...")

print("Finish checking errors")