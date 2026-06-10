# Assignment 14 – Garbage Collection and Circular References in Python

## Question

Create a scenario where objects are "dead" but still have a reference count higher than zero, then force the Garbage Collector to clean them up.

Requirements:

* Create a Node class
* Create Node A and Node B
* Create circular references:

  * A.link = B
  * B.link = A
* Use sys.getrefcount()
* Delete A and B
* Use gc module to investigate memory
* Use gc.collect() to remove unreachable objects

---

## Objective

To demonstrate how circular references can prevent immediate object destruction and how Python's Garbage Collector resolves such situations.

---

## Concepts Used

* Reference Counting
* Circular References
* Garbage Collection
* Memory Management
* gc Module
* sys Module

---

## Files Included

* Assignment14.py

---

## Features

* Creates cyclic references
* Displays reference counts
* Demonstrates unreachable objects
* Forces garbage collection manually
* Verifies memory cleanup

---

## Expected Output

```text
Reference counts BEFORE cycle

Reference counts AFTER cycle

Deleting A and B...

Objects still tracked by GC

gc.collect() freed unreachable objects

Cleanup successful
```

---

## Learning Outcomes

* Python memory management
* Reference counting mechanism
* Circular reference problems
* Cyclic garbage collection

---

## Author

Ranjan Malakar
B.Tech CSE
Tezpur University
