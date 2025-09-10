# Python Dunder Methods Demonstration

This Python script, `dunder_methods.py`, demonstrates the use of several common dunder (double underscore) methods. These special methods allow you to emulate the behavior of built-in types and implement operator overloading.

The script defines a `Book` class that uses the following dunder methods:

### Implemented Dunder Methods

-   `__init__(self, title, pages)`
    -   The constructor for the class. Initializes a new `Book` instance with a title and page count.

-   `__str__(self)`
    -   Provides a user-friendly string representation of the object. Called by `print()` and `str()`.
    -   Example: `print(book1)`
    -   Output: `📖 Python Tricks (300 pages)`

-   `__repr__(self)`
    -   Provides an official, unambiguous string representation of the object, which can be used to recreate the object.
    -   Example: `repr(book1)`
    -   Output: `Book(title='Python Tricks', pages=300)`

-   `__len__(self)`
    -   Returns the "length" of the object. Called by `len()`.
    -   Example: `len(book1)`
    -   Output: `300`

-   `__add__(self, other)`
    -   Defines the behavior for the addition (`+`) operator.
    -   Example: `print(book1 + book2)`
    -   Output: `📖 Python Tricks Fluent Python (1000 pages)`

-   `__call__(self)`
    -   Allows an instance of the class to be called as a function.
    -   Example: `print(book1())`
    -   Output: `Book 'Python Tricks' has 300 pages.`

-   `__getitem__(self, index)`
    -   Defines behavior for accessing items using subscription (e.g., `obj[index]`).
    -   Example: `print(book1[0:6])`
    -   Output: `Python`

### How to Run

To see the output, navigate into the `Dunder` directory and run the script from your terminal:

```sh
python dunder_methods.py
```

### Expected Output

```
Book 'Python Tricks' has 300 pages.
Book 'Fluent Python' has 700 pages.
📖 Python Tricks (300 pages)
300
📖 Python Tricks Fluent Python (1000 pages)
Python
```