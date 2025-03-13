import random
from Crustify.rules.base import LintRule

class SemicolonRule(LintRule):
    """Randomly duplicates or removes semicolons while preserving ignore comment placement."""

    def apply(self, line):
        if ";" in line and random.random() < self.chaos_level:
            semicolon_count = line.count(";")

            if semicolon_count > 1 and random.random() < 0.5:
                # 🔥 Randomly remove a semicolon (but leave at least one)
                line = line.replace(";", "", 1)
            else:
                # 🔥 Randomly duplicate semicolons
                line = line.replace(";", ";;", 1)

        # Ensure ignore comments stay at the end of the line
        if "//" in line:
            code, comment = line.split("//", 1)
            return f"{code.strip()}; //{comment.strip()}"
        else:
            return f"{line.strip()};"
