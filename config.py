"""
PyWorkout user configuration.

A user can override exercises, rep counts, and (most usefully) video paths
without editing source. Config lives at ``~/.pyworkout/config.json`` and is
deep-merged over the built-in defaults in ``data.py`` -- so overriding just one
group's video path leaves every other group untouched.

Missing config -> defaults, silently. Malformed JSON -> defaults, with a single
warning line (this is a hobby tool; never crash on a bad config).
"""

import copy
import json
import os

try:
    from data import WORKOUTS, GROUP_ORDER
except ImportError:  # installed as part of the package
    from .data import WORKOUTS, GROUP_ORDER

CONFIG_DIR_NAME = ".pyworkout"
CONFIG_FILE_NAME = "config.json"


def config_dir():
    """Return the directory holding PyWorkout config and history."""
    return os.path.join(os.path.expanduser("~"), CONFIG_DIR_NAME)


def default_config_path():
    """Return the default path to ``config.json``."""
    return os.path.join(config_dir(), CONFIG_FILE_NAME)


def _deep_merge(base, override):
    """Return a deep copy of ``base`` with ``override`` recursively merged in."""
    result = copy.deepcopy(base)
    for key, value in override.items():
        if (
            key in result
            and isinstance(result[key], dict)
            and isinstance(value, dict)
        ):
            result[key] = _deep_merge(result[key], value)
        else:
            result[key] = copy.deepcopy(value)
    return result


def default_workouts():
    """Return a deep copy of the built-in workout data."""
    return copy.deepcopy(WORKOUTS)


def load_config(path=None):
    """
    Load the merged workout config.

    Reads JSON from ``path`` (defaults to ``default_config_path()``) and
    deep-merges it over the built-in defaults. Returns the defaults unchanged
    when the file is absent or unreadable.
    """
    if path is None:
        path = default_config_path()

    if not os.path.exists(path):
        return default_workouts()

    try:
        with open(path, encoding="UTF-8") as handle:
            user = json.load(handle)
    except (json.JSONDecodeError, OSError) as err:
        print(f"Warning: could not read config at {path} ({err}). Using defaults.")
        return default_workouts()

    if not isinstance(user, dict):
        print(f"Warning: config at {path} is not a JSON object. Using defaults.")
        return default_workouts()

    return _deep_merge(WORKOUTS, user)


def write_default_config(path=None):
    """
    Write the built-in defaults to ``path`` as a starting point users can edit.

    Creates the config directory if needed. Returns the path written.
    """
    if path is None:
        path = default_config_path()

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="UTF-8") as handle:
        json.dump(default_workouts(), handle, indent=2)
    return path


def group_order(workouts=None):
    """
    Return group keys in display order.

    Built-in groups keep their canonical order; any extra groups a user added
    via config are appended in sorted order.
    """
    if workouts is None:
        return list(GROUP_ORDER)
    ordered = [g for g in GROUP_ORDER if g in workouts]
    extra = sorted(k for k in workouts if k not in GROUP_ORDER)
    return ordered + extra
