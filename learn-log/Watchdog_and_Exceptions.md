# Day 4: Watchdog, File Automation & Exception Handling

Today marked a big shift in direction — I finally explored the tools that are essential for building my first project: a file automation system using Python.

---

## 👁️ Watchdog & File Monitoring

I learned how the `watchdog` library allows Python to monitor folders in real-time. I now understand the core concepts of:

- Creating a custom handler class that responds to file system events
- Using an observer to track changes in a specific directory
- Monitoring file creation and reacting to it immediately
- The concept of `recursive` watching to include subfolders

This was the first time I felt like I was writing something *reactive* — Python wasn't just processing logic; it was waiting, listening, and acting on its own.

---

## 📁 File Moving & shutil Module

To complement `watchdog`, I explored the `shutil` module to:

- Move files from one folder to another
- Dynamically detect the filename and construct destination paths
- Learn the `shutil.move()` for portability

This part gave me real insight into file automation workflows and how things actually work in real applications.

---

## ⚠️ Exception Handling

I also spent time learning Python’s exception handling — something I had skipped over before but realized is *critical* for writing safe, stable code.

Key takeaways:

- How `try`, `except`, and `finally` blocks work
- Different exception types like `FileNotFoundError`, `PermissionError`, `ValueError`, and how to catch them
- Why exception handling makes scripts cleaner, prevents crashes, and improves user experience
- Used `KeyboardInterrupt` to gracefully exit long-running loops (e.g., for `watchdog` observers)

Learning this made me feel more prepared to write code that won’t break on unexpected input.

---

## 🧠 Reflections

It was a dense day with a lot of interconnected concepts. At times it felt overwhelming, especially with so many new built-in functions and modules to take in — but I now see how close I am to building my first mini-project. The foundation is almost set.

---

## 🔗 Sources

- [Exception Handling – Bro Code](https://www.youtube.com/watch?v=V_NXT2-QIlE)  
- [File Automation using Watchdog – Internet Made Coder](https://www.youtube.com/watch?v=NCvI-K0Gp90&t=50s)  
- [Git & GitHub Basics – Nick White](https://www.youtube.com/watch?v=mJ-qvsxPHpY)  
- [shutil Module – NeuralNine](https://www.youtube.com/watch?v=sXzezIK0d7c)  
- ChatGPT (for debugging help, corrections, and explanations)

---

With most prerequisites done, I feel ready to begin implementing the actual file-organizer project tomorrow.
