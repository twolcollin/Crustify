import random
from Crustify.rules.base import LintRule

class IndentationRule(LintRule):
    """Randomly switches between tabs and spaces while keeping ignore comments correctly placed."""

    def apply(self, line):
        """Modify indentation but ensure newlines and ignore comments are placed correctly."""
        if random.random() < self.chaos_level:
            from Crustify.config import INDENTATION_IGNORE_TOOL  # ✅ Move import here to avoid circular import issues

            indentation_type = random.choice(["tabs", "spaces"])
            newline = "\n" if line.endswith("\n") else ""

            if indentation_type == "tabs":
                line = "\t" * random.randint(1, 3) + line.lstrip()
            else:
                line = " " * random.randint(1, 8) + line.lstrip()

            # Ensure ignore comments are correctly positioned
            line = self.add_ignore_comment(line, INDENTATION_IGNORE_TOOL)

            return line + newline

        return line

    def add_ignore_comment(self, line, ignore_tool):
        """Ensures Clang-Tidy or Uncrustify ignore comments are placed correctly."""
        if not ignore_tool:
            return line  # No ignore comment needed

        ignore_comment = {
            "clang-tidy": "// NOLINT",
            "uncrustify": "// uncrustify:off"
        }.get(ignore_tool, "")

        if ignore_comment in line:
            return line  # Don't duplicate ignore comments

        return f"{line.rstrip()} {ignore_comment}"
