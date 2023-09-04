# Define a list of valid usernames
user = ['Nicho', 'David', 'Jonatan']

# Prompt the user for their username
user_id = input("Username: ")

# Check if the entered username is in the list of valid usernames
if user_id in user:
    # If the username is valid, prompt the user for their password
    pw = input("Password: ")

    # Check if the entered password is correct
    if pw == '1234':
        print("Login successful.")
    else:
        print("Incorrect password.")
else:
    print("Invalid user.")
