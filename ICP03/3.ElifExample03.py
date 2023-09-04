fruits = ['apple', 'banana', 'grape', 'mango', 'durian']
fruit_input = input("Enter your favorite fruit: ")

if fruit_input not in fruits:
    print("The fruit is not in the list.")
elif fruit_input == "durian":
    print("You are durian-lover!")
else:
    print("Try durian; you're sure to like it.")
