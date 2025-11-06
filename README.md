# 🧠 WellFormedFormula-CalculationModel

📘 Description

This project implements a recursive logical formula parser and visualizer.
It takes a logical expression as input (using operators ~, &, | or their symbolic forms ¬, ∧, ∨),
then:

Normalizes the expression (removes spaces and converts symbols).

Builds a binary tree that represents the structure of the logical formula.

Checks recursively if the formula is well-formed according to logical grammar rules.

Generates a PNG image of the tree using Graphviz.

The goal is to model the calculation process of well-formed formulas in propositional logic, combining recursion, data structures, and visualization.

⚙️ Example

Input formula:

(A∨B)∧(¬C∨D)


Normalized:

(A|B)&(~C|D)


Output (tree image):

        &
       / \
      |   |
     / \ / \
    A  B ~  D
        |
        C


🖼️ The program produces an image file like:
Aor_Band_not_Cor_D.png

🧩 Main Features

Recursive parser that converts a string formula into a binary tree.

Validation of well-formed formulas:

Atomic proposition → no children

Unary NOT (~) → exactly one child

Binary operators (&, |) → exactly two children

Automatic Graphviz rendering into a clear logical tree.

Supports both ASCII and Unicode logical symbols.

🧮 Example Supported Inputs
Input	Accepted	Meaning
A	✅	Atomic proposition
~A	✅	Negation
`(A	B)&(~C	D)`
(A∨B)∧(¬C∨D)	✅	Unicode symbols supported
A&	❌	Invalid formula

🛠 Requirements

Python 3.8+

Graphviz installed and added to your system PATH
(Download from https://graphviz.org/download/)

Python libraries:

pip install graphviz

▶️ Run the program
python logical_formula_tree.py


It will test a set of predefined formulas and generate PNG images for all well-formed ones.

📂 Output Example
Formula: (A|B)&(~C|D)
✅ Well-formed. Drawing tree...
🖼️ Tree image saved as: /path/Aor_Band_not_Cor_D.png

🧾 Credits

This project was developed as part of the “Well-Formed Formula – Calculation Model” course work.
It demonstrates recursive tree construction, syntactic validation, and logical formula visualization.
