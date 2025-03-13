import random
import re
from Crustify.rules.base import LintRule
from Crustify.config import INDENTATION_IGNORE_TOOL

class IndentationRule(LintRule):
    """Randomly switches between tabs and spaces while ensuring ignore comments are placed correctly without adding newlines."""

    def apply(self, line):
        """Modify indentation but ensure newlines and ignore comments are placed correctly."""
        if not line.strip():  # Don't modify empty lines
            return line

        if random.random() < self.chaos_level:
            indentation_type = random.choice(["tabs", "spaces"])

            # Preserve the newline at the end of the line
            newline = "\n" if line.endswith("\n") else ""

            # Apply random indentation (tabs or spaces)
            if indentation_type == "tabs":
                line = "\t" * random.randint(1, 3) + line.lstrip()
            else:
                line = " " * random.randint(1, 8) + line.lstrip()

            # Ensure comments are added correctly at the end of the statement
            line = self.add_ignore_comment(line)

            # Re-append the preserved newline (no new ones added)
            return line.rstrip() + newline  

        return line

    def add_ignore_comment(self, line):
        """Ensures `// NOLINT` is always placed at the correct end of the statement without adding extra newlines."""
        if not INDENTATION_IGNORE_TOOL:
            return line  # No ignore comment needed

        ignore_comment = {
            "clang-tidy": "// NOLINT",
            "uncrustify": "// uncrustify:off"
        }.get(INDENTATION_IGNORE_TOOL, "")

        if not ignore_comment or ignore_comment in line:
            return line  # Skip if already commented

        # Ensure ignore comments are only added to actual code
        if not re.search(r'\w', line):
            return line  # Skip purely whitespace lines

        # Make sure semicolons appear before comments, but keep everything on one line
        if ";" in line:
            line = re.sub(r";\s*(//.*)?$", f"; {ignore_comment}", line)  # Append comment after semicolon
        else:
            line = f"{line.rstrip()} {ignore_comment}"

        return line
