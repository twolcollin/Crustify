import clang.cindex
import os
from Crustify.rule_manager import load_rules
from Crustify.rules.echo_comment import EchoCommentRule  # ✅ Import EchoCommentRule
from Crustify.config import MINIFY_CODE  # ✅ Import the minification flag

# Set Clang library file path (adjust based on your system)
LIBCLANG_PATH = "C:\\Python310\\Lib\\site-packages\\clang\\native\\libclang.dll"
clang.cindex.Config.set_library_file(LIBCLANG_PATH)

index = clang.cindex.Index.create()

def clean_up_nolint(lines):
    """Removes redundant `// NOLINT` from commented-out lines but keeps it on actual code lines."""
    cleaned_lines = []
    for line in lines:
        stripped_line = line.strip()

        # ✅ Remove `// NOLINT` from commented-out lines
        if stripped_line.startswith("//") and "// NOLINT" in stripped_line:
            line = line.replace("// NOLINT", "").rstrip() + "\n"  # ✅ Remove `// NOLINT`, keep spacing
        
        cleaned_lines.append(line)

    return cleaned_lines

def minify_c_code(lines):
    """Converts C/C++ code into a single line while preserving functionality and keeping comments inside /* */."""
    
    import re
    # Step 1: Convert `//` comments to `/* */`
    converted_lines = []
    for line in lines:
        line = line.rstrip()  # ✅ Remove trailing whitespace

        if "//" in line:
            line = re.sub(r"//(.*)", r"/* \1 */", line)  # ✅ Convert to `/* ... */`
        
        converted_lines.append(line)

    # Step 2: Remove newlines & unnecessary spaces while preserving `/* */` comments
    minified_code = " ".join(converted_lines)  # ✅ Join lines into a single line
    minified_code = re.sub(r"\s+", " ", minified_code)  # ✅ Replace multiple spaces with one

    return [minified_code + "\n"]  # ✅ Return list with a single minified line

def parse_c_file(filename):
    """Parses a C file using libclang and applies all loaded rules correctly."""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File '{filename}' not found.")

    # Load all rules dynamically
    rules = load_rules()

    # Read file contents
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    modified_lines = lines[:]  # ✅ Start with the original file content

    # Apply each rule properly
    for rule in rules:
        if isinstance(rule, EchoCommentRule):  # ✅ Apply EchoCommentRule to the entire file
            modified_lines = rule.apply(modified_lines)
        else:  # ✅ Apply other rules line by line
            modified_lines = [rule.apply(line) for line in modified_lines]

    # 🧹 Remove unnecessary `// NOLINT` from commented-out lines
    modified_lines = clean_up_nolint(modified_lines)

    # 🏆 ✅ Minify as the last step, but only if enabled in config
    if MINIFY_CODE:
        modified_lines = minify_c_code(modified_lines)

    # Write back the modified file
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(modified_lines)

    print(f"Modified {filename} with {len(rules)} rules. Minification: {'ON' if MINIFY_CODE else 'OFF'}")
