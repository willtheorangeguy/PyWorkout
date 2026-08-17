<!-- Logo -->
<h1 align="center">
  <img src="https://raw.githubusercontent.com/willtheorangeguy/.github/main/icons/PyWorkout/logo.png" height="250px" width="400px" alt="PyWorkout">
  <br>
  PyWorkout
  <br>
</h1>

<!-- Copy -->
<h4 align="center">A minimal CLI to keep you inspired during your workout.</h4>

<!-- Badges -->
<div align="center">
  <img alt="Tests" src="https://github.com/willtheorangeguy/PyWorkout/actions/workflows/tests.yml/badge.svg">
  <img alt="Pylint" src="https://github.com/willtheorangeguy/PyWorkout/actions/workflows/pylint.yml/badge.svg">
  <img alt="Docker Build" src="https://github.com/willtheorangeguy/PyWorkout/actions/workflows/docker-publish.yml/badge.svg">
  <img alt="PyPI Build" src="https://github.com/willtheorangeguy/PyWorkout/actions/workflows/push-to-pypi.yml/badge.svg">
  <img alt="CodeQL" src="https://github.com/willtheorangeguy/PyWorkout/actions/workflows/codeql-analysis.yml/badge.svg">
  <img alt="Version" src="https://img.shields.io/github/v/release/willtheorangeguy/PyWorkout?include_prereleases">
  <img alt="Issues" src="https://img.shields.io/github/issues/willtheorangeguy/PyWorkout">
  <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/willtheorangeguy/PyWorkout">
  <img alt="License" src="https://img.shields.io/github/license/willtheorangeguy/PyWorkout">
</div>

<!-- Navigation -->
<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#documentation">Documentation</a> •
  <a href="#support">Support</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

<!-- Hero -->

![PyWorkout running in a terminal](https://raw.githubusercontent.com/willtheorangeguy/.github/main/icons/PyWorkout/welcome.png)

## Key Features

* Pick a muscle group and get walked through the workout one exercise at a time.
* Nine muscle groups covering the whole body, each with its own set and rep counts.
* Live elapsed time and percent complete after every exercise.
* Skip anything you would rather not do, and see full statistics at the end.
* Open a local video for the current muscle group with one command.
* Add exercises, change rep counts, and swap videos by editing plain Python lists.
* No runtime dependencies beyond the standard library. Runs on Windows, macOS, and Linux.

## Installation

```bash
pip install pyworkout
```

Prefer a standalone Windows executable, the source, or a container? See [Installation](docs/installation.md).

## Usage

Start the CLI, choose a muscle group, then step through the workout:

```console
$ pyworkout
Which muscle group would you like to work out? abs

> start
You have started the abs muscle group.
The current time is: 14:19:35
You have completed: 0%
Please complete 2 Sets of 25 Reps of Situps

> next
You have completed: 16%
Please complete 2 Sets of 25 Reps of Reverse Crunches

> end
```

`help` lists every command. The full reference is in [Commands](docs/commands.md).

## Documentation

Full documentation lives in [`docs/`](docs/README.md):
[Quickstart](docs/quickstart.md) · [Installation](docs/installation.md) · [Usage](docs/usage.md) · [Commands](docs/commands.md) · [Configuration](docs/configuration.md) · [Architecture](docs/architecture.md) · [FAQ](docs/faq.md) · [Troubleshooting](docs/troubleshooting.md) · [Roadmap](docs/roadmap.md)

## Support

Open a [GitHub Discussion](https://github.com/willtheorangeguy/PyWorkout/discussions/new) or file an [issue](https://github.com/willtheorangeguy/PyWorkout/issues/new/choose).

## Contributing

Contributions welcome. See the org-wide [Contributing Guide](https://github.com/willtheorangeguy/.github/blob/main/CONTRIBUTING.md) and [Code of Conduct](https://github.com/willtheorangeguy/.github/blob/main/CODE_OF_CONDUCT.md).

## Credits

Built with [Python](https://www.python.org/), packaged with [PyInstaller](https://pyinstaller.org/), and distributed through [PyPI](https://pypi.org/project/PyWorkout/) and [GitHub Packages](https://github.com/willtheorangeguy/PyWorkout/pkgs/container/pyworkout).

## License

MIT — see [`LICENSE.md`](LICENSE.md).
