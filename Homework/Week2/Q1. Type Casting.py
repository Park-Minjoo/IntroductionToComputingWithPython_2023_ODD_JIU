'''
x = 1, y = '3', z = '4.45346'

1) Make x, y, z to integer

2) Make x, y, z to float

3) Make x, y, z to string
'''
x = 1
y = '3'
z = '4.45346'

# 1)
# Write your code here
int_x = x
int_y = int(y)
int_z = int(float(z))

print("== 1) The type of x, y, z ==")
print(int_x, int_y, int_z)
print(type(int_x))
print(type(int_y))
print(type(int_z))
print()


# 2)
# Write your code here
float_x = float(x)
float_y = float(y)
float_z = float(z)
print("== 2) The type of x, y, z ==")
print(float_x, float_y, float_z)
print(type(float_x))
print(type(float_y))
print(type(float_z))
print()

# 3)
# Write your code here
string_x = str(x)
string_y = y
string_z = z
print("== 3) The type of x, y, z ==")
print(string_x, string_y, string_z)
print(type(string_x))
print(type(string_y))
print(type(string_z))
