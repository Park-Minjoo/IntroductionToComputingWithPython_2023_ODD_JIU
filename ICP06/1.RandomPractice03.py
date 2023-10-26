import random
def dice():
    d = random.randrange(1, 7)
    return d

n1 = dice()
n2 = dice()
print(n1, n2)

while n1 != n2:
    n1 = dice()
    n2 = dice()
    print(n1, n2)