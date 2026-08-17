# PyWorkout — Quickstart

## Install

```bash
pip install pyworkout
```

Requires Python 3.9+. Other install paths — source, Docker, Windows executable — are in
[Installation](./installation.md).

## Run

```bash
pyworkout
```

## Pick a muscle group

You are prompted for one. Both the number and the name work:

```
1  abs        4  chest      7  back
2  quads      5  arms
3  glutes     6  shoulders
```

## Work through it

```
list    show the exercises in this group
start   begin, and start the timer
next    move to the next exercise
skip    skip the current one
stats   progress so far
end     finish and show the summary
quit    exit
```

A typical session is `start`, then `next` repeatedly, then `end`.

## What to expect

```
You have started the abs muscle group.
The current time is: 14:19:35
You have completed: 0%
Please complete 2 Sets of 25 Reps of Situps
```

Each `next` reports elapsed time and percentage complete. `end` prints the total time and
everything you finished.

## One thing that will catch you out

**`skip` and `stats` do not work together.** Once you have skipped an exercise, `stats`
stops reporting for that session and says so. This is a known defect rather than a design
choice — see [Roadmap](./roadmap.md).

## Then what

- [Usage](./usage.md) — the full session flow
- [Commands](./commands.md) — every command with example output
- [Configuration](./configuration.md) — adding your own exercises and videos
