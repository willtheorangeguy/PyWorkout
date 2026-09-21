"""This is the main file for the workout app."""

# pylint: disable=invalid-name, import-error

try:
    from cli import main
except ImportError:
    from .cli import main

if __name__ == "__main__":
    main()
