# Changelog

## [v1.3.0](https://github.com/willtheorangeguy/PyWorkout/releases/tag/v1.3.0)

### Added

- Workout history saved between sessions (`history` command and `--history` flag).
- Command-line flags: `--group`, `--list`, `--history`, `--init-config`, `--config`, `--version`.
- User config file (`~/.pyworkout/config.json`) for exercises, reps, and video paths — no code editing required.

### Changed

- Exercise data refactored into a single structure; the old parallel-list / if-elif layout is gone.
- Video paths now come from config instead of being hardcoded.
- Packaging consolidated into `pyproject.toml` (removed `setup.py`, trimmed `setup.cfg`).

### Fixed

- Triceps `list` showing glutes exercises.
- `start` always reporting 0% progress.
- Off-by-one bounds and a rep-count mismatch on five-exercise groups.
- `stats` no longer breaks after `skip`.

## [v1.2.0](https://github.com/willtheorangeguy/PyWorkout/releases/tag/v1.2.0)

### Added

- Docker container.
- PyPI package.

## [v1.1.0](https://github.com/willtheorangeguy/PyWorkout/releases/tag/v1.1.0)

### Added

- License text to the top of each code file.

## [v1.0.0](https://github.com/willtheorangeguy/PyWorkout/releases/tag/v1.0.0)

### Added

- CLI

### Changed

- GUI filenames

## [v0.1.0-beta](https://github.com/willtheorangeguy/PyWorkout/releases/tag/v0.1.0-beta)

### Added

- GUI
- Accurate timekeeping

### Changed

- Timer
