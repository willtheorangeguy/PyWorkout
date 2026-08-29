"""Tests for workout history persistence in history.py."""

from datetime import datetime

import history  # pylint: disable=import-error


def test_load_history_empty_when_absent(tmp_path):
    """No history file yields an empty list."""
    assert history.load_history(str(tmp_path / "history.json")) == []


def test_record_workout_appends_and_roundtrips(tmp_path):
    """record_workout writes a record load_history reads back."""
    path = str(tmp_path / "history.json")
    rec = history.record_workout("abs", 125.6, ["Situps", "Leg Raises"], path=path)

    assert rec["group"] == "abs"
    assert rec["duration_seconds"] == 126
    assert rec["completed"] == ["Situps", "Leg Raises"]

    loaded = history.load_history(path)
    assert len(loaded) == 1
    assert loaded[0]["group"] == "abs"


def test_record_workout_multiple(tmp_path):
    """Successive records accumulate."""
    path = str(tmp_path / "history.json")
    history.record_workout("abs", 60, ["Situps"], path=path)
    history.record_workout("quads", 90, ["Lunges"], path=path)
    assert len(history.load_history(path)) == 2


def test_format_history_empty(tmp_path):
    """An empty history reports a friendly message."""
    msg = history.format_history(str(tmp_path / "history.json"))
    assert "No workouts recorded yet" in msg


def test_format_history_lists_sessions(tmp_path):
    """format_history summarises recorded sessions."""
    path = str(tmp_path / "history.json")
    history.record_workout(
        "abs", 3661, ["Situps"], path=path, when=datetime(2026, 1, 2, 8, 0, 0)
    )
    out = history.format_history(path)
    assert "1 session" in out
    assert "abs" in out
    assert "1:01:01" in out  # 3661s -> H:MM:SS


def test_corrupt_history_returns_empty(tmp_path):
    """A corrupt history file is treated as empty rather than crashing."""
    path = tmp_path / "history.json"
    path.write_text("not json")
    assert history.load_history(str(path)) == []
