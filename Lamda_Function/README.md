
# 🐍 Lambda Functions in Python — Example Overview

## 🔹 What is a Lambda Function?
A **lambda function** in Python is a **small, anonymous function** defined using the `lambda` keyword.  
It can take any number of arguments but can only contain **one expression**.

**Syntax:**
```python
lambda arguments: expression
```
Lambda functions are often used for **short, one-line operations**—especially when combined with built-in functions like `map()`, `filter()`, `sorted()`, `reduce()` etc.

---

## ⚙️ Example Overview
This example demonstrates how to use lambda functions with:
- **map()** → applies a transformation to every element in a list.  
- **filter()** → selects elements that meet a condition.  
- **sorted()** → sorts data using a custom key.  
- **reduce()** → combines elements into a single result through accumulation.

Each of these functions uses a lambda expression to perform operations concisely—such as squaring numbers, finding even values, sorting by computed keys, and summing squared values.

---

## 🧠 Key Concepts Illustrated
- **Lambda + Map** → Apply quick transformations (e.g., square each number).  
- **Lambda + Filter** → Extract elements that satisfy conditions (e.g., even numbers).  
- **Lambda + Sorted** → Customize sorting logic (e.g., sort by square, descending).  
- **Lambda + Reduce** → Perform accumulative operations (e.g., sum of squares).  

---

## 💡 Why Use Lambda Functions?
- Reduce code clutter by avoiding `def` for small, temporary functions.  
- Improve readability for short operations.  
- Work seamlessly with Python’s functional tools.

---

## 🧾 Output Example
When running the script, you’ll see printed results showing:
- The list of squared numbers.  
- Filtered even numbers.  
- Numbers sorted by their squares (in descending order).  
- The total sum of all squared numbers.

---

## 🚀 Summary
Lambda functions make your code **short, expressive, and powerful** when combined with built-in higher-order functions.  
They are a key tool for writing **clean, functional-style Python code**.
