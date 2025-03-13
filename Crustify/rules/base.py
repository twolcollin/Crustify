class LintRule:
    """Base class for all lint rules."""

    def __init__(self, chaos_level=0.5):
        self.chaos_level = chaos_level  # Determines probability of applying rule

    def apply(self, line):
        """Apply the rule to a line of code (to be overridden in subclasses)."""
        raise NotImplementedError("Each rule must implement the apply() method.")
