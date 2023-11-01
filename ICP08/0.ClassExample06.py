class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
    def enroll(self, num): # Course Number
        print(f'{self.name} has enrolled in the course {num}.')
s1 = Student('Lindung', 'IS')
s2 = Student('Dani', 'IT')

s1.enroll(10)
s2.enroll(20)

