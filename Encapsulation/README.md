# Encapsulation in Python (Advanced Example)

## 🔒 What is Encapsulation?
Encapsulation is one of the core principles of **Object-Oriented Programming (OOP)**.  
It means **bundling data (attributes) and methods (functions) into a class** and **restricting direct access** to the internal state of an object.  

In Python, encapsulation is commonly implemented using:
- **Private attributes** (`__var`) with **name mangling**.
- **Properties (`@property`)** for controlled access.
- **Validation logic** in setters and methods.
- **Static methods** that belong to the class, not an instance.

---

## 📝 Explanation of the Example

- **Private Attributes (`__account_number`, `__balance`)**  
  These cannot be accessed directly. Python internally renames them (e.g., `_BankAccount__balance`), which discourages external tampering.

- **Property: `account_number`**  
  This makes the account number **read-only**. When accessed, it returns a **masked version** (e.g., showing only the last 4 digits).

- **Property with Setter: `balance`**  
  Allows **controlled updates**. Validation ensures the balance cannot be negative.

- **Methods: `deposit` and `withdraw`**  
  Encapsulate business rules:
  - Deposits must be positive.
  - Withdrawals cannot exceed the available balance.

- **Static Method: `bank_policy()`**  
  Demonstrates behavior that **belongs to the class itself**, not tied to any specific account.

- **Bypassing Encapsulation**  
  Directly accessing `acc._BankAccount__balance` works because of name mangling, but this breaks encapsulation principles and should be avoided.

---

## 🚀 Key Takeaways
1. Encapsulation **hides sensitive data** and exposes only what is necessary.  
2. Use **`@property` decorators** to create **read-only or validated access**.  
3. **Static methods** provide general rules or utilities not tied to an instance.  
4. Python’s name mangling (`__var`) is a **soft form of private access**, encouraging best practices but not enforcing them strictly.  
