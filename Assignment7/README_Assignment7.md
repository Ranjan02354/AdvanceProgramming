# Assignment 7 – Activity Log Analyzer in Python

## Question

Develop an activity log analyzer in Python.

You are given a list of activity records:

```python id="8n3ylc"
{
    "user": str,       # roll number of student
    "action": str,     # online activity (apps/websites visited)
    "duration": float  # screen time for each activity
}
```

### Implement the following functions

```python id="6w3z9m"
def total_time_per_user(logs: list[dict]) -> dict[str, float]

def most_active_users(logs: list[dict], k: int) -> list[str]

def unique_actions(logs: list[dict]) -> set[str]
```

### Requirements

* Use dict, set, and list
* Use comprehensions where appropriate
* Use sorted() with key
* Avoid explicit loops where possible
* Use typing annotations
* Use defaultdict optionally
* Use reduce() to compute total activity time

### Complexity Analysis

1. Time complexity for computing Top K users
2. Space complexity of storing intermediate results

---

## Objective

The objective of this assignment is to analyze student activity logs using Python built-in containers and functional programming techniques. The system computes total screen time, identifies the most active users, and extracts unique online activities.

---

## Concepts Used

* Python Lists
* Dictionaries
* Sets
* defaultdict
* reduce()
* List Comprehensions
* Set Comprehensions
* Sorting with Key Functions
* Type Hints
* Functional Programming

---

## Files Included

* Assignment7.py

---

## Program Features

* Calculates total screen time per user.
* Finds the top K most active users.
* Displays all unique activities performed by users.
* Uses Python built-in data structures efficiently.
* Implements reduce() for cumulative calculations.
* Uses comprehensions for concise and readable code.

---

## How to Run

```bash id="cbbmzf"
python Assignment7.py
```

---

## Sample Output

```text id="h0f8pw"
Total time per user:
{
 'CSB24077': 1.5,
 'CSB24017': 2.0,
 'CSB24067': 0.5,
 'CSB24071': 3.0,
 'CSB24080': 1.0,
 'CSB24062': 2.5
}

Most active users:
['CSB24071', 'CSB24062']

Unique actions:
{'YouTube', 'Instagram', 'WhatsApp', 'Facebook', 'Chrome'}
```

---

## Algorithm

### total_time_per_user()

1. Group activity durations by user using defaultdict.
2. Store all durations corresponding to each user.
3. Use reduce() to compute the total activity time.
4. Return a dictionary mapping users to total screen time.

### most_active_users()

1. Compute total activity time per user.
2. Sort users in descending order based on total time.
3. Return the top K users.

### unique_actions()

1. Traverse all activity records.
2. Extract action names using set comprehension.
3. Return the set of unique actions.

---

## Complexity Analysis

### Time Complexity for Top K Users

Let:

* n = total number of activity records
* u = number of unique users

Computing totals:

```text id="qywrl2"
O(n)
```

Sorting users:

```text id="isg1r2"
O(u log u)
```

Overall Complexity:

```text id="5z1m0t"
O(n + u log u)
```

---

### Space Complexity

Intermediate structures:

* defaultdict for grouped durations
* totals dictionary
* sorted user list

Space Complexity:

```text id="8yzt2k"
O(n + u)
```

where:

* n = activity records
* u = unique users

## Author

Ranjan Malakar
B.Tech Computer Science & Engineering
Tezpur University
