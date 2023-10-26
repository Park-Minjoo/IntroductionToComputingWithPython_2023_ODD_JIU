inf = open('num.txt', 'r')
sm = inf.readlines()
print("All data = ", sm)

for i in range(len(sm)) :
    s = sm[i].split(",") ## “,” important
    print(s)
    sum = 0
    for j in range(len(s)) :
        sum = sum + int(s[j])
    print("Average = ", sum/len(s))
    print()
inf.close()