dubi = {1,2,3,4,5}
duba = {4,5,6,7,8}
dubu = {1,4}

print(dubi & duba) # {4, 5}
print(dubi.intersection(duba)) # {4, 5}
print(dubi & duba & dubu) # {4}

print(dubi | duba) # {1, 2, 3, 4, 5, 6, 7, 8}
print(dubi.union(duba)) # {1, 2, 3, 4, 5, 6, 7, 8}
print(dubi | duba | dubu) # {1, 2, 3, 4, 5, 6, 7, 8}

print(dubi - duba) # {1, 2, 3}
print(dubi.difference(duba)) # {1, 2, 3}

print(dubi ^ dubu) # {2, 3, 5}
print(dubi.symmetric_difference(dubu)) # {2, 3, 5}
