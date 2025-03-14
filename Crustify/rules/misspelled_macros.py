import random
import re
from Crustify.rules.base import LintRule
from Crustify.config import get_rule_chaos_level, is_rule_enabled

class MisspelledMacrosRule(LintRule):
    """Replaces C/C++ keywords with slightly misspelled macros while keeping the code functional."""

    def __init__(self):
        self.chaos_level = get_rule_chaos_level("MisspelledMacrosRule")

        # ✅ Define misspelled versions of common C/C++ keywords
        self.keyword_map = {
            "int": "ent",
            "return": "rheturn",
            "for": "four",
            "while": "whole",
            "if": "iff",
            "else": "elsE",
            "switch": "schwicht",
            "case": "case",
            "break": "brake",
            "continue": "continu",
            "void": "voyd",
            "char": "charzard",
            "float": "flot",
            "double": "dubble",
            "static": "statik",
            "struct": "strukt",
            "typedef": "typedef"
        }

        # ✅ Compile regex patterns to match full-word keywords
        self.regex_map = {
            original: re.compile(rf'\b{original}\b') for original in self.keyword_map.keys()
        }

    def apply(self, lines):
        """Processes the file, replacing keywords with their misspelled macro equivalents."""
        if not is_rule_enabled("MisspelledMacrosRule"):
            return lines  # ✅ If disabled, return unchanged lines

        modified_lines = []
        for line in lines:
            new_line = line
            for original, macro in self.keyword_map.items():
                if random.random() < self.chaos_level:
                    new_line = self.regex_map[original].sub(macro, new_line)  # ✅ Replace full-word matches only

            modified_lines.append(new_line)

        return modified_lines
