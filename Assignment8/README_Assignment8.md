# Assignment 8 – Course Enrollment Dashboard in ReactJS

## Question

Develop a course enrollment dashboard in ReactJS.

You are building a React component that displays enrolled students.

Each student:

```javascript
{
  id: number,
  name: string,
  enrolledCourses: Set<string>,
  gpa: number
}
```

### Requirements

#### 1. Maintain students in state.

#### 2. Implement the following features:

* Add new student
* Remove student by ID
* Display students sorted by GPA (descending)
* Display all unique courses across students
* Filter students enrolled in a specific course

#### 3. Use the following:

* useState
* Map internally for ID-to-student mapping
* Set for course uniqueness
* map(), filter(), and reduce()
* Do not mutate state directly
* Use spread operator for updates
* Convert Set to Array before rendering

#### 4. Compute time complexity of filtering students by course.

---

## Objective

The objective of this assignment is to develop a dynamic Course Enrollment Dashboard using ReactJS. The application manages student records, course enrollments, GPA-based sorting, course filtering, and unique course extraction while demonstrating React state management and modern JavaScript collection types.

---

## Concepts Used

* ReactJS Functional Components
* useState Hook
* Map Data Structure
* Set Data Structure
* Array Methods

  * map()
  * filter()
  * reduce()
* State Management
* Dynamic Rendering
* Immutable Updates
* Event Handling

---

## Files Included

* Assignment8.jsx

---

## Features

### Student Management

* Add new students
* Remove students using Student ID
* Store students using a Map

### GPA-Based Sorting

* Automatically sorts students in descending GPA order

### Course Filtering

* Filter students enrolled in a specific course

### Unique Course Extraction

* Displays all unique courses across enrolled students

### Dynamic UI Updates

* Reactively updates UI whenever state changes

---

## How to Run

### Install Dependencies

```bash
npm install
```

### Start Development Server

```bash
npm run dev
```

or

```bash
npm start
```

(depending on project configuration)

---

## Sample Workflow

### Add Student

```text
Name: Ranjan
GPA: 9.1
Courses: DSA, DBMS, OS
```

### Add Another Student

```text
Name: Rahul
GPA: 8.5
Courses: DBMS, CN
```

### Display

```text
Students Sorted by GPA

Ranjan - GPA 9.1
Rahul  - GPA 8.5

Unique Courses:
DSA
DBMS
OS
CN
```

---

## Algorithm

### Adding a Student

1. Read user input.
2. Create a Set from course input.
3. Create a student object.
4. Clone existing Map.
5. Insert student into Map.
6. Update state.

### Removing a Student

1. Clone existing Map.
2. Remove selected student.
3. Update state.

### GPA Sorting

1. Convert Map values into an array.
2. Sort using GPA comparator.
3. Display sorted array.

### Course Filtering

1. Check selected course.
2. Filter students whose enrolledCourses Set contains the course.
3. Display filtered results.

### Unique Course Extraction

1. Traverse all students.
2. Use reduce() to accumulate courses into a Set.
3. Convert Set to Array before rendering.

---

## Time Complexity Analysis

### Filtering Students by Course

Let:

* n = number of students

For each student:

```text
student.enrolledCourses.has(course)
```

takes approximately:

```text
O(1)
```

Therefore:

```text
O(n)
```

### GPA Sorting

Sorting students:

```text
O(n log n)
```

### Extracting Unique Courses

Let:

* n = number of students
* c = average number of courses per student

Complexity:

```text
O(n × c)
```
## Conclusion

This assignment demonstrates how ReactJS can be used to build a dynamic Course Enrollment Dashboard. The application efficiently manages student records, supports GPA-based ranking, performs course filtering, and extracts unique courses while following modern React development practices.

---

## Author

Ranjan Malakar
B.Tech Computer Science & Engineering
Tezpur University
