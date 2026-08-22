# PyWorkout — FAQ

## Why can't I use `skip` and `stats` together?

Because they interfere. Once you skip an exercise, `stats` stops reporting for that session
and prints "You cannot use both the `skip` and `stats` commands, sorry!"

This is a defect rather than a design decision — both commands manipulate the same session
bookkeeping inside one large function. See [Architecture](./architecture.md) and
[Roadmap](./roadmap.md).

## The `video` command does nothing

It needs paths configured first. Video file paths are literals in `main.py`, under the
`# Video File Paths` comment — the command opens whatever is listed there in your default
player, and does nothing useful until you point it at real files. See
[Configuration](./configuration.md).

## Does it save my workout history?

No. Nothing is persisted. Closing the program discards the session, and there is no history
across runs.

## Can I add my own exercises?

Yes, by editing `main.py` — the muscle groups, exercises, sets, and reps are literals in
the source. There is no data file. See [Configuration](./configuration.md).

## What's `gui.py`?

A separate Tkinter window that tracks percentage completion for a fixed exercise list. It
is **not** a front end for the CLI — the two programs are independent and share nothing but
the repository. Looking for how they connect is time wasted; they do not.

## Why does it print GPL text when the repo says MIT?

`main.py` prints GPL boilerplate at startup — "ABSOLUTELY NO WARRANTY", "free software",
"redistribute it under certain conditions" — with a 2021-2024 copyright line. The
repository is MIT-licensed, and `LICENSE.md` is the MIT text.

The startup banner is wrong. It is a leftover, tracked in [Roadmap](./roadmap.md), and the
licence that governs the code is the one in `LICENSE.md`.

## Does the timer pause?

No. It measures wall-clock time from `start`, so time spent away from the terminal counts.
A timer fix is the tracked item for version 2.0.0.

## Which install should I use?

`pip install pyworkout` unless you have a reason not to. Docker suits a throwaway
environment; the Windows executable suits a machine with no Python. All four ship the same
code — see [Installation](./installation.md).

## Why do GUI tests skip in CI?

Tkinter needs a display, and CI runners are headless. Expected behaviour, not a failure.

## Is this exercise advice?

No. It is a timer and a checklist. The exercises, sets, and reps are one person's routine
hardcoded into a script, not a programme designed for anyone in particular.
