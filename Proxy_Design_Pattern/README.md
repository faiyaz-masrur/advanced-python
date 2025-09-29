# Proxy Design Pattern in Python

## 📌 What is Proxy Design Pattern?
The **Proxy Design Pattern** is a **structural design pattern** where a `Proxy` object acts as a **substitute** or **placeholder** for another object (called the *Real Subject*).  
The proxy controls access to the real object and can add additional functionality like **logging, caching, lazy loading, or access control**.

In short:
- The **client** interacts with the **proxy**.
- The proxy decides whether (and how) to forward the request to the **real object**.

---

## 🤔 Why Use Proxy Pattern?
- **Lazy Initialization**: Create heavy objects only when they are really needed.
- **Access Control**: Restrict access to sensitive objects (security checks).
- **Logging & Monitoring**: Add logging, caching, or usage tracking without changing the real object.
- **Remote Proxy**: Represent objects in different address spaces (like RPC, web services).

---

## 📍 Where is it Needed?
- When working with **large/heavy objects** (e.g., images, files, database connections).
- When adding **security checks** before accessing resources.
- When we want to add **extra functionality (logging, monitoring, caching)** without modifying the real class.
- Common in frameworks, middleware, and distributed systems.


## 🔍 Explanation of Code
1. **`Image` (Abstract Interface)**  
   - Defines the contract (`display()` method) that both `RealImage` and `ProxyImage` must follow.

2. **`RealImage` (Real Subject)**  
   - The heavy object that loads an image from disk when created.  
   - `_load_from_disk()` simulates expensive I/O.

3. **`ProxyImage` (Proxy)**  
   - Holds a reference to `RealImage` but does not load it immediately.  
   - Only creates `RealImage` when `display()` is called for the first time (**lazy loading**).  
   - Can add **extra functionality** like logging, access control, or monitoring.

4. **Client Code**  
   - Uses `ProxyImage` instead of directly working with `RealImage`.  
   - The client doesn’t know if it’s dealing with a proxy or the real object.

---

## ▶️ Sample Output
```
First call:
Loading image from disk: photo1.png
Displaying image: photo1.png

Second call:
Displaying image: photo1.png

Different image:
Loading image from disk: photo2.png
Displaying image: photo2.png
```

---

## ✅ Benefits
- Better **performance** with lazy loading.
- Cleaner code with **separation of concerns** (proxy handles logging/security, real subject does the core work).
- Flexible — you can **add features without modifying the real class**.

---

## ⚡ Conclusion
The Proxy Design Pattern is a great choice when you want **control over object creation or access**.  
In this example, `ProxyImage` acts as a lightweight placeholder for `RealImage`, ensuring that images are only loaded when necessary.  

This makes applications faster, more secure, and easier to extend.
