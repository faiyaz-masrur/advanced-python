# 🧩 Composite Design Pattern in Python

## 📘 What is the Composite Design Pattern?

The **Composite Design Pattern** is a **structural pattern** that lets
you treat individual objects and groups of objects uniformly.\
It's used to represent **part-whole hierarchies**, such as trees or
nested structures (e.g., a company → departments → employees).

In simpler terms --- it allows you to treat a **single object** and a
**collection of objects** in the same way.

------------------------------------------------------------------------

## 🎯 Why Use It?

-   To build **hierarchical structures** (e.g., organization trees, file
    systems, UI components).
-   To allow clients to **interact with complex and simple elements
    through a single interface**.
-   To make your code **extensible** --- you can add new components
    without changing existing code.

------------------------------------------------------------------------

## 🏢 Where It's Used

Some real-world examples include: 
- **Company structures**: a company can have departments, and each department can have employees. 
- **File systems**: folders can contain files or other folders. 
- **GUI systems**: windows can contain panels, buttons, and other widgets.

------------------------------------------------------------------------

## 💡 Explanation of the Example Code

In the provided code:

-   **`IDepartment`** is the **abstract base class** defining the
    interface (`__init__` and `print_data`) that all components (both
    individual and composite) must implement.
-   **`Accounting`** and **`Development`** are **leaf components** ---
    they represent individual departments and simply print their own
    data.
-   **`Company`** is the **composite class** --- it contains a
    collection of other departments (components). It can add new
    departments and treat them the same way as individual ones.

When `company.print_data()` is called: - It prints the company's own
information. - Then it delegates the printing of each department to
their respective `print_data()` methods --- demonstrating uniform
treatment of both composite and leaf objects.

------------------------------------------------------------------------

## ✅ Key Takeaways

  -----------------------------------------------------------------------
  Concept                       Description
  ----------------------------- -----------------------------------------
  **Component**                 The abstract interface (`IDepartment`)
                                that defines common operations.

  **Leaf**                      Represents an individual object (e.g.,
                                `Accounting`, `Development`).

  **Composite**                 Represents a group of objects (`Company`)
                                and manages child components.

  **Goal**                      Treat both single and group objects the
                                same way.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 🧠 Summary

The Composite pattern helps manage complex object structures easily.\
It's widely used when your system involves **hierarchical relationships** --- such as companies, file explorers, or nested UI layouts.

With this approach, your code becomes **more flexible, scalable, and easier to maintain**.
