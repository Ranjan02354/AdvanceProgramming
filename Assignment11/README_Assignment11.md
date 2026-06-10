# Assignment 11 – Library Management System using Python Abstraction

## Question

Design a library system in Java or Python with:

### Base/Abstract Class

Create a base/abstract class `LibraryItem` containing:

* title
* year

and an abstract/common method:

```python id="wtub2a"
displayInfo()
```

### Create Subclasses

#### Book

* Add author

#### DVD

* Add duration
* Add genre

### Your implementation should clearly show:

* Use of abstraction (common structure in base class)
* Method overriding in subclasses
* Polymorphism using a collection of LibraryItem objects

### One Additional Feature

Use either:

* Constructor overloading / default arguments

OR

* Class/static counter

---

## Objective

The objective of this assignment is to implement a Library Management System using Object-Oriented Programming principles. The system demonstrates abstraction, inheritance, method overriding, polymorphism, and static class members through different library item types.

---

## Concepts Used

* Abstract Classes
* Abstract Methods
* Inheritance
* Method Overriding
* Polymorphism
* Static/Class Variables
* Default Arguments
* Object-Oriented Programming

---

## Files Included

* Assignment11.py

---

## Class Structure

### LibraryItem (Abstract Base Class)

Common attributes:

```text id="itc7q8"
title
year
```

Common method:

```python id="sxfx6k"
displayInfo()
```

Additional Feature:

```python id="9h2n6l"
total_items
```

Static counter used to track total library items created.

---

### Book Class

Additional attribute:

```text id="3s0q9z"
author
```

Features:

* Inherits LibraryItem
* Overrides displayInfo()
* Uses default argument for author

---

### DVD Class

Additional attributes:

```text id="55v3r2"
duration
genre
```

Features:

* Inherits LibraryItem
* Overrides displayInfo()
* Uses default argument for genre

---

## Features

### Library Item Management

* Create books
* Create DVDs
* Store common information in a base class

### Abstraction

* Enforces implementation of displayInfo()
* Prevents direct instantiation of LibraryItem

### Polymorphism

* Stores Book and DVD objects together
* Calls displayInfo() using a common reference

### Static Counter

* Tracks total number of library items created

---

## How to Run

```bash id="r4lvrh"
python Assignment11.py
```

---

## Sample Output

```text id="vmyv9v"
Library Items:

Book Details:
Title  : The Alchemist
Author : Paulo Coelho
Year   : 1988

Book Details:
Title  : Python Basics
Author : Unknown Author
Year   : 2020

DVD Details:
Title    : Inception
Genre    : Sci-Fi
Duration : 148 minutes
Year     : 2010

DVD Details:
Title    : The Lion King
Genre    : General
Duration : 88 minutes
Year     : 1994

Total Library Items Created: 4
```

---

## Algorithm

### Creating Library Items

1. Create Book objects.
2. Create DVD objects.
3. Automatically increment static counter.

### Polymorphic Display

1. Store all objects in a single collection.
2. Iterate through the collection.
3. Call displayInfo().
4. Python automatically invokes the correct overridden method.

### Static Counter

1. Increment counter whenever a LibraryItem is created.
2. Retrieve count using:

```python id="jupm0v"
LibraryItem.getTotalItems()
```

---

## OOP Features Demonstrated

### Abstraction

```python id="fxf4tz"
class LibraryItem(ABC)
```

Defines a common structure for all library items.

Abstract method:

```python id="wxwjlwm"
@abstractmethod
def displayInfo(self):
```

Forces subclasses to provide their own implementation.

---

### Inheritance

```python id="t2xt6r"
class Book(LibraryItem)
class DVD(LibraryItem)
```

Both classes inherit common properties from LibraryItem.

---

### Method Overriding

```python id="l9gbwh"
def displayInfo(self):
```

Each subclass provides its own version of displayInfo().

---

### Polymorphism

```python id="aw7jgx"
library = [book1, book2, dvd1, dvd2]
```

Stores different object types in one collection and invokes the same method.

---

### Static Counter

```python id="a4y9w2"
total_items
```

Tracks the total number of LibraryItem objects created.

---

### Default Arguments

```python id="jw6u5u"
author="Unknown Author"
genre="General"
```

Demonstrates constructor overloading behavior in Python.

---

## Time Complexity

| Operation           | Complexity |
| ------------------- | ---------- |
| Create Item         | O(1)       |
| Display Item        | O(1)       |
| Traverse Collection | O(n)       |
| Get Total Items     | O(1)       |

where **n** is the number of library items.

## Author

Ranjan Malakar
B.Tech Computer Science & Engineering
Tezpur University
