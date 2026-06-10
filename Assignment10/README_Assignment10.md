# Assignment 10 – Student Management System using Python OOP

## Question

Design a student system in Python with:

### Address Class

* street
* city
* zipCode

### Student Class

* name
* age
* Address
* course list

Requirements:

* Store age as a protected attribute and control it using `@property`
* Implement:

  * `add_course()`
  * `display()`

### Extend it with:

#### ScholarshipStudent

* Add `scholarshipAmount`
* Override `display()`

### Your implementation should clearly show:

* Composition (Student HAS-A Address)
* Proper data validation using `@property` (age must be valid)
* Inheritance and overriding (`super()` in display)
* Understanding of mutable behavior (course list updates persist)

---

## Objective

The objective of this assignment is to design a Student Management System using Object-Oriented Programming concepts in Python. The system demonstrates composition, inheritance, property-based validation, method overriding, and mutable object behavior.

---

## Concepts Used

* Classes and Objects
* Composition
* Inheritance
* Method Overriding
* super()
* Encapsulation using @property
* Data Validation
* Mutable Data Structures
* Exception Handling

---

## Files Included

* Assignment10.py

---

## Class Structure

### Address Class

Stores address details of a student.

Attributes:

```text
street
city
zip_code
```

Methods:

```python
display()
```

Returns a formatted address string.

---

### Student Class

Stores student information.

Attributes:

```text
name
_age (protected)
address
courses
```

Methods:

```python
add_course()
display()
```

Features:

* Uses Composition (Student HAS-A Address)
* Uses @property for age validation
* Stores courses in a mutable list

---

### ScholarshipStudent Class

Derived from Student.

Additional Attribute:

```text
scholarship_amount
```

Features:

* Inherits Student
* Uses super()
* Overrides display()

---

## Features

### Student Management

* Create student records
* Store address information
* Add courses dynamically
* Display complete student details

### Scholarship Support

* Create scholarship students
* Display scholarship amount

### Age Validation

* Reject non-integer ages
* Reject negative ages
* Reject unrealistic ages (>100)

### Mutable Behavior Demonstration

* Courses can be added after object creation
* Updates persist throughout the program

---

## How to Run

```bash
python Assignment10.py
```

---

## Sample Output

```text
Student Details:

Name    : Arjun Sharma
Age     : 20
Address : 12 MG Road, Mumbai - 400001
Courses : Data Structures, Operating Systems, DBMS

Scholarship Student Details:

Name    : Priya Patel
Age     : 21
Address : 5 Nehru Street, Delhi - 110011
Courses : Computer Networks, Machine Learning

Scholarship : Rs. 75000

Mutable Behavior Demonstration:

Courses : Data Structures, Operating Systems,
DBMS, Computer Graphics

Age Validation:

Age must be positive.
Age must be less than or equal to 100.
```

---

## Algorithm

### Creating a Student

1. Create an Address object.
2. Create a Student object.
3. Validate age through @property.
4. Store address using composition.

### Adding Courses

1. Accept course name.
2. Append course to course list.
3. Updated list persists because lists are mutable.

### Scholarship Student

1. Inherit from Student.
2. Add scholarship amount.
3. Override display().
4. Use super() to display parent details.

### Age Validation

1. Check if age is an integer.
2. Ensure age is greater than zero.
3. Ensure age does not exceed 100.
4. Raise appropriate exceptions if validation fails.

---

## OOP Features Demonstrated

### Composition

```python
self.address = address
```

A Student object contains an Address object.

Relationship:

```text
Student HAS-A Address
```

---

### Encapsulation using @property

```python
@property
def age(self):
```

Provides controlled access to age.

---

### Inheritance

```python
class ScholarshipStudent(Student):
```

ScholarshipStudent inherits all Student functionality.

---

### Method Overriding

```python
def display(self):
```

Overrides parent display() method.

---

### super()

```python
super().display()
```

Reuses parent functionality before adding scholarship details.

---

### Mutable Behavior

```python
self.courses.append(course_name)
```

Changes made to the course list remain available throughout the object's lifetime.

---

## Time Complexity

| Operation       | Complexity |
| --------------- | ---------- |
| Add Course      | O(1)       |
| Display Student | O(n)       |
| Age Validation  | O(1)       |
| Create Student  | O(1)       |

where **n** is the number of courses.


## Author

Ranjan Malakar
B.Tech Computer Science & Engineering
Tezpur University
