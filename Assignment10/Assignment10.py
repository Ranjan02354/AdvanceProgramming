class Address:

    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code

    def display(self):
        return f"{self.street}, {self.city} - {self.zip_code}"


class Student:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address  # Composition
        self.courses = []

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer.")

        if value <= 0:
            raise ValueError("Age must be positive.")

        if value > 100:
            raise ValueError("Age must be less than or equal to 100.")

        self._age = value

    # Demonstrates mutable list behavior
    def add_course(self, course_name):
        self.courses.append(course_name)

    def display(self):
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Address : {self.address.display()}")

        if self.courses:
            print(f"Courses : {', '.join(self.courses)}")
        else:
            print("Courses : None")

        print()


class ScholarshipStudent(Student):

    def __init__(self, name, age, address, scholarship_amount):
        super().__init__(name, age, address)
        self.scholarship_amount = scholarship_amount

    def display(self):
        super().display()
        print(f"Scholarship : Rs. {self.scholarship_amount}")
        print()


address1 = Address("12 MG Road", "Mumbai", "400001")
address2 = Address("5 Nehru Street", "Delhi", "110011")

student1 = Student("Arjun Sharma", 20, address1)

student1.add_course("Data Structures")
student1.add_course("Operating Systems")
student1.add_course("DBMS")

print("Student Details:")
student1.display()

student2 = ScholarshipStudent(
    "Priya Patel",
    21,
    address2,
    75000
)

student2.add_course("Computer Networks")
student2.add_course("Machine Learning")

print("Scholarship Student Details:")
student2.display()

print("Mutable Behavior Demonstration:")
student1.add_course("Computer Graphics")
student1.display()

print("Age Validation:")

try:
    student1.age = -5
except ValueError as e:
    print(e)

try:
    student1.age = 200
except ValueError as e:
    print(e)