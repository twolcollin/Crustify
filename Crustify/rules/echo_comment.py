import random
from Crustify.rules.base import LintRule
from Crustify.config import get_rule_chaos_level, is_rule_enabled

class EchoCommentRule(LintRule):
    """Randomly inserts a comment exactly one line above its target while keeping everything else unchanged."""

    def __init__(self):
        self.chaos_level = get_rule_chaos_level("EchoCommentRule")

    def apply(self, lines):
        """Processes the file in reverse order to ensure correct placement of comments without modifying behavior."""
        if not is_rule_enabled("EchoCommentRule"):
            return lines  # ✅ If disabled, return unchanged lines

        modified_lines = list(lines)  # ✅ Copy list to avoid modifying while iterating

        for i in range(len(modified_lines) - 1, 0, -1):  # 🔄 Iterate bottom-up to ensure precise insertion
            next_line = modified_lines[i]

            # ✅ Ensure we only comment real code lines (not existing comments)
            if next_line.strip() and not next_line.lstrip().startswith(("//", "#")):
                if "NOLINT" not in next_line and random.random() < self.chaos_level:
                    leading_spaces = len(next_line) - len(next_line.lstrip())  # ✅ Preserve indentation
                    comment = f"{' ' * leading_spaces}// {next_line.strip()}\n"
                    modified_lines.insert(i, comment)  # ✅ Insert comment exactly one line above

        return modified_lines
