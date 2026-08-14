# PyWorkout — Development

## Local Setup

```bash
git clone https://github.com/willtheorangeguy/PyWorkout
cd PyWorkout
pip install -e .
```

An editable install means `pyworkout` on your PATH runs your working copy, so edits take effect immediately. To skip installing altogether, `python main.py` works just as well.

Development tooling — pytest, pytest-cov, pytest-mock, pylint, build — is not pulled in by the editable install:

```bash
pip install pytest pytest-cov pytest-mock pylint build
```

## Architecture in Brief

Almost all of PyWorkout is a single `workout()` function in `main.py`, roughly 600 lines. That is deliberate: the program is simple, and one readable function beats an abstraction layer nobody needs.

Two consequences worth knowing before you edit:

**State lives in module-level globals** set inside `workout()` — `select` (chosen muscle group), `activity_num` (current exercise), `start` (start time), `complete` (finished exercises), and `times` (per-exercise durations). Pylint objects to this; the file silences those specific warnings with inline `# pylint: disable=` comments. That is the established pattern here — please follow it rather than adding a `.pylintrc`.

**Workout data is parallel lists.** Each muscle group has a list of exercise names and a matching `_count` list of reps, and the two are index-aligned. Adding an exercise means appending to both, and updating the bounds check in the `next` branch. [Configuration](configuration.md) walks through this step by step.

`gui.py` is an unfinished Tkinter frontend. It is not connected to `main.py` and does not run — do not treat it as a reference for how the application behaves.

## Everyday Commands

```bash
# Run the CLI
python main.py

# Run the tests
pytest tests/ -v

# Tests with coverage
pytest tests/ --cov=. --cov-report=term-missing

# Lint
pylint $(git ls-files '*.py')

# Build the distributable packages
python -m build
```

[Testing](testing.md) covers the suite in more detail.

## Conventions

* **Comments.** The codebase comments heavily. Match that when you touch `main.py`.
* **No runtime dependencies.** PyWorkout uses only the standard library. Please keep it that way — it is why the executable build stays small and the Docker image stays simple.
* **Versioning.** [Semantic versioning](https://semver.org/). The version appears in both `setup.cfg` and `pyproject.toml`; update them together.

## Continuous Integration

Five workflows run in GitHub Actions:

| Workflow | Trigger | Does |
| --- | --- | --- |
| `tests.yml` | Push or PR to `main`/`develop` | pytest on Python 3.9–3.12, uploads coverage |
| `pylint.yml` | Every push | Pylint on Python 3.9 |
| `docker-publish.yml` | Push to `main`, tags, PRs, daily | Builds and pushes the image to ghcr.io |
| `push-to-pypi.yml` | Release published | Builds and publishes to PyPI |
| `codeql-analysis.yml` | Push, PRs, schedule | Security scanning |

## Releasing

1. Bump the version in `setup.cfg` and `pyproject.toml`.
2. Update `CHANGELOG.md`.
3. Tag and push: `git tag v1.2.0 && git push --tags`.
4. Publish a GitHub Release. `push-to-pypi.yml` handles PyPI from there; `docker-publish.yml` pushes the tagged image.
