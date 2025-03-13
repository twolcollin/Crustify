import random
import re

def random_space():
    """Returns random spaces to mess up indentation and formatting."""
    return " " * random.randint(1, 5) if random.random() < 0.5 else ""

def modify_line(line, chaos_prob):
    """Randomly introduces lint issues into a line based on chaos probability."""
    if random.random() < chaos_prob:
        # Add random spaces before or after braces
        line = re.sub(r'(\{|\})', r' \1 ', line)

    if random.random() < chaos_prob:
        # Add extra spaces inside function parentheses
        line = re.sub(r'(\w+)\((.*?)\)', lambda m: f"{m.group(1)}( {m.group(2)} )", line)

    if random.random() < chaos_prob / 2:
        # Randomly duplicate semicolons
        line = re.sub(r';', ';;', line)

    if random.random() < chaos_prob / 3:
        # Insert random blank lines
        line = "\n" + line

    return line
