# PyWorkout — Architecture

## Layout

```
PyWorkout/
├── main.py             the CLI — command loop, workout data, all session state
├── gui.py              a separate Tkinter percentage tracker
├── __main__.py         module entry point (python -m pyworkout)
├── docker-compose.yml  containerised run
├── Dockerfile          published to GHCR
├── pyproject.toml      packaging; published to PyPI
├── setup.cfg           pytest and coverage configuration
└── tests/
    ├── test_main.py    CLI behaviour
    └── test_gui.py     GUI components
```

## Two programs, not one

`main.py` and `gui.py` are independent. The CLI does not import the GUI, and the GUI is not
a front end for the CLI — it is a separate Tkinter window that displays percentage
completion for a fixed exercise list.

They share the project and the name, and nothing else. Worth knowing before looking for the
integration point: there isn't one.

## `main.py` is a single function

The entire CLI — muscle-group selection, the command loop, timing, statistics, help output,
and the exercise data itself — lives inside one `workout()` function of roughly six hundred
lines.

Consequences that show up in practice:

- **Session state is local variables**, which is why `skip` and `stats` interact badly:
  they manipulate overlapping bookkeeping in the same scope rather than through a shared
  model. See [Roadmap](./roadmap.md).
- **Help text is printed inline in two places** (around lines 613 and 632) and the two
  copies have drifted — one documents the `skip`/`stats` limitation, the other omits it.
- **Tests reach the logic through `builtins.input` and `builtins.print`.** Every test in
  `test_main.py` patches those and asserts against captured output, because there is no
  return value to inspect. That is a consequence of the structure, not a testing choice.

Extracting the workout data and the session state into their own modules is the change that
would unlock most of the rest.

## Data

Exercise definitions — muscle groups, exercises, sets, reps — are literals in `main.py`.
There is no data file, no database, and nothing persisted between runs. Closing the program
discards the session.

Video paths are also literals, under a `# Video File Paths` comment, which is why the
`video` command requires editing source to work. See [Configuration](./configuration.md).

## Timing

Elapsed time is computed from a start timestamp captured by `start` and compared against
the current time on each `next`, `stats`, and `end`. There is no pause, and no persistence —
the timer measures wall-clock time from `start`, including any time you spent away from the
terminal.

The known timer defect tracked for 2.0.0 lives here.

## Distribution

The same code ships four ways: PyPI (`pip install pyworkout`), a GHCR container, a Windows
executable attached to releases, and the source itself. `pyproject.toml` drives the first,
`Dockerfile` the second.

Because the PyPI and GHCR pages render the README off-site, its images must be absolute
URLs — they point at `.github/icons/PyWorkout/`. Relative image paths would break there
even though they work on github.com.

## Testing

`setup.cfg` configures pytest with coverage, branch coverage, and three report formats.
Coverage sits around 54%. GUI tests skip in headless environments, since Tkinter needs a
display — expected in CI rather than a failure.
