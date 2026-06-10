import { useState } from "react";

function TodoApp() {
  const [todos, setTodos] = useState<string[]>([]);
  const [task, setTask] = useState("");

  // Add a new todo if input is not empty
  const addTodo = () => {
    if (task.trim() === "") return;

    setTodos([...todos, task]);
    setTask("");
  };

  return (
    <div>
      <h3>Todo List</h3>

      <input
        type="text"
        value={task}
        onChange={(e) => setTask(e.target.value)}
      />

      <button onClick={addTodo}>Add</button>

      {/* Display all todos */}
      <ul>
        {todos.map((todo, index) => (
          <li key={index}>{todo}</li>
        ))}
      </ul>
    </div>
  );
}

export default TodoApp;