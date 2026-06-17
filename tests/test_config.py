"""Tests for the user-config loading and merging in config.py."""

import json
import os

import config  # pylint: disable=import-error


def test_defaults_when_no_file(tmp_path):
    """Missing config file falls back to built-in defaults."""
    workouts = config.load_config(str(tmp_path / "missing.json"))
    assert workouts["abs"]["display"] == "Ab"
    assert workouts["abs"]["exercises"][0] == ["Situps", 25] or workouts["abs"][
        "exercises"
    ][0] == ("Situps", 25)


def test_deep_merge_overrides_one_group(tmp_path):
    """A config overriding one field leaves every other group/field intact."""
    path = tmp_path / "config.json"
    path.write_text(json.dumps({"abs": {"video": "/movies/abs.mp4"}}))

    workouts = config.load_config(str(path))
    # Override applied.
    assert workouts["abs"]["video"] == "/movies/abs.mp4"
    # Untouched data preserved.
    assert workouts["abs"]["display"] == "Ab"
    assert workouts["quads"]["display"] == "Quad"


def test_bad_json_falls_back(tmp_path, capsys):
    """Malformed JSON warns once and returns defaults."""
    path = tmp_path / "config.json"
    path.write_text("{not valid json")

    workouts = config.load_config(str(path))
    assert workouts["chest"]["display"] == "Chest"
    assert "Warning" in capsys.readouterr().out


def test_non_object_falls_back(tmp_path, capsys):
    """A JSON file that isn't an object returns defaults."""
    path = tmp_path / "config.json"
    path.write_text("[1, 2, 3]")

    workouts = config.load_config(str(path))
    assert "abs" in workouts
    assert "Warning" in capsys.readouterr().out


def test_write_default_config_roundtrips(tmp_path):
    """write_default_config produces a file load_config can read back."""
    path = str(tmp_path / "nested" / "config.json")
    written = config.write_default_config(path)
    assert os.path.exists(written)

    workouts = config.load_config(path)
    assert set(workouts) == set(config.default_workouts())


def test_group_order_appends_custom_groups():
    """User-added groups appear after the canonical ones, sorted."""
    workouts = config.default_workouts()
    workouts["zumba"] = {"display": "Zumba", "video": "", "exercises": []}
    workouts["cardio"] = {"display": "Cardio", "video": "", "exercises": []}
    order = config.group_order(workouts)
    assert order[:7] == config.GROUP_ORDER
    assert order[7:] == ["cardio", "zumba"]
