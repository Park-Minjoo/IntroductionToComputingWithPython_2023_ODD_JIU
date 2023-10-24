user_id = 'hello'
user_pw = 'world'

id = input("Please enter the ID: ")
assert user_id == id, 'ID doesn\'t match'

pw = input("Please enter the password: ")
assert user_pw == pw, 'Password does\'t match'

print("Login successfully!")