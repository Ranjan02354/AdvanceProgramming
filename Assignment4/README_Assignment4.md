# Assignment 4 – Product Inventory Management using List and Dictionary in Python

## Question

Create a Python program using a list and dictionary to store products with name and stock quantity.

Display all products whose stock is less than 10.

---

## Objective

The objective of this assignment is to understand the use of Python lists and dictionaries for storing and managing structured data. The program allows users to enter product details and identifies products with low stock levels.

---

## Concepts Used

* Python Lists
* Python Dictionaries
* User Input Handling
* Conditional Statements
* Iteration using Loops
* Inventory Management

---

## Files Included

* Assignment4.py

---

## Program Features

* Accepts multiple product records from the user.
* Stores products using a list of dictionaries.
* Displays all entered products.
* Identifies products whose stock quantity is less than 10.
* Demonstrates structured data storage using Python collections.

---

## How to Run

```bash
python Assignment4.py
```

---

## Sample Input

```text
Enter number of products: 3

Product 1
Enter product name: Mouse
Enter stock quantity: 5

Product 2
Enter product name: Keyboard
Enter stock quantity: 20

Product 3
Enter product name: Monitor
Enter stock quantity: 8
```

---

## Sample Output

```text
All Products:
Name: Mouse | Stock: 5
Name: Keyboard | Stock: 20
Name: Monitor | Stock: 8

Products with stock less than 10:
Name: Mouse | Stock: 5
Name: Monitor | Stock: 8
```

---

## Algorithm

1. Create an empty list to store products.
2. Accept the number of products from the user.
3. For each product:

   * Input product name.
   * Input stock quantity.
   * Store details in a dictionary.
   * Add the dictionary to the list.
4. Display all products.
5. Traverse the list and check stock quantity.
6. Display products whose stock is less than 10.

---

## Time Complexity

| Operation                  | Complexity |
| -------------------------- | ---------- |
| Adding Products            | O(n)       |
| Displaying Products        | O(n)       |
| Finding Low Stock Products | O(n)       |

Where **n** is the number of products.

---

## Author

Ranjan Malakar
B.Tech Computer Science & Engineering
Tezpur University
