# Factory Design Pattern in Python

## 📌 What is the Factory Design Pattern?

The **Factory Method Pattern** is a **creational design pattern** that provides an interface for creating objects in a **superclass**, but allows **subclasses or factories** to decide which class to instantiate.

In simple words:
- Instead of creating objects directly with `Car()`, `Bike()`, or `Truck()`,  
- You ask a **Factory** to create them for you.  
- This decouples object **creation** from object **usage**.

---

## 🤔 Why is it Needed?

- **Encapsulation of object creation**  
  You don’t expose the logic of how objects are created. Clients just use the factory.
  
- **Loose coupling**  
  The client code only depends on an interface (`Vehicle`) instead of concrete classes (`Car`, `Bike`, `Truck`).

- **Flexibility for extension**  
  New products (like `Bus`) can be added **without changing existing client code**. You just register them in the factory.

- **Cleaner code**  
  Complex initialization logic is moved to the factory, keeping client code simple.

---

## 🔎 How the Example Works

1. **`Vehicle` interface**  
   Defines a common contract (`drive()`) that all vehicles must implement.

2. **Concrete classes** (`Car`, `Bike`, `Truck`)  
   Each implements `Vehicle` differently:
   - `Car` → has seats  
   - `Bike` → may or may not have gears  
   - `Truck` → carries load  

3. **`VehicleFactory`**  
   - Maintains a dictionary of registered creators (`car`, `bike`, `truck`).  
   - The `create()` method looks up the right constructor and calls it with any passed arguments.

4. **Client code (`main`)**  
   - Registers vehicle types once.  
   - Requests new objects with `factory.create("car", seats=5)` instead of directly calling `Car(seats=5)`.

---

## ✅ Benefits Demonstrated

- You can **add a new vehicle type** (e.g., `Bus`) without changing existing code, just by:
  ```python
  factory.register("bus", Bus)
  ```
- The client does not care **which concrete class** is returned — it just calls `drive()`.

---

## 🚀 Conclusion

The **Factory Design Pattern** is useful when:
- You want to decouple object creation from usage.
- Your code should remain flexible to add new types of objects.
- You want to centralize object creation logic in one place.

This makes your code **more maintainable, extensible, and testable**.
