class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

s1 = Student('Lindung', 'IS')
print(s1.name, s1.major)
s2 = Student('Dani', 'IT')
print(s2.name, s2.major)