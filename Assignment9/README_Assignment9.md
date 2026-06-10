# Assignment 9 – Banking System using Java OOP Concepts

## Question

Design a banking system in Java with:

### Base Class: Account

A base class `Account` containing private fields:

* accountNumber
* ownerName
* balance

Requirements:

* Provide getters and setters
* Provide at least two constructors (use constructor chaining)
* Implement `deposit()` and `withdraw()` with proper validation
* Add a `display()` method

### Extend it with:

#### SavingsAccount

* Add `interestRate`
* Override `display()`
* Show interest earned

#### CurrentAccount

* Add `overdraftLimit`
* Restrict withdrawals accordingly

### Your implementation should clearly show:

* Proper encapsulation (no direct field access)
* Constructor overloading and chaining using `this(...)`
* Inheritance and method overriding using `@Override` and `super`
* Polymorphism using an `Account` reference list
* Validation using exceptions or assertions

---

## Objective

The objective of this assignment is to design a simple banking system using Object-Oriented Programming principles in Java. The system demonstrates encapsulation, inheritance, polymorphism, constructor chaining, method overriding, and exception handling.

---

## Concepts Used

* Classes and Objects
* Encapsulation
* Constructor Overloading
* Constructor Chaining
* Inheritance
* Method Overriding
* Polymorphism
* Exception Handling
* Java Collections (ArrayList)

---

## Files Included

* Assignment9.java

---

## Class Structure

### Account (Base Class)

Fields:

```text
accountNumber
ownerName
balance
```

Methods:

* deposit()
* withdraw()
* display()
* getters and setters

---

### SavingsAccount

Additional Field:

```text
interestRate
```

Features:

* Inherits Account
* Calculates interest earned
* Overrides display()

---

### CurrentAccount

Additional Field:

```text
overdraftLimit
```

Features:

* Supports overdraft withdrawals
* Overrides withdraw()
* Overrides display()

---

## Features

### Account Management

* Create savings accounts
* Create current accounts
* Deposit money
* Withdraw money

### Validation

* Prevent negative deposits
* Prevent invalid withdrawals
* Handle overdraft restrictions

### Polymorphism

Stores different account types using:

```java
ArrayList<Account>
```

and invokes:

```java
account.display();
```

through parent references.

---

## How to Run

### Compile

```bash
javac Assignment9.java
```

### Execute

```bash
java Assignment9
```

---

## Sample Output

```text
All Accounts:

Account Number : SAV001
Owner Name     : Riya Sharma
Balance        : Rs.10000.0
Interest Rate  : 4.5%
Interest Earned: Rs.450.0

Account Number : CUR001
Owner Name     : Arjun Mehta
Balance        : Rs.5000.0
Overdraft Limit: Rs.2000.0

Deposited Rs.5000.0 successfully.
Withdrawn Rs.3000.0 successfully.

Updated Account Details:
...
```

---

## Algorithm

### Deposit Operation

1. Validate amount.
2. Ensure amount is positive.
3. Add amount to balance.
4. Update account balance.

### Withdraw Operation

1. Validate amount.
2. Check available balance.
3. Deduct amount.
4. Update balance.

### Current Account Withdrawal

1. Check balance + overdraft limit.
2. Allow withdrawal if limit is not exceeded.
3. Update account balance.

### Savings Account Display

1. Retrieve account details.
2. Calculate interest.
3. Display interest information.

---

## OOP Features Demonstrated

### Encapsulation

```java
private String accountNumber;
private String ownerName;
private double balance;
```

Access provided through getters and setters.

---

### Constructor Chaining

```java
this(accountNumber, ownerName, 0.0);
```

Used to avoid code duplication.

---

### Inheritance

```java
class SavingsAccount extends Account
class CurrentAccount extends Account
```

---

### Method Overriding

```java
@Override
public void display()
```

Customized behavior in subclasses.

---

### Polymorphism

```java
ArrayList<Account> accounts
```

Stores multiple account types using parent references.

---

## Time Complexity

| Operation             | Complexity |
| --------------------- | ---------- |
| Deposit               | O(1)       |
| Withdraw              | O(1)       |
| Display               | O(1)       |
| Traverse Account List | O(n)       |

where **n** is the number of accounts.


## Author

Ranjan Malakar
B.Tech Computer Science & Engineering
Tezpur University
