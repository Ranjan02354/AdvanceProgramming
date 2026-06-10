# Assignment 15 – Race Condition and Mutex Synchronization using POSIX Threads

## Question

Write a multithreaded C program using POSIX threads where multiple threads increment a shared global counter variable many times.

First implement the program without any synchronization and observe the incorrect output caused by a race condition.

Then modify the program using a mutex (`pthread_mutex_t`) to protect the critical section and produce the correct final counter value.

Your program must demonstrate:

* `pthread_create()`
* `pthread_join()`
* `pthread_mutex_lock()`
* `pthread_mutex_unlock()`

Also explain briefly why the race condition occurs and how the mutex solves the problem.

---

## Objective

To understand race conditions in multithreaded programming and demonstrate how mutex synchronization ensures safe access to shared resources.

---

## Concepts Used

* POSIX Threads (Pthreads)
* Multithreading
* Race Conditions
* Critical Sections
* Mutex Locks
* Thread Synchronization

---

## Files Included

* race_condition.c
* mutex_solution.c

---

## Features

* Demonstrates incorrect results without synchronization.
* Demonstrates correct results using mutex protection.
* Uses shared global counter.
* Shows thread creation and joining.

---

## Expected Output

### Without Mutex

```text
Final Counter Value: 1674321
```

(Varies every run)

### With Mutex

```text
Final Counter Value: 2000000
```

---

## Time Complexity

| Operation         | Complexity |
| ----------------- | ---------- |
| Counter Increment | O(1)       |
| Total Execution   | O(n)       |

where n = total increments performed.

---

## Learning Outcomes

* Understanding race conditions
* Critical section protection
* Mutex synchronization
* Thread-safe programming

---

## Author

Ranjan Malakar
B.Tech CSE
Tezpur University
