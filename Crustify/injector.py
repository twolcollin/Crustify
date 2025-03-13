from Crustify.parser import parse_c_file
from Crustify.config import DEFAULT_CHAOS_LEVEL

def inject_lint(filename, chaos_level=DEFAULT_CHAOS_LEVEL):
    """Injects random lint into a C/C++ file."""
    print(f"Injecting random lint into {filename} with chaos level: {chaos_level}")
    parse_c_file(filename)
