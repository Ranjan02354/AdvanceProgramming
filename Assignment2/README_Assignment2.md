# Assignment 2 – Space Complexity Analysis in C

## Question

Write a C program for three different operations as stated in Question 1 to analyze the space complexity.

---

## Objective

The objective of this assignment is to study and compare the space requirements of algorithms with different space complexities by allocating memory dynamically and observing how memory usage grows as the input size increases.

---

## Concepts Used

* Space Complexity Analysis
* Dynamic Memory Allocation
* malloc()
* free()
* Arrays and Matrices
* Big O Notation

---

## Space Complexity Demonstrated

### 1. Constant Space Complexity – O(1)

Uses only a fixed number of variables regardless of input size.

### 2. Linear Space Complexity – O(n)

Allocates a one-dimensional array whose size depends on the input value.

### 3. Quadratic Space Complexity – O(n²)

Allocates a two-dimensional matrix whose memory requirement grows as the square of the input size.

---

## Files Included

* Assignment2.c

## Program Features

* Demonstrates constant, linear, and quadratic space usage.
* Uses dynamic memory allocation.
* Properly frees allocated memory to prevent memory leaks.
* Measures execution for multiple input sizes:

  * 100
  * 500
  * 1000
  * 2000
  * 4000

---

## Space Complexity Summary

| Function         | Space Complexity |
| ---------------- | ---------------- |
| constant_time()  | O(1)             |
| linear_time()    | O(n)             |
| quadratic_time() | O(n²)            |

---


## Author

Ranjan Malakar
B.Tech CSE
Tezpur University
