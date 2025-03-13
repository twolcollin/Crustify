import argparse
from Crustify.injector import inject_lint

def main():
    parser = argparse.ArgumentParser(description="Inject random lint into C/C++ files")
    parser.add_argument("file", help="Path to the C/C++ file")
    parser.add_argument(
        "--chaos",
        choices=["mild", "medium", "extreme"],
        default="medium",
        help="Set chaos level for lint injection",
    )
    args = parser.parse_args()

    inject_lint(args.file, args.chaos)

if __name__ == "__main__":
    main()
