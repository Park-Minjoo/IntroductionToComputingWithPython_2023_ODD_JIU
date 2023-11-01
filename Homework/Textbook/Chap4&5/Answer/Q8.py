# Q8
def mystery(n):
    numtimes = 0
    while n > 1:
        n = n // 2
        numtimes += 1
    return numtimes

print(mystery(4))
print(mystery(11))
print(mystery(25))