# Assignment 6 – Student Performance Analyzer in Java

## Question

Develop a student performance analyzer in Java. You are given a list of students of your batch.

Each student has:

* id (int)
* name (String)
* courses (List<String>)
* scores (Map<String, Integer>) where key = course and value = marks

### Implement the following methods

```java
List<Student> getTopNStudents(List<Student> students, int n);

Map<String, Double> getAverageScorePerCourse(List<Student> students);

Set<String> getAllUniqueCourses(List<Student> students);
```

### Requirements

* Use ArrayList, HashMap and HashSet
* Use Streams for aggregation and filtering
* Sort students by average score (descending)
* Use Comparator
* Handle missing course scores using getOrDefault()
* Ensure type safety using Generics

### Complexity Analysis

1. What is the time complexity of computing course averages?
2. What is the complexity of sorting top N students?

---

## Objective

The objective of this assignment is to analyze student performance using Java Collections Framework and Stream API. The system computes average marks, identifies top-performing students, and extracts unique courses from student records.

---

## Concepts Used

* ArrayList
* HashMap
* HashSet
* Java Streams
* Comparator
* Generics
* getOrDefault()
* Functional Programming
* Collection Framework

---

## Files Included

* Assignment6.java

---

## Program Features

* Stores student records efficiently.
* Calculates average score of each student.
* Finds top N students based on average marks.
* Computes average score for each course.
* Displays all unique courses.
* Uses Java Stream API for aggregation and filtering.
* Handles missing marks safely using getOrDefault().

---

## How to Run

### Compile

```bash
javac Assignment6.java
```

### Execute

```bash
java Assignment6
```

---

## Sample Output

```text
Top Students:
1 Ranjan Avg: 92.5
2 Rahul Avg: 82.5

Average Score Per Course:
{CS=47.5, Math=85.0, Physics=42.5}

Unique Courses:
[Math, CS, Physics]
```

---

## Algorithm

### getTopNStudents()

1. Calculate average score of every student.
2. Sort students in descending order.
3. Select top N students.
4. Return the result.

### getAverageScorePerCourse()

1. Extract all unique courses.
2. For each course:

   * Retrieve marks from all students.
   * Use getOrDefault() for missing scores.
   * Compute average.
3. Store results in a HashMap.

### getAllUniqueCourses()

1. Traverse all student course lists.
2. Flatten the lists using Stream API.
3. Store unique values in a HashSet.

---

## Complexity Analysis

### Computing Course Averages

If:

* n = number of students
* c = number of unique courses

Time Complexity:

```text
O(n × c)
```

### Sorting Top N Students

Sorting all students:

```text
O(n log n)
```

---

## Author

Ranjan Malakar
B.Tech Computer Science & Engineering
Tezpur University
