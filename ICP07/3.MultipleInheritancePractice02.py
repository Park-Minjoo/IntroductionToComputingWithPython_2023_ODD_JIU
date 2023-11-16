class Person:
    def __init__(self, name):
        self.name = name

class ITStudent(Person):
    def __init__(self, name, IT_grade):
        super().__init__(name)
        self.IT_grade = IT_grade
class ISStudent(Person):
    def __init__(self, name, IS_grade):
        super().__init__(name)
        self.IS_grade = IS_grade
IT1 = ITStudent('Zezen', 100)
IS1 = ISStudent("Firman", 50)

print(IT1.name, IT1.IT_grade)
print(IS1.name, IS1.IS_grade)
