
# Python Type Hinting with `mypy`

This README demonstrates **Python type hinting** using a `User` class and shows how to use `mypy` for static type checking.

---

## What is Type Hinting?

Type hinting allows you to **declare expected types** for variables, function parameters, and return values.

**Benefits:**
- Improves **readability**  
- Provides better **IDE support**  
- Enables **static type checking** with `mypy`  
- Reduces the need for extra comments  

## User Class Example

Below is a `User` class demonstrating **type hints for constructor, attributes, and methods**:

**Explanation of the Class:**  
- Constructor parameters: `name: str`, `age: int`, `hobbies: Optional[List[str]]`  -> expects string name, integer age, list of string as hobbies
- Class attributes: `self.name: str`, `self.age: int`, `self.hobbies: List[str]`  -> expects name ad string, age as integer, hobbies as list of string
- Methods:
  - `add_hobby(self, hobby: str) -> None` -> expects a string hobby  
  - `get_profile(self) -> str` -> returns formatted string  

---

## Using `mypy` for Static Type Checking

`mypy` checks that your code **matches the type hints** without executing it.

**Run type checking:**
```bash
mypy user.py
```

**Expected output:**
```
error: Argument 1 to "add_hobby" has incompatible type "int"; expected "str"
```
---

## Quick Start

1. Install `mypy`:
```bash
pip install mypy
```

2. Save the `User` class code in `user.py`.

3. Run the file:
```bash
python user.py
```

4. Check types with `mypy`:
```bash
mypy user.py
```

`mypy` will highlight any type mismatches immediately.
