#!/usr/bin/env python3
"""
Add a short Complexity and Explanation comment above Python functions that don't already have one.

This is intentionally conservative:
 - It will NOT overwrite existing '# Complexity:' comments.
 - It uses simple AST-based heuristics (loop nesting, presence of sorted/sort, recursion, comprehensions).
 - It's meant to be run by pre-commit with staged files as arguments.
"""

import ast
import sys
from pathlib import Path

def max_loop_nesting(node):
    """Return max loop nesting depth inside node."""
    max_depth = 0
    def visit(n, depth=0):
        nonlocal max_depth
        if isinstance(n, (ast.For, ast.While)):
            depth += 1
            max_depth = max(max_depth, depth)
        for child in ast.iter_child_nodes(n):
            visit(child, depth)
    visit(node, 0)
    return max_depth

def contains_sorted_or_sort(node):
    for n in ast.walk(node):
        if isinstance(n, ast.Call):
            # call to sorted(...) or .sort()
            if isinstance(n.func, ast.Name) and n.func.id == "sorted":
                return True
            if isinstance(n.func, ast.Attribute) and n.func.attr == "sort":
                return True
    return False

def contains_list_duplication(node):
    # look for list(slice) or comprehensions that create new lists
    for n in ast.walk(node):
        if isinstance(n, (ast.ListComp, ast.List)):
            return True
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "list":
            return True
    return False

def contains_recursive_call(func_def):
    name = getattr(func_def, "name", None)
    if not name:
        return False
    for n in ast.walk(func_def):
        if isinstance(n, ast.Call):
            if isinstance(n.func, ast.Name) and n.func.id == name:
                return True
            if isinstance(n.func, ast.Attribute) and isinstance(n.func.value, ast.Name) and n.func.attr == name:
                # method calling itself (less precise)
                return True
    return False

def estimate_complexity(func_def):
    loops = max_loop_nesting(func_def)
    uses_sort = contains_sorted_or_sort(func_def)
    duplicates = contains_list_duplication(func_def)
    recursive = contains_recursive_call(func_def)

    # Time complexity heuristic
    if uses_sort:
        time = "O(n log n)"
        reason = "uses sorted()/list.sort() which is O(n log n)"
    elif recursive:
        time = "O(n) (recursive — heuristic)"
        reason = "contains recursive calls (heuristic: treat as O(n))"
    elif loops == 0:
        time = "O(1)"
        reason = "no loops or recursion found"
    elif loops == 1:
        time = "O(n)"
        reason = "one loop found"
    else:
        time = f"O(n^{loops})"
        reason = f"{loops} nested loops found -> O(n^{loops})"

    # Space heuristic
    if duplicates:
        space = "O(n)"
        sreason = "creates new lists/comprehensions"
    else:
        space = "O(1)"
        sreason = "no obvious large temporary structures"

    return time, space, reason, sreason

def already_has_complexity_comment(lines, def_lineno):
    # check up to 3 lines above def for a Complexity: marker
    start = max(0, def_lineno-4)
    for i in range(start, def_lineno-1):
        if i < 0 or i >= len(lines):
            continue
        if "Complexity:" in lines[i] or "# Complexity" in lines[i]:
            return True
    return False

def process_file(path: Path):
    src = path.read_text(encoding="utf8")
    try:
        tree = ast.parse(src)
    except Exception:
        # If parse fails, skip file to avoid corrupting code
        return False, f"PARSE_ERROR: {path}"
    lines = src.splitlines()
    insertions = []  # tuples (insert_at_line_index, text_to_insert)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            def_lineno = node.lineno  # 1-based
            if already_has_complexity_comment(lines, def_lineno):
                continue
            time, space, reason, sreason = estimate_complexity(node)
            comment_lines = [
                f"# Complexity: Time {time}, Space {space}",
                f"# Explanation: {reason}; {sreason}"
            ]
            # insert before the def line (convert to 0-based index)
            insert_at = def_lineno - 1
            insertions.append((insert_at, "\n".join(comment_lines)))
    if not insertions:
        return False, "NO_CHANGES"
    # Apply insertions from bottom to top (so indexes remain valid)
    new_lines = list(lines)
    for idx, text in sorted(insertions, key=lambda x: x[0], reverse=True):
        new_lines[idx:idx] = [text]
    new_src = "\n".join(new_lines) + ("\n" if not new_lines[-1].endswith("\n") else "")
    path.write_text(new_src, encoding="utf8")
    return True, f"UPDATED: {path}"

def main():
    changed_any = False
    results = []
    # pre-commit gives file paths as args; if none, scan repo for .py files
    paths = [Path(p) for p in sys.argv[1:]] if len(sys.argv) > 1 else list(Path(".").rglob("*.py"))
    for p in paths:
        if not p.exists(): continue
        ok, msg = process_file(p)
        if ok:
            changed_any = True
        results.append(msg)
    # Print minimal output for pre-commit logs
    for r in results:
        print(r)
    # If we modified files, fail so pre-commit shows the changes and stops the commit.
    # User will need to 'git add' the modified files and re-run commit.
    return 1 if changed_any else 0

if __name__ == "__main__":
    sys.exit(main())
