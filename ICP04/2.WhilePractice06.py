num = 0
count = 0
sum = 0

while num <= 10000:
    num = float(input("Enter the price: "))
    if num <= 10000 :
        sum += num
        count += 1

print("The total price of", count, "items are", sum, "Rupiah")