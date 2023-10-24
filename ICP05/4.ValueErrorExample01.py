import sys

while True:
    try:
        x = int(input("Please Enter an integer: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")