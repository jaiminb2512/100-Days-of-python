# Hybrid Inheritance
# Hybrid inheritance is a combination of multiple inheritance and single inheritance in object-oriented programming. It is a type of inheritance in which multiple inheritance is used to inherit the properties of multiple base classes into a single derived class, and single inheritance is used to inherit the properties of the derived class into a sub-derived class.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city

    def display_address(self):
        print(f"Address: {self.street}, {self.city}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_student_info(self):
        print(f"Student ID: {self.student_id}")

class UniversityStudent(Student, Address):
    def __init__(self, name, age, student_id, street, city):
        Student.__init__(self, name, age, student_id)
        Address.__init__(self, street, city)

    def display_university_student_info(self):
        self.display_info()  
        self.display_student_info()  
        self.display_address()  


student = UniversityStudent("Jaimin", 20, "12345", "314 gokuoldham", "Delh")

student.display_university_student_info()


#Hierarchical inharitance
print("\n\nExample of Hierarchical inheritance")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_student_info(self):
        self.display_info()
        print(f"Student ID: {self.student_id}")

class Faculty(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_Faculty_info(self):
        self.display_info()
        print(f"Faculty ID: {self.employee_id}")

student = Student("Jaimin", 20, "EC101")
faculty = Faculty("Mr. CH Vithalani", 55, "T9876")

student.display_student_info()
faculty.display_Faculty_info()
