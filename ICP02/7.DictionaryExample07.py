animal = {'a':'ant', 'b' :'lion', 'c':'tiger'}
animal1 = {'g':'squirrel', 'd':'snake', 'f':'dog'}
animal.update(animal1)
print(animal)
# {'a': 'ant', 'b': 'lion', 'c': 'tiger', 'g': 'squirrel', 'd': 'snake', 'f': 'dog’}

t = [('a', 0), ('c', 2), ('b', 1)]
result = dict(t)
print(result) # {'a': 0, 'c': 2, 'b': 1}

