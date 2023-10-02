def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(1))
print(factorial(3))
print(factorial(5))


