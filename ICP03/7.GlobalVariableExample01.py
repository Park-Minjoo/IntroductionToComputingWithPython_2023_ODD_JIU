def fun(count):  # count: local scope
    global a
    a = 5        # global a is changed
    count += a
    return count

count = 0        # count: global scope
print("result :", fun(count))

print(a)         # count: global scope