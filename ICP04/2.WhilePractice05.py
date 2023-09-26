numofnum = 0
count = 1
sum = 0

while numofnum <= 0:
    numofnum = int(input("How many values to enter?: "))

while count <= numofnum:
    num = float(input("Enter the number: "))
    count += 1
    sum += num

print("The average of the input values are =", sum / numofnum)