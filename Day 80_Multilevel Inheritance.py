# Multilevel inharitance
# In multilevel inharitance we making a child class from another child class
# The multilevel inharitance class have all the atributes of child class and parent class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_student_info(self):
        self.display_info()
        print(f"Student ID: {self.student_id}")


class CollegeStudent(Student):
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age, student_id)
        self.major = major

    def display_college_student_info(self):
        self.display_student_info()
        print(f"Major: {self.major}")


college_student = CollegeStudent("Jaimin", 20, "EC101", "EC")

college_student.display_college_student_info()
