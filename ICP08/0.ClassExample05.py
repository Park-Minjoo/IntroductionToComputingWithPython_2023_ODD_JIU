class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
    def enroll(self, num): # Course Number
        print(f'{self.name} has enrolled in the course {num}.')
s3 = Student('Nicholas', 'IT')
s3.enroll(100)
