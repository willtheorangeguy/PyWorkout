"""
PyWorkout workout history.

Persists completed workouts to ``~/.pyworkout/history.json`` so users can see
past sessions and totals across runs. Each record is a small JSON object; the
file is a JSON list of those records.
"""

import json
import os
from datetime import datetime

try:
    import config as config_mod
except ImportError:  # installed as part of the package
    from . import config as config_mod

HISTORY_FILE_NAME = "history.json"


def default_history_path():
    """Return the default path to ``history.json``."""
    return os.path.join(config_mod.config_dir(), HISTORY_FILE_NAME)


def load_history(path=None):
    """Return the list of workout records, or [] when absent/unreadable."""
    if path is None:
        path = default_history_path()
    if not os.path.exists(path):
        return []
    try:
        with open(path, encoding="UTF-8") as handle:
            data = json.load(handle)
    except (json.JSONDecodeError, OSError):
        return []
    return data if isinstance(data, list) else []


def record_workout(group, duration_seconds, completed, path=None, when=None):
    """
    Append one completed-workout record and return it.

    ``duration_seconds`` is rounded to an int; ``completed`` is the list of
    activity names finished. ``when`` defaults to now (ISO 8601).
    """
    if path is None:
        path = default_history_path()
    if when is None:
        when = datetime.now()

    record = {
        "date": when.isoformat(timespec="seconds"),
        "group": group,
        "duration_seconds": int(round(duration_seconds)),
        "completed": list(completed),
    }

    records = load_history(path)
    records.append(record)

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="UTF-8") as handle:
        json.dump(records, handle, indent=2)
    return record


def _format_duration(seconds):
    """Render seconds as H:MM:SS."""
    seconds = int(seconds)
    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours}:{minutes:02d}:{secs:02d}"


def format_history(path=None):
    """Return a human-readable multi-line summary of past workouts."""
    records = load_history(path)
    if not records:
        return "No workouts recorded yet. Complete one with the `end` command!"

    lines = [f"Workout history ({len(records)} session(s)):"]
    for i, rec in enumerate(records, start=1):
        date = rec.get("date", "?")
        group = rec.get("group", "?")
        duration = _format_duration(rec.get("duration_seconds", 0))
        count = len(rec.get("completed", []))
        lines.append(
            f"{i}. {date}\t{group}\t{duration}\t({count} activities)"
        )
    return "\n".join(lines)
