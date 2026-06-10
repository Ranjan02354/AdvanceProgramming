# Assignment 3 – Book Search System using ArrayList in Java

## Question

Write a Java program using ArrayList to store book titles.

Add at least 5 books and search for books whose title contains a given word.

---

## Objective

The objective of this assignment is to understand the use of Java Collections Framework, specifically ArrayList, for storing and managing data dynamically. The program allows users to search for books by entering a keyword and displays all matching book titles.

---

## Concepts Used

* Java Collections Framework
* ArrayList
* String Handling
* User Input using Scanner
* Case-Insensitive Search
* Iteration using Loops

---

## Files Included

* Assignment3.java

---

## Program Features

* Stores multiple book titles using ArrayList.
* Accepts user input for searching.
* Performs case-insensitive keyword matching.
* Displays all books containing the entered word.
* Demonstrates dynamic data storage using collections.

---

## How to Run

### Compile

```bash id="it6m8i"
javac Assignment3.java
```

### Execute

```bash id="6ecpwu"
java Assignment3
```

---

## Sample Input

```text id="xym6fo"
Enter a word to search:
computer
```

## Sample Output

```text id="ynpq4j"
Matching books are:

Computer Networks
Computer Architecture
```

---

## Algorithm

1. Create an ArrayList to store book titles.
2. Add at least five book titles.
3. Accept a search keyword from the user.
4. Traverse the ArrayList.
5. Compare each title with the search keyword.
6. Display matching titles.

---

## Time Complexity

| Operation          | Complexity         |
| ------------------ | ------------------ |
| Adding Books       | O(1) per insertion |
| Searching Books    | O(n)               |
| Displaying Results | O(n)               |

Where **n** is the number of books stored in the ArrayList.

## Author

Ranjan Malakar
B.Tech Computer Science & Engineering
Tezpur University
