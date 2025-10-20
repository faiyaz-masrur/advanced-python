# Python Function Arguments

This README explains **positional-only arguments**, **keyword-only
arguments** and how to use **args** and **kwargs** in Python.
It also describes how these concepts are applied in the given example
functions.

------------------------------------------------------------------------

## ⚙️ 1. Positional-Only Arguments (`/`)

**Definition:**
Arguments before the `/` symbol in a function definition must be passed
**only by position**, not by keyword.

**Why Use:**
- To enforce a strict calling convention.
- Useful in APIs or libraries to prevent accidental keyword usage.

**Example from code:**
`name` and `age` in the `student_report` function must be passed
**positionally**.
For instance:

``` python
student_report("Faiyaz", 23, grade="A+", school="BRAC University")
```

✅ Correct --> `name` and `age` are passed positionally.
❌ Incorrect --> `name="Faiyaz", age=23, ...` (raises
`TypeError`)

------------------------------------------------------------------------

## 🧾 2. Keyword-Only Arguments (`*`)

**Definition:**
Arguments after the `*` symbol must be passed **by keyword**, not by
position.

**Why Use:**
- To make your function calls clearer.\
- Prevents confusion when there are many parameters.

**Example from code:**
`grade` and `school` in the `student_report` function must be passed
using their names.

------------------------------------------------------------------------

## 🌀 3. \*args (Variable-Length Positional Arguments)

**Definition:**
`*args` allows you to pass **any number of positional arguments** to a
function.
All extra positional arguments are collected into a **tuple**.

**Why Use:**
- When you don't know how many arguments will be passed.
- Common in utility or logging functions.

**Example from code:**
In `project_details`, all technologies like `Python`, `TensorFlow`,
`React` are stored in `technologies` as a tuple.

------------------------------------------------------------------------

## 🧩 4. \*\*kwargs (Variable-Length Keyword Arguments)

**Definition:**
`**kwargs` allows you to pass **any number of keyword arguments**.
All extra keyword arguments are collected into a **dictionary**.

**Why Use:**
- To accept flexible configuration or metadata.\
- Common in API wrappers or class initializers.

**Example from code:**\
In `project_details`, keyword arguments like `duration="6 months"` and
`team_size=5` are stored in `info` as a dictionary.

------------------------------------------------------------------------

## 💡 Summary

  ---------------------------------------------------------------------------
  Argument Type     Symbol       Passed By    Stored As     Example Use
  ----------------- ------------ ------------ ------------- -----------------
  Positional-only   `/`          Position     N/A           Fixed-order
                                                            parameters

  Keyword-only      `*`          Keyword      N/A           Enforce clarity

  Variable          `*args`      Position     Tuple         Variable-length
  positional                                                inputs

  Variable keyword  `**kwargs`   Keyword      Dict          Flexible
                                                            configuration
  ---------------------------------------------------------------------------

------------------------------------------------------------------------

## 🧠 Concept in the Example Code (Summary)

The code defines two functions:
- `student_report()` uses **positional-only** and **keyword-only**
arguments for strict clarity.
- `project_details()` uses **`*args`** and **`**kwargs`** to handle a
flexible number of inputs.

Both demonstrate **different argument styles** in real-world Python
programming.

------------------------------------------------------------------------

### ✅ When to Use Which

-   Use **positional-only** when argument order is critical.\
-   Use **keyword-only** for clarity in large functions.\
-   Use **`*args`** for optional positional parameters.\
-   Use **`**kwargs`** for dynamic keyword inputs.

------------------------------------------------------------------------

**Author:** Faiyaz Masrur\
**Topic:** Understanding Python Function Arguments
