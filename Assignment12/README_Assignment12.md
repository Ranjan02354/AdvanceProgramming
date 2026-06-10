# Assignment 12 – E-Commerce Order Processing System using SOLID Principles

## Question

Design a system in Java/Python for processing customer orders in an e-commerce platform.

The system should support:

* Multiple payment methods (Credit Card, UPI, Wallet, etc.)
* Multiple notification channels (Email, SMS, Push Notification)
* Different order types (Regular Order, Discounted Order, Priority Order)
* Different storage mechanisms (Database, File, etc.)

Apply the following SOLID principles:

1. Single Responsibility Principle (SRP)
2. Open/Closed Principle (OCP)
3. Liskov Substitution Principle (LSP)
4. Interface Segregation Principle (ISP)
5. Dependency Inversion Principle (DIP)

The system should:

* Create an order
* Process payment
* Send notification
* Save order details

---

## Objective

To design an extensible and maintainable e-commerce order processing system by applying all five SOLID principles and demonstrating clean software architecture.

---

## Concepts Used

* Object-Oriented Programming
* Abstract Base Classes
* Inheritance
* Polymorphism
* Dependency Injection
* SOLID Principles
* Interface Design

---

## Files Included

* Assignment12.py

---

## Features

* Supports multiple payment methods
* Supports multiple notification channels
* Supports multiple storage mechanisms
* Supports multiple order types
* Easy to extend without modifying existing code
* Demonstrates Dependency Injection

---

## SOLID Principles Demonstrated

| Principle | Implementation                                                                |
| --------- | ----------------------------------------------------------------------------- |
| SRP       | Separate classes for Payment, Notification, Storage                           |
| OCP       | New payment/notification methods can be added without modifying existing code |
| LSP       | All order/payment subclasses work through base types                          |
| ISP       | Small focused interfaces                                                      |
| DIP       | OrderService depends on abstractions                                          |

---

## Learning Outcomes

* Understanding SOLID principles
* Designing loosely coupled systems
* Applying dependency inversion
* Implementing extensible architectures

---

## Author

Ranjan Malakar
B.Tech CSE
Tezpur University
