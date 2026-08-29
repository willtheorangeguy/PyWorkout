"""Initialize PyPI Package"""

# pylint: disable=invalid-name, import-error

try:
    from main import workout
    from cli import main
except ImportError:
    from .main import workout
    from .cli import main

__all__ = ["workout", "main"]
