# Python Decorator Example: Logging Execution Time

This project demonstrates a **practical use of decorators in Python** — measuring and logging the execution time of functions.  

---

## 📌 What is a Decorator?
A decorator in Python is a **function that wraps another function** to extend or modify its behavior, without changing the function’s original code.  

They are commonly used for:
- Logging  
- Authentication  
- Caching  
- Performance monitoring  

---

## 🔎 How It Works in This Project

- The program defines a decorator called **`log_execution_time`**.  
- When applied to a function, the decorator:  
  1. Records the start time before the function runs.  
  2. Executes the original function.  
  3. Records the end time after the function finishes.  
  4. Calculates and prints the total execution time.  

- The decorator is applied to a function called **`process_data`**.  
- This function simulates heavy computation by squaring numbers in a list and adding a small delay.  
- Because of the decorator, every call to `process_data` automatically prints how long it took to run, without adding timing code inside the function itself.  
