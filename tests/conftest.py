"""Shared pytest fixtures for PyWorkout."""

import sys
import os

import pytest  # pylint: disable=import-error

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import config  # pylint: disable=import-error,wrong-import-position


@pytest.fixture(autouse=True)
def isolated_home(tmp_path, monkeypatch):
    """
    Redirect the PyWorkout config/history directory into a temp folder so tests
    never read or write the real ``~/.pyworkout/``.
    """
    target = tmp_path / ".pyworkout"
    monkeypatch.setattr(config, "config_dir", lambda: str(target))
    return target
