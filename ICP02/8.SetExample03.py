dubi = {1,2,3,4,5}
duba = {4,5,6,7,8}
dubu = {1,4}

print(dubi <= dubi) # True
print(dubi.issubset(dubi)) # True

print(dubi < dubi) # False

print(dubi >= dubu) # True
print(dubi.issuperset(dubu)) # True

print(dubi > dubu) # True

