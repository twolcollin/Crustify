import random

# 🎭 Chaos Levels (Probability of applying a rule)
CHAOS_LEVELS = {
    "mild": 0.2,      # 20% chance of modifying lines
    "medium": 0.5,    # 50% chance
    "extreme": 0.9    # 90% chance
}

# 🌪️ Default chaos level
DEFAULT_CHAOS_LEVEL = "medium"

# 🛠️ Available Rules - Toggle On/Off
ENABLED_RULES = {
    "SpacingRule": False,
    "IndentationRule": True,
    "SemicolonRule": False,
    "BracesRule": False  # Disabled by default
}

# 🎛️ Custom Chaos Levels for Individual Rules
CUSTOM_RULE_CHAOS = {
    "SpacingRule": 0.6,
    "IndentationRule": 0.8,
    "SemicolonRule": 0.3,
    "BracesRule": 0.5
}

# 🔧 Choose Ignore Comment Type for Indentation Rule
# Options: "clang-tidy", "uncrustify", or None (disable ignore comments)
INDENTATION_IGNORE_TOOL = "clang-tidy"  # Change to "uncrustify" or None

def is_rule_enabled(rule_name):
    """Check if a rule is enabled in config."""
    return ENABLED_RULES.get(rule_name, True)

def get_rule_chaos_level(rule_name):
    """Retrieve chaos level for a rule, falling back to global level."""
    return CUSTOM_RULE_CHAOS.get(rule_name, CHAOS_LEVELS[DEFAULT_CHAOS_LEVEL])

def get_random_chaos_level():
    """Returns a random chaos level for more unpredictable behavior."""
    return random.choice(list(CHAOS_LEVELS.keys()))
