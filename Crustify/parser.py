import clang.cindex
import os
from Crustify.rule_manager import load_rules

# Set Clang library file path for Windows
clang.cindex.Config.set_library_file("C:\\Python310\\Lib\\site-packages\\clang\\native\\libclang.dll")

index = clang.cindex.Index.create()

def parse_c_file(filename):
    """Parses a C file using libclang and applies all loaded rules."""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File '{filename}' not found.")

    # Load all rules dynamically
    rules = load_rules()

    # Read file contents
    with open(filename, "r") as f:
        lines = f.readlines()

    # Apply rules
    modified_lines = []
    for line in lines:
        for rule in rules:
            line = rule.apply(line)
        modified_lines.append(line)

    # Write back the modified file
    with open(filename, "w") as f:
        f.writelines(modified_lines)

    print(f"Modified {filename} with {len(rules)} rules.")
