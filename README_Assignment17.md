# Assignment 17 – User Onboarding Validation Module

## Question

Build a user onboarding validation module.

Requirements:

* Validate email format
* Validate age (minimum age 18)
* Create custom exceptions:

  * InvalidEmailError
  * UnderageError
* Implement RegistrationService
* Use assertions
* Create pytest test suite

---

## Objective

To implement a user registration validation system with proper exception handling, input validation, assertions, and automated testing.

---

## Concepts Used

* Custom Exceptions
* Regular Expressions
* Assertions
* Exception Handling
* Pytest
* Input Validation

---

## Files Included

* registration_service.py
* test_registration_service.py

---

## Features

* Email validation using regex
* Age validation
* Custom exception handling
* Automated testing using pytest
* Assertion-based invariant checking

---

## Expected Output

### Valid Registration

```text
User 'alice@example.com' registered successfully.
```

### Invalid Email

```text
InvalidEmailError:
Email must not be empty or null.
```

### Underage User

```text
UnderageError:
User must be at least 18 years old.
```

---

## Time Complexity

| Operation        | Complexity |
| ---------------- | ---------- |
| Email Validation | O(n)       |
| Age Validation   | O(1)       |
| Registration     | O(n)       |

where n = email length.

---

## Learning Outcomes

* Custom exception design
* Regex-based validation
* Unit testing using pytest
* Defensive programming

---

## Author

Ranjan Malakar
B.Tech CSE
Tezpur University
