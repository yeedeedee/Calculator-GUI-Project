# 🧮 Tkinter Calculator

A simple calculator application built using **Python** and **Tkinter**.
This project demonstrates how to build a graphical user interface (GUI) in Python with basic arithmetic operations.

---

## ✨ Features

* Perform basic arithmetic: **Addition (+), Subtraction (-), Multiplication (\*), Division (/)**
* Supports **decimal values**
* **CE (Clear Entry):** deletes the last entered character
* **C (Clear All):** clears the entire expression
* Simple, clean layout with a teal background

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/tkinter-calculator.git
cd tkinter-calculator
```

### 2. Run the script

Make sure you have Python installed (≥3.7). Then run:

```bash
Calculator_GUI.py```

---

## 📂 Project Structure

```
Calculator-GUI-Project/
│
├── Calculator_GUI.py   # Main application file
├── README.md       # Project documentation
```

---

## 📖 How It Works

* The calculator uses a global variable `equation` to store the current expression.
* Button clicks are handled by the `Calculate()` function, which:

  * Appends digits/operators to the equation
  * Evaluates the result with `eval()` when "=" is pressed
  * Clears entries with `C` and `CE`

---

## ⚠️ Notes

* The project uses Python’s built-in `eval()` function to calculate results.

  * This is fine for personal/learning projects, but in production apps, you should replace it with a safer evaluation method.

---

## 🛠️ Technologies Used

* **Python** (3.x)
* **Tkinter** (for GUI)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork the repo and submit a pull request.

---
