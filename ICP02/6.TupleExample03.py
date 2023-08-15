my_tuple = (11, 3, 15, 7, 9)
my_list = list(my_tuple)
print(my_list) # [ 11, 3, 15, 7, 9 ]

my_list.sort()
print(my_list) # [ 3, 7, 9, 11, 15 ]

sorted_tuple = tuple(my_list)
print(sorted_tuple) # (3, 7, 9, 11, 15)

