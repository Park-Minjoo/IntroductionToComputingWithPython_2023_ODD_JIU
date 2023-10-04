t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 7]]

for row in t:
    print(row)

def print2D(t):
    for row in t:
        for item in row:
            print(item, end=' ')
        print()

print2D(t)

