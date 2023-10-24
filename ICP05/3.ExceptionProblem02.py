import sys

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Division by Zero!")
    else:
        print("Result is", result)

divide(9,0)