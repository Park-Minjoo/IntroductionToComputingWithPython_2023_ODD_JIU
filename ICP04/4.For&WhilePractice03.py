str = input("Enter the string: ")
count = 0

for ch in str:
    if ch in "AEIOUaeiou":
        count+=1

print("The number of vowels:", count)