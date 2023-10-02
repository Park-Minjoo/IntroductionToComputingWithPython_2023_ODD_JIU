def nested2(n):
    for j in range(n):
        for i in range(j+1):
            print(i, end= ' ')
        print()

nested2(9)

