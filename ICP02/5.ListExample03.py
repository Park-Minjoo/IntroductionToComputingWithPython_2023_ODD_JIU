birthday = '9/6/2007'
print(birthday.split('/'))
# ['9', '6', '2007']

splitme = 'a/b//c/d///e'
print(splitme.split('/'))
# ['a', 'b', '', 'c', 'd', '', '', 'e']

splitme = 'a/b//c/d///e'
print(splitme.split('//'))
# ['a/b', 'c/d', '/e']

