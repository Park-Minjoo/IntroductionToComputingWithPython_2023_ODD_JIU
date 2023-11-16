class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
    def enroll(self):
        print(f'{self.name} has enrolled in the course')
s3 = Student('Nicholas', 'IT')
s3.enroll()