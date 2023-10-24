# Zero Division
import sys
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Division by Zero!")
    else:
        print("Result is", result)
    finally:
        print("Executing Finally Clause")

divide(2, 1)
divide(3, 0)