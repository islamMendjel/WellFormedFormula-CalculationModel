import os
import re
import shutil
from graphviz import Digraph


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# =============================
# 1. Formula normalization
# =============================
def normalize(expr: str) -> str:
    """ --> Remove spaces and replace the connectors """
    expr = expr.replace(" ", "")
    expr = expr.replace("∨", "|").replace("∧", "&").replace("¬", "~")
    if not re.fullmatch(r"[A-Z|&~()]*", expr):
        raise ValueError(f"formule logique non bien formée: {expr}")
    return expr


# =============================
# 2. Recursive parser  (FIXED)
# =============================
def build_tree(expr: str) -> Node:
    expr = normalize(expr)

    # Remove outer parentheses if they enclose the entire expression
    if expr.startswith("(") and expr.endswith(")"):
        level = 0
        for i, ch in enumerate(expr):
            if ch == "(":
                level += 1
            elif ch == ")":
                level -= 1
            # if we close parentheses before the end, they don't enclose whole expr
            if level == 0 and i < len(expr) - 1:
                break
        else:
            expr = expr[1:-1]

    # ----- IMPORTANT FIXED ORDER -----
    # 1) Try to find a top-level binary operator first (& or |)
    level = 0
    for i in range(len(expr) - 1, -1, -1):  # scan right-to-left
        ch = expr[i]
        if ch == ")":
            level += 1
        elif ch == "(":
            level -= 1
        elif level == 0 and ch in ("|", "&"):
            left = build_tree(expr[:i])
            right = build_tree(expr[i + 1:])
            return Node(ch, left, right)

    # 2) If no top-level binary operator found, handle unary ~
    if expr.startswith("~"):
        # unary NOT stored in left child (right remains None)
        return Node("~", build_tree(expr[1:]))

    # 3) Finally, the base case: single atomic variable
    if len(expr) == 1 and expr.isalpha() and expr.isupper():
        return Node(expr)

    # If none matched, it's invalid
    raise ValueError(f"Invalid formula: {expr}")


# =============================
# 3. Well-formed checker
# =============================
def is_well_formed(node: Node) -> bool:
    if node is None:
        return False

    v = node.value

    if v.isalpha():
        return node.left is None and node.right is None

    if v == "~":
        return node.left is not None and node.right is None and is_well_formed(node.left)

    if v in ("&", "|"):
        return (
            node.left is not None and node.right is not None
            and is_well_formed(node.left)
            and is_well_formed(node.right)
        )

    return False

# def display_tree(node: Node, level=0):
#    """Print the formula tree recursively with indentation."""
#    if node is not None:
#        print("  " * level + str(node.value))
#        display_tree(node.left, level + 1)
#        display_tree(node.right, level + 1)


# =============================
# 4. Graphviz drawing
# =============================
def draw_tree(node: Node, filename="logical_tree"):
    """Draws the logical formula tree as a PNG image."""
    if not shutil.which("dot"):
        print("⚠️ Graphviz not found. Install it from: https://graphviz.org/download/")
        return

    dot = Digraph(comment="Logical Formula Tree", format="png")
    _add_nodes(dot, node)
    output_dir = os.path.abspath(".")
    file_path = os.path.join(output_dir, filename)

    try:
        path = dot.render(file_path, cleanup=True)
        print(f"🖼️  Tree image saved as: {path}")
    except Exception as e:
        print(f"❌ Error generating tree: {e}")


def _add_nodes(dot: Digraph, node: Node, parent_id=None, counter=[0]):
    """Recursive helper to add nodes and edges."""
    if node is None:
        return

    counter[0] += 1
    node_id = str(counter[0])
    dot.node(node_id, node.value)

    if parent_id:
        dot.edge(parent_id, node_id)

    if node.left:
        _add_nodes(dot, node.left, node_id, counter)
    if node.right:
        _add_nodes(dot, node.right, node_id, counter)


# =============================
# 5. Test section
# =============================
# if __name__ == "__main__":
#     formulas = [
#         "A",
#         "~A",
#         "A&B",
#         "~A&(B)",
#         "A|B&C|D",
#         "(A|B)&(~C|D)",
#         "(A∨B)∧(¬C∨D)",  # Unicode-friendly
#         "A&",
#         "~(A|)",
#         # specifically test the edge case the bug caused:
#         "~C|D",
#         "(~C|D)",
#         "(A|B)&(C|D)&(E|F)&(G|H)&(I|J)&(K|L)&(M|N)&(O|P)&(Q|R)&(S|T)&(U|V)&(W|X)&(Y|Z)",
#         "((~C&D)|(~E&F))&((G&~H)|(I&~J))",
#         "((~C&D)|(~E&F))&",
#         "(A|~B)&(~C|D)",
#         "(A&B)|~C"
#     ]

#     for f in formulas:
#         print(f"\nFormula: {f}")
#         try:
#             tree = build_tree(f)
#             if is_well_formed(tree):
#                 print("✅ Well-formed. Drawing tree...")
#                 safe_name = (
#                     f.replace("~", "not_")
#                      .replace("|", "or_")
#                      .replace("&", "and_")
#                      .replace("∨", "or_")
#                      .replace("∧", "and_")
#                      .replace("¬", "not_")
#                      .replace("(", "")
#                      .replace(")", "")
#                 )
#                 draw_tree(tree, filename=safe_name[:80])
#             else:
#                 print("❌ Not well-formed.")
#         except Exception as e:
#             print("❌ Error:", e)


# ================================
# 6. Read inputs from user section
# ================================
if __name__ == "__main__":
    print("=== Logic Formula Parser ===")
    print("Enter a logic formula (ex: (A∨B)∧(¬C∨D))")
    user_formula = input("→ Formula : ").strip()

    if not user_formula:
        print("❌ No Formula has been entred.")
    else:
        try:
            tree = build_tree(user_formula)
            if is_well_formed(tree):
                print("✅ Well-formed. Drawing tree...")
                safe_name = (
                    user_formula.replace("~", "not_")
                                .replace("|", "or_")
                                .replace("&", "and_")
                                .replace("∨", "or_")
                                .replace("∧", "and_")
                                .replace("¬", "not_")
                                .replace("(", "")
                                .replace(")", "")
                )
                draw_tree(tree, filename=safe_name[:80])
            else:
                print("❌ Not well-formed.")
        except Exception as e:
            print(f"❌ Error: {e}")
