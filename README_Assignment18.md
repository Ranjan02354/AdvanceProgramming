# Assignment 18 – Score Processor with Exception Handling

## Question

Create a ScoreProcessor utility.

Requirements:

* Read a numeric score from a file
* Multiply the score by 10
* Handle FileNotFoundError
* Handle ValueError
* Use try-except-else-finally
* Create pytest test cases

---

## Objective

To demonstrate robust file handling and exception management while ensuring proper resource cleanup.

---

## Concepts Used

* File Handling
* Exception Handling
* try-except-else-finally
* Pytest
* Resource Management

---

## Files Included

* score_processor.py
* test_score_processor.py

---

## Features

* Reads numeric score from file
* Processes score safely
* Handles missing files
* Handles invalid data
* Executes cleanup code regardless of errors

---

## Expected Output

### Valid File

```text
Data processed successfully
File cleanup completed
Final Result: 50
```

### Missing File

```text
Error: File not found.
File cleanup completed
```

### Invalid Data

```text
Error: Invalid number format in file.
File cleanup completed
```

---

## Time Complexity

| Operation          | Complexity |
| ------------------ | ---------- |
| File Read          | O(n)       |
| Integer Conversion | O(n)       |
| Multiplication     | O(1)       |

where n = file content length.

---

## Learning Outcomes

* Safe file processing
* Exception handling
* Cleanup management
* Automated testing

---

## Author

Ranjan Malakar
B.Tech CSE
Tezpur University
