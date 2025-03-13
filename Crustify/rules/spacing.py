import random
from Crustify.rules.base import LintRule

class SpacingRule(LintRule):
    """Randomly adds/removes spaces inside function calls and around operators."""

    def apply(self, line):
        if random.random() < self.chaos_level:
            line = line.replace("(", " ( ").replace(")", " ) ")
        if random.random() < self.chaos_level:
            line = line.replace("=", " = ").replace("+", " + ")
        return line
