# Python Generators Example

## Overview
This project demonstrates how **generators** in Python work and why they are useful.

Generators are special functions that use the `yield` keyword to return values one at a time, instead of computing and storing everything in memory at once. This makes them memory-efficient and perfect for handling large datasets or even infinite sequences.

---

## Example

```python
import sys

def infinite_counter():
    num = 0
    while True:
        yield num
        num += 1

values = infinite_counter()

for _ in range(5):
    print(next(values))

print(f"generator size: {sys.getsizeof(values)} bytes")
```

### Step-by-step:
1. **Define a generator**:  
   The `infinite_counter()` function starts from `0` and keeps yielding numbers infinitely using `yield`.
   
2. **Create generator object**:  
   `values = infinite_counter()` creates a generator object. At this point, the function hasn't executed yet; it's just ready to generate values when asked.

3. **Iterate with `next()`**:  
   The `for _ in range(5)` loop calls `next(values)` five times, retrieving numbers `0` to `4`.

4. **Memory efficiency**:  
   `sys.getsizeof(values)` shows that the generator object itself uses only a small, fixed amount of memory, regardless of how many numbers it can generate.

---

## Example Output
```
0
1
2
3
4
generator size: 112 bytes
```

*(The size may vary depending on your system, but it will always remain small even for infinite sequences.)*

---

## Key Takeaways
- Generators use `yield` to produce values lazily (on demand).
- They don’t store all values in memory, making them **highly memory-efficient**.
- Useful for large datasets, streaming data, or infinite sequences.

---

## Run the Code
```bash
python generator_example.py
```

---

## License
This project is open-source and free to use for learning purposes.
