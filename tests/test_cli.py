"""Tests for the argparse CLI wrapper in cli.py."""

# Flat-layout module names can be shadowed by site-packages during pylint's
# static resolution; disable no-member for this test module.
# pylint: disable=no-member

from unittest.mock import patch

import pytest  # pylint: disable=import-error

import cli  # pylint: disable=import-error


def test_parse_args_defaults():
    """No flags -> all options at their defaults."""
    args = cli.parse_args([])
    assert args.group is None
    assert args.list is None
    assert args.history is False
    assert args.init_config is False
    assert args.config is None


def test_parse_args_group():
    """--group captures the group name."""
    assert cli.parse_args(["--group", "abs"]).group == "abs"
    assert cli.parse_args(["-g", "quads"]).group == "quads"


def test_parse_args_list_optional_value():
    """--list works with and without a group argument."""
    assert cli.parse_args(["--list"]).list == "__ALL__"
    assert cli.parse_args(["--list", "abs"]).list == "abs"


def test_version_exits(capsys):
    """--version prints and exits 0."""
    with pytest.raises(SystemExit) as exc:
        cli.parse_args(["--version"])
    assert exc.value.code == 0
    assert "pyworkout" in capsys.readouterr().out


def test_no_args_launches_repl():
    """With no flags, main() dispatches to the interactive workout()."""
    with patch.object(cli, "workout") as mock_workout:
        assert cli.main([]) == 0
        mock_workout.assert_called_once_with(preselect=None, config_path=None)


def test_group_flag_preselects():
    """--group is threaded into workout()."""
    with patch.object(cli, "workout") as mock_workout:
        cli.main(["--group", "abs"])
        mock_workout.assert_called_once_with(preselect="abs", config_path=None)


def test_list_all(capsys):
    """--list prints every group."""
    assert cli.main(["--list"]) == 0
    out = capsys.readouterr().out
    assert "Abs:" in out
    assert "Chest:" in out
    assert "Situps" in out


def test_list_one_group(capsys):
    """--list GROUP prints just that group."""
    assert cli.main(["--list", "abs"]) == 0
    out = capsys.readouterr().out
    assert "Abs:" in out
    assert "Chest:" not in out


def test_list_unknown_group(capsys):
    """--list with a bad group reports an error and returns non-zero."""
    assert cli.main(["--list", "nope"]) == 1
    assert "Unknown group" in capsys.readouterr().out


def test_history_flag(capsys):
    """--history prints the (empty) history and returns 0."""
    assert cli.main(["--history"]) == 0
    assert "No workouts recorded yet" in capsys.readouterr().out


def test_init_config_writes_file(tmp_path, capsys):
    """--init-config writes a config file at the given path."""
    path = str(tmp_path / "config.json")
    assert cli.main(["--init-config", "--config", path]) == 0
    out = capsys.readouterr().out
    assert "Wrote default config" in out
    import os  # pylint: disable=import-outside-toplevel

    assert os.path.exists(path)
