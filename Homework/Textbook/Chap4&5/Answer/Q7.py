# Q7
def fib(n):
    first = 0
    second = 1
    third = 1
    for i in range(n):
        third = first + second
        first, second = second, third
    return second

print(fib(0))
print(fib(4))
print(fib(8))