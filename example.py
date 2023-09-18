
input_str = input("Enter two integers separated by a space: ")

input_list = input_str.split()
a = int(input_list[0])
b = int(input_list[1])
print("Result:", a - b)
