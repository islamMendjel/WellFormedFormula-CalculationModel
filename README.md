# 🧠 WFF = Well Formed Formula

### 📘 Description

This project implements a **recursive logical formula parser and visualizer**.  
It takes a logical expression as input — using either **ASCII** operators (`~`, `&`, `|`) or **Unicode** logical symbols (`¬`, `∧`, `∨`) — and performs the following steps:

1. **Normalizes** the expression (removes spaces and converts Unicode symbols).  
2. **Builds a binary tree** that represents the logical structure of the formula.  
3. **Checks recursively** whether the formula is **well-formed** according to logical grammar rules.  
4. **Generates a PNG image** of the logical tree using **Graphviz**.

The goal is to **model and visualize the calculation process of well-formed formulas** in propositional logic using recursion, data structures, and graphical representation.

---

### ⚙️ Example

**Input formula:**
```
(A∨B)∧(¬C∨D)
```

**Normalized:**
```
(A|B)&(~C|D)
```

**Output (tree image):**

```
        &
       / \
      |   |
     / \ / \
    A  B ~  D
        |
        C
```

🖼️ The program produces an image file such as:  
`Aor_Band_not_Cor_D.png`

---

### 🧩 Main Features

- 🔁 **Recursive parser** that converts a formula string into a binary tree.  
- ✅ **Validation** of well-formed formulas:
  - **Atomic proposition** → no children  
  - **Unary NOT (~)** → exactly one child  
  - **Binary operators (&, |)** → exactly two children  
- 🌳 **Graphviz rendering** for automatic logical tree visualization.  
- 🌐 Supports both **ASCII** and **Unicode** logical operators.  

---

### 🧮 Example Supported Inputs

| Input | Accepted | Meaning |
|--------|-----------|----------|
| `A` | ✅ | Atomic proposition |
| `~A` | ✅ | Negation |
| `(A&B)&(~C&D)` | ✅ | Complex logical formula |
| `(A∧B)∧(¬C∧D)` | ✅ | Unicode symbols supported |
| `A&` | ❌ | Invalid formula |

---

### 🛠 Requirements

- **Python 3.8+**  
- **Graphviz** installed and added to your system `PATH`  
  → [Download Graphviz](https://graphviz.org/download/)

**Install Python dependency:**
```
pip install graphviz
```
▶️ Run the Program
```
python WFF.py
```

Formula: (A|B)&(~C|D)
✅ Well-formed. Drawing tree...
🖼️  Tree image saved as: /path/Aor_Band_not_Cor_D.png

### 🧾 Credits

This project was developed as part of the “Well-Formed Formula – Calculation Model” coursework.
It demonstrates:

recursive tree construction,

syntactic validation of logical formulas, and

visualization of propositional logic using Graphviz.
