fruit = 'banana'
count = 0

for char in fruit:
    if char == 'a':
        count += 1
    elif char == 'n':
        break
    else:
        print(char)
print(count)