import importlib
import pkgutil
from Crustify.rules.base import LintRule
from Crustify.config import is_rule_enabled, get_rule_chaos_level

def load_rules():
    """Dynamically load only enabled lint rules from the `rules` directory."""
    rules = []
    package = "Crustify.rules"

    for _, module_name, _ in pkgutil.iter_modules([package.replace(".", "/")]):
        module = importlib.import_module(f"{package}.{module_name}")

        for obj in module.__dict__.values():
            if isinstance(obj, type) and issubclass(obj, LintRule) and obj is not LintRule:
                if is_rule_enabled(obj.__name__):  # ✅ Only load rules that are enabled in ENABLED_RULES
                    if obj.__name__ in ["EchoCommentRule", "MisspelledMacrosRule"]:
                        rules.append(obj())  # ✅ These rules take no extra arguments
                    else:
                        chaos_level = get_rule_chaos_level(obj.__name__)  # 🎭 Get rule-specific chaos level
                        rules.append(obj(chaos_level))  # ✅ Instantiate rule with correct chaos level

    return rules
