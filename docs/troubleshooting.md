# PyWorkout — Troubleshooting

## `stats` stopped working

You used `skip` earlier in the session. The two commands do not coexist, and `stats` will
say so. Start a new session to get statistics back, or avoid `skip` in a session where you
want them. Tracked in [Roadmap](./roadmap.md).

## `video` opens nothing

Video paths are not configured out of the box — they are literals in `main.py` under
`# Video File Paths`, and point nowhere useful until you edit them. See
[Configuration](./configuration.md).

## `pyworkout: command not found`

The console script did not land on your `PATH`. Either the install went into a virtual
environment that is not active, or your user-level bin directory is not on `PATH`. As a
check, the module entry point works regardless:

```bash
python -m pyworkout
```

## The GUI will not start

`gui.py` needs Tkinter, which is not always present on Linux even when Python is:

```bash
sudo apt install python3-tk     # Debian/Ubuntu
```

Over SSH without X forwarding it cannot open a window at all. The CLI is unaffected.

## GUI tests are skipped

Expected in a headless environment. Tkinter needs a display, so CI skips them. Not a
failure.

## Docker container exits immediately

The container needs an interactive terminal — the program is a prompt loop, and without
stdin it reaches EOF and stops:

```bash
docker run -i -t ghcr.io/willtheorangeguy/pyworkout:main python main.py
```

Both `-i` and `-t` matter.

## Elapsed time looks wrong

The timer measures wall-clock time from `start` with no pause, so any time away from the
terminal is included. There is also a known timer defect tracked for version 2.0.0 — see
[Roadmap](./roadmap.md).

## It prints GPL warranty text on startup

A leftover banner. The repository is MIT-licensed; `LICENSE.md` is authoritative and the
startup text is wrong. Recorded in [Roadmap](./roadmap.md).

## Tests fail to import

Run them from the project root, so the package resolves:

```bash
cd /path/to/PyWorkout
pytest tests/
```
