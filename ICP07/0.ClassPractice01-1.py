class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f'Hello, {self.name}! You are {self.age} years old!')
    def is_adult(self):
        if int(self.age) > 18:
            return True
        else:
            return False

p1 = Person('Grace', '19')
p2 = Person('Jessica', '18')
p1.greet()
p2.greet()
print(p1.is_adult())
print(p2.is_adult())
