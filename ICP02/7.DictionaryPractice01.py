birthdate = {}


def add_birth(num):
    for i in range(num):
        input_name = input("Name: ")
        input_birth = int(input("Birthday: "))
        birthdate[input_name] = input_birth


add_birth(5)
print(birthdate)
