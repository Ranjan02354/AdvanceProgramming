# Assignment 13 – Dynamic String Buffer in C

## Question

Implement a Dynamic String Buffer that automatically grows as needed.

Requirements:

1. Create a StringBuffer struct containing:

   * char *data
   * size_t length
   * size_t capacity

2. Implement:

   * sb_init()
   * sb_append()
   * sb_free()

3. Use malloc() and realloc() safely.

4. Handle allocation failures correctly.

5. Demonstrate the buffer growing at least twice and free all memory.

---

## Objective

To implement a dynamic string buffer that automatically expands when additional memory is required while ensuring safe memory management.

---

## Concepts Used

* Structures
* Dynamic Memory Allocation
* malloc()
* realloc()
* free()
* String Manipulation
* Memory Safety

---

## Files Included

* Assignment13.c

---

## Features

* Dynamic string storage
* Automatic capacity expansion
* Safe realloc usage
* Prevention of memory leaks
* Destructor-style cleanup function

---

## Expected Output

```text
Initial Capacity: 8

Buffer resized to capacity: 16
Buffer resized to capacity: 32

String: Hello World! Dynamic String Buffer Example

All memory freed successfully.
```

---

## Time Complexity

| Operation     | Complexity |
| ------------- | ---------- |
| Append String | O(n)       |
| Resize Buffer | O(n)       |
| Free Memory   | O(1)       |

---

## Learning Outcomes

* Dynamic memory management
* Safe use of realloc()
* Buffer resizing strategies
* Memory leak prevention

---

## Author

Ranjan Malakar
B.Tech CSE
Tezpur University
