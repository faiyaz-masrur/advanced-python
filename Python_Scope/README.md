# Understanding Python Scope: Global, Local, and Nonlocal

Python scope determines where variables are accessible within your program. Understanding how **local**, **global**, and **nonlocal** scopes work helps you control variable visibility and avoid unexpected behavior.

---

## 🧩 Types of Scope in Python

### 1. **Global Scope**
Variables declared outside any function are **global**.  
They can be accessed anywhere in the program unless shadowed by a local variable.

**Example:**  
A variable `x = "global x"` defined outside all functions can be read or modified using the `global` keyword inside a function.

---

### 2. **Local Scope**
A variable created inside a function belongs to the **local scope** of that function.  
It is only accessible within that function and disappears once the function finishes execution.

**Example:**  
Inside `inner_function()`, a local variable `x = "inner x"` is created.  
It temporarily hides the outer or global variable `x` within that scope.

---

### 3. **Nonlocal Scope**
A **nonlocal** variable exists in an enclosing function’s scope (not global).  
You can use the `nonlocal` keyword inside a nested function to modify that variable.

**Example:**  
`modify_outer()` uses `nonlocal x` to modify the variable from `outer_function()`, not the global one.

---

### 🔁 How They Interact

Let’s understand the order of scope resolution using the **LEGB Rule**:

| Scope Type | Description | Example |
|-------------|-------------|----------|
| **L**ocal | Inside the current function | `x = "inner x"` |
| **E**nclosing | In the outer (non-global) function | `x = "outer x"` |
| **G**lobal | Defined at the top level of the script | `x = "global x"` |
| **B**uilt-in | Python’s built-in names (e.g., `len`, `print`) | `print()` |

Python searches variables in this order: **Local → Enclosing → Global → Built-in**.

---

### 🧠 Output Behavior Summary

When running the example script:

```
Initially: global x
Inside inner_function: inner x
Inside modify_outer: modified by inner (nonlocal)
Inside outer_function after modification: modified by inner (nonlocal)
After outer_function: global x
Inside global_modifier: modified globally
After global_modifier: modified globally
```

### 🔍 Explanation
- **Initially**, `x` is `"global x"`.
- **inner_function()** creates its own local `x`, printing `"inner x"`.
- **modify_outer()** changes the `outer_function`’s variable using `nonlocal x`.
- The **global variable** remains unchanged until `global_modifier()` explicitly modifies it with `global x`.

---

### ✅ Key Takeaways
- Use `global` to modify global variables inside a function.
- Use `nonlocal` to modify variables in the nearest enclosing scope.
- Local variables override outer ones within their function.
- Python follows the **LEGB** lookup order for variable resolution.

---

### 📘 Summary
Understanding Python’s scope rules is essential for writing clean, bug-free, and modular code. Proper use of `global` and `nonlocal` helps you manage variable accessibility effectively across different function levels.

