mul = [10 * [0] for i in range(15)]
# print(mul)

for i in range(15):
    for j in range(10):
        mul[i][j] = (i+2) * (j+1)
    print(mul[i])
print("Done!")
