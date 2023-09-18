'''Let alist = [’a’, ’b’, ’c’, ’d’, ’e’, ’f’].

Find the output using the list index: [?:?]
1. [’b’, ’c’]
2. [’a’, ’b’, ’c’, ’d’]
3. [’d’, ’e’, ’f’]
4. Remove ‘b’ using list method.
5. Add ‘z’ in index 2 using list method.
6. Pop the element in the list.
7. Sort the list using list method.
'''

alist = ['a', 'b', 'c', 'd', 'e', 'f']

print("1)", alist[1:3])
print("2)", alist[:4])
print("3)", alist[3:])
alist.remove('b')
print("4)", alist)
alist.insert(2,'z')
print("5)", alist)
alist.pop()
print("6)", alist)
alist.sort()
print("7)", alist)