# Q5
def pay(wage, hours):
    pay = 0
    for i in range(1, hours + 1):
        if i <= 40:
            pay += wage
        elif i > 40 and i <= 60:
            pay += wage * 1.5
        elif i > 60:
            pay += wage * 2
    return pay

print(pay(10, 35))
print(pay(10, 45))
print(pay(10, 61))