import random

# ✅ Enable or disable minification (set to True to enable)
MINIFY_CODE = True  # Change to False to disable minification

# 🎭 Chaos Levels (Probability of applying a rule)
CHAOS_LEVELS = {
    "mild": 0.2,
    "medium": 0.5,
    "extreme": 0.9
}

# 🌪️ Default chaos level
DEFAULT_CHAOS_LEVEL = "medium"

# 🛠️ Available Rules - Toggle On/Off
ENABLED_RULES = {
    "SpacingRule": False,
    "IndentationRule": True,
    "SemicolonRule": False,
    "BracesRule": False,
    "EchoCommentRule": True
}

# 🎛️ Custom Chaos Levels for Individual Rules
CUSTOM_RULE_CHAOS = {
    "SpacingRule": 0.6,
    "IndentationRule": 0.8,
    "SemicolonRule": 0.3,
    "BracesRule": 0.5,
    "EchoCommentRule": 0.5
}

# 🔧 Choose Ignore Comment Type for Indentation Rule
# Options: "clang-tidy", "uncrustify", or None (disable ignore comments)
INDENTATION_IGNORE_TOOL = "clang-tidy"  # ✅ Ensure this variable exists

def is_rule_enabled(rule_name):
    """Check if a rule is enabled in config."""
    return ENABLED_RULES.get(rule_name, True)

def get_rule_chaos_level(rule_name):
    """Retrieve chaos level for a rule, falling back to global level."""
    return CUSTOM_RULE_CHAOS.get(rule_name, CHAOS_LEVELS[DEFAULT_CHAOS_LEVEL])
