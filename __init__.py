"""Initialize PyPI Package"""

# pylint: disable=invalid-name, import-error

try:
    from main import workout
except ImportError:
    from .main import workout

__all__ = ["workout"]
