# Assignment 5 – Todo List Application using React useState

## Question

Create a simple React component that maintains a list of todos using useState.

Allow the user to add a todo and display all added todos on the screen.

---

## Objective

The objective of this assignment is to understand React state management using the useState Hook and build a simple interactive Todo List application.

---

## Concepts Used

* ReactJS
* Functional Components
* useState Hook
* Event Handling
* Controlled Components
* Array State Management
* Dynamic Rendering

---

## Files Included

* App.tsx / TodoApp.tsx

---

## Program Features

* Add new todo items.
* Prevent addition of empty tasks.
* Display all added todos dynamically.
* Automatically update the UI when state changes.
* Demonstrates React's reactive rendering behavior.

---

## How to Run

### Install Dependencies

```bash
npm install
```

### Start Development Server

```bash
npm run dev
```

or

```bash
npm start
```

(depending on project setup)

---

## Sample Usage

### Input

```text
Study React
Complete Assignment
Prepare for Viva
```

### Output

```text
Todo List

• Study React
• Complete Assignment
• Prepare for Viva
```

---

## Algorithm

1. Create a state variable to store todos.
2. Create another state variable for user input.
3. Accept task input from the user.
4. Validate that the task is not empty.
5. Add the task to the todo list.
6. Update the state.
7. Render the updated list on the screen.

---

## Time Complexity

| Operation    | Complexity |
| ------------ | ---------- |
| Add Todo     | O(n)       |
| Render Todos | O(n)       |
| Input Update | O(1)       |

Where **n** is the number of todo items.

---

## Author

Ranjan Malakar
B.Tech Computer Science & Engineering
Tezpur University
