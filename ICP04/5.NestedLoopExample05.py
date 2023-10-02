a = 0

for i in range(2, 10):
    a = a + i
    # print('a:', a, 'i:', i)
    for j in range(10, 1, -2):
        a = a + j
        # print('a:', a, 'j:', j)

print(a)

