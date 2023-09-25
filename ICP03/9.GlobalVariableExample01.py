a = 0
def fun(count):  # count: local scope
    global a
    a = 5        # global a is changed
    count += a
    return count

count = 0        # count: global scope
print("result :", fun(count)) # 5

print(a)         # count: global scope 5