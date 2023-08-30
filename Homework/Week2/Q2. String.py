'''
string1 = LetUsTransformTheWorld
string2 = jakarta international university

1) Reverse the string1 using index slicing.

2) Make string1 as 'Unmo' using index slicing.

3) Print the length of string1, string2

4) Make string2 as 'Jakarta International University' using string methods.

5) Make string2 as capital letters.

6) Replace the word 'jakarta' to 'The best jakarta' in string2.

'''
string1 = 'LetUsTransformTheWorld'
string2 = 'jakarta international university'

# 1)
# Write your code here
print("1) ", string1[-1::-1])
# 2)
# Write your code here
print("2) ",string1[3::5])
# 3)
# Write your code here
print("3) Length of string1 :", len(string1), ", Length of string2: ", len(string2))
# 4)
# Write your code here
print("4) ",string2.title())
# 5)
# Write your code here
print("5) ",string2.upper())
# 6)
# Write your code here
print("6) ", string2.replace("jakarta", "The best jakarta"))