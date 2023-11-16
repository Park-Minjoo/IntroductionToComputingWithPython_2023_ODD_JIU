class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f'Hello, {self.name}! You are {self.age} years old!')

p1 = Person('Grace', '18')
p2 = Person('Jessica', '18')
p1.greet()
p2.greet()
