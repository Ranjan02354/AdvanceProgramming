# Assignment 16 – Producer Consumer Synchronization using Semaphores

## Question

Develop a multithreaded C program using POSIX threads where multiple threads coordinate access to a shared resource using semaphores or condition variables.

You may implement a Producer-Consumer System.

Requirements:

* Use shared buffer
* Use semaphores
* Use mutex protection
* Demonstrate thread communication
* Print execution order
* Prevent inconsistent behavior

Use:

* sem_wait()
* sem_post()
* pthread_mutex_lock()
* pthread_mutex_unlock()

---

## Objective

To demonstrate thread synchronization using semaphores and mutexes through the Producer-Consumer problem.

---

## Concepts Used

* POSIX Threads
* Semaphores
* Mutex Locks
* Shared Memory
* Producer Consumer Problem
* Synchronization

---

## Files Included

* Assignment16.c

---

## Features

* Shared circular buffer
* Producer thread
* Consumer thread
* Semaphore synchronization
* Safe shared memory access

---

## Expected Output

```text
Starting Producer Consumer System

Producer produced item 1
Consumer consumed item 1

Producer produced item 2
Consumer consumed item 2

...

All threads finished successfully.
```

---

## Time Complexity

| Operation       | Complexity |
| --------------- | ---------- |
| Produce Item    | O(1)       |
| Consume Item    | O(1)       |
| Total Execution | O(n)       |

where n = number of items processed.

---

## Learning Outcomes

* Semaphore synchronization
* Shared resource management
* Thread communication
* Deadlock prevention

---

## Author

Ranjan Malakar
B.Tech CSE
Tezpur University
