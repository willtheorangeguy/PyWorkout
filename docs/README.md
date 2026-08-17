# PyWorkout — Documentation

A terminal workout tracker: pick a muscle group, work through its exercises, and get timing
and completion statistics as you go. Ships to PyPI, GHCR, and as a Windows executable.

```
PyWorkout/
├── docs/
│   ├── README.md          this page
│   ├── quickstart.md      install, pick a group, finish a session
│   ├── installation.md    all four install paths
│   ├── usage.md           the session flow
│   ├── commands.md        every command with example output
│   ├── configuration.md   exercises, videos, and what needs source edits
│   ├── architecture.md    how main.py and gui.py are shaped
│   ├── development.md     contributing to the code
│   ├── testing.md         the test suite and coverage
│   ├── faq.md             skip/stats, the GPL banner, what gui.py is
│   ├── troubleshooting.md concrete failures and fixes
│   └── roadmap.md         planned work and known defects
├── main.py                the CLI
├── gui.py                 a separate Tkinter percentage tracker
└── tests/
```

## Pages

- [Quickstart](./quickstart.md) — install, run one workout
- [Installation](./installation.md) — PyPI, source, Docker, Windows executable
- [Usage](./usage.md) — how a session flows
- [Commands](./commands.md) — full command reference with example output
- [Configuration](./configuration.md) — adding exercises and video paths
- [Architecture](./architecture.md) — the shape of the code and what follows from it
- [Development](./development.md) — working on it
- [Testing](./testing.md) — the suite, coverage, and writing new tests
- [FAQ](./faq.md) — why `stats` stopped, what `gui.py` is, the licence banner
- [Troubleshooting](./troubleshooting.md) — Tkinter, Docker, `PATH`, timing
- [Roadmap](./roadmap.md) — version 2.0.0 and known defects
