# 🧩 Singleton Design Pattern in Python

## 🧠 What is the Singleton Pattern?

The **Singleton Design Pattern** ensures that **only one instance** of a
class exists throughout the application.\
It provides a **global point of access** to that instance, meaning all
parts of the program use the same object.

------------------------------------------------------------------------

## 🎯 Why Use the Singleton Pattern?

-   ✅ To **control access** to shared resources (e.g., database
    connections, configuration files).
-   ✅ To **avoid conflicts** caused by multiple instances of the same
    class.
-   ✅ To **ensure consistency** --- all parts of the application share
    the same data.
-   ✅ To **save memory** --- instead of creating multiple identical
    objects, you reuse one.

------------------------------------------------------------------------

## 🧰 Where It's Commonly Used

-   🗃 **Database Connection Managers**
-   ⚙️ **Configuration Managers**
-   🧾 **Loggers**
-   🔌 **Hardware Access Handlers**
-   🧠 **Cache Managers**

------------------------------------------------------------------------

## 🔍 Step-by-Step Code Explanation

1.  **`IPerson` (Abstract Base Class)**
    -   Defines a contract using the `print_data()` abstract method.\
    -   Any class inheriting it must implement this method.
2.  **`Person` class**
    -   Implements the `IPerson` interface.
    -   Contains a class variable `__instance` which stores the **single
        instance**.
3.  **`get_instance()` (Static Method)**
    -   Checks if an instance exists.\
    -   If not, creates one with default values.\
    -   Returns the same instance every time.
4.  **`__init__()`**
    -   Initializes `name` and `age` only if no instance exists.\
    -   If an instance already exists, it raises an exception to prevent
        multiple objects.
5.  **`print_data()`**
    -   Prints the instance data (name and age).
6.  **Usage**
    -   `p1 = Person("John", 30)` creates the first instance.\
    -   `p2 = Person.get_instance()` retrieves the **same instance**.\
    -   Both refer to the **same object**, ensuring Singleton behavior.

------------------------------------------------------------------------

## ✅ Output

    Name: John, Age: 30
    Name: John, Age: 30

Even though `get_instance()` creates a new reference, both objects point
to the same memory instance.

------------------------------------------------------------------------

## 🧠 Summary

  Feature            Description
  ------------------ -------------------------------------------------
  **Pattern Type**   Creational
  **Goal**           Ensure only one instance of a class exists
  **Use Case**       Shared resources, global configuration, logging
  **Key Methods**    `__new__()`, `get_instance()`

------------------------------------------------------------------------

## 🚀 Advantages

-   Ensures **controlled access** to resources\
-   Reduces **memory usage**\
-   Maintains **global consistency**

------------------------------------------------------------------------

## ⚠️ Disadvantages

-   Can make unit testing difficult (shared state)\
-   Can hide dependencies (acts like global variables)

------------------------------------------------------------------------

## 🧩 Summary Diagram (Conceptually)

             +---------------------+
             |     Person Class    |
             |---------------------|
             |  __instance (1x)    |
             |  get_instance()     |
             |  print_data()       |
             +---------+-----------+
                       |
                       v
            +------------------------+
            |   One Shared Instance  |
            +------------------------+

------------------------------------------------------------------------

**Author:** Faiyaz Masrur\
**Topic:** Singleton Design Pattern in Python
