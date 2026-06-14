# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

PyWorkout is a minimal Python CLI application that guides users through workout sessions by muscle group. Users select a muscle group, then navigate exercises with commands (`list`, `start`, `next`, `skip`, `end`, `stats`, `video`, `help`, `license`, `quit`). The package is distributed on PyPI as `pyworkout` and as a Docker image on `ghcr.io`.

## Common Commands

```bash
# Run the CLI locally
python main.py

# Install in editable mode for development
pip install -e .

# Run all tests
pytest tests/ -v

# Run a single test
pytest tests/test_main.py::TestMuscleGroupSelection::test_abs_selection_by_number -v

# Run tests with coverage report
pytest tests/ --cov=. --cov-report=term-missing

# Lint all Python files
pylint $(git ls-files '*.py')

# Build distributable packages
python -m build
```

## Architecture

The application is almost entirely contained in `main.py` as a single `workout()` function (~600 lines). This is intentional — the project is simple by design.

**State is managed through module-level globals** set inside `workout()`: `select` (chosen muscle group index), `activity_num` (current exercise index), `start` (workout start time), `complete` (list of completed exercises), and `times` (per-exercise durations). Pylint complains about these; the file suppresses those warnings with inline `# pylint: disable=` comments, which is the established pattern for this codebase.

**Workout data** is stored as parallel hardcoded lists at the top of `main.py` — one list of exercise names per muscle group (e.g., `abs`, `quads`) and a corresponding `_count` list of rep counts. Adding a new exercise means appending to both lists in sync.

**Video playback** uses platform detection: `os.startfile()` on Windows, `subprocess` with `open` on macOS, and `xdg-open` on Linux. Video file paths are hardcoded absolute paths in `main.py` (lines 86–94) and must be updated by the user for their local setup.

**`gui.py`** is an incomplete Tkinter GUI frontend — it is not integrated with `main.py` and is not functional. Do not treat it as a reference for current application behavior.

## Testing Conventions

Tests live in `tests/test_main.py` and use `pytest` with `pytest-mock`. All CLI I/O is tested by patching `builtins.input` and `builtins.print` via `@patch` decorators. Test classes map to functional areas:

- `TestWorkoutData` — validates the parallel data list structure
- `TestMuscleGroupSelection` — number and name-based group selection, invalid inputs
- `TestWorkoutCommands` — each CLI command in isolation
- `TestWorkoutFlow` — multi-step exercise sequences
- `TestVideoFunctionality` — cross-platform video path dispatch
- `TestIntegration` — full end-to-end scenarios

Pytest configuration (in `setup.cfg`) auto-enables branch coverage and `--strict-markers`. Available markers: `@pytest.mark.slow`, `@pytest.mark.integration`.

## CI/CD

Five GitHub Actions workflows run automatically:

| Workflow | Trigger | What it does |
|---|---|---|
| `tests.yml` | Push/PR to main or develop | pytest on Python 3.9–3.12, uploads coverage |
| `pylint.yml` | Every push | Pylint check on Python 3.9 |
| `docker-publish.yml` | Push to main, tags, PRs, daily | Build + push Docker image to ghcr.io |
| `push-to-pypi.yml` | Release published | Build + publish to PyPI |
| `codeql-analysis.yml` | Push, PRs, schedule | Security scanning |

## Conventions

- **Pylint suppressions**: Use inline `# pylint: disable=<rule>` for violations that are intentional given the single-function architecture. Do not add a `.pylintrc` file.
- **Versioning**: Semantic versioning (e.g., `v1.2.0`). Version is defined in `setup.cfg` and `pyproject.toml`.
- **Comments**: The codebase uses heavy inline comments per `CONTRIBUTING.md` — follow the same style when modifying `main.py`.
- **No external runtime dependencies**: The CLI relies only on the Python standard library. Keep it that way.
