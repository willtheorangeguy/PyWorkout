# PyWorkout — Roadmap

## Version 2.0.0

- [ ] [#1](https://github.com/willtheorangeguy/PyWorkout/issues/1) — Fix Timer

More planning lives on the
[Issues page](https://github.com/willtheorangeguy/PyWorkout/issues) and the
[Projects page](https://github.com/willtheorangeguy/PyWorkout/projects?type=classic).

## Known defects

**`skip` and `stats` are mutually exclusive.** Using `skip` disables `stats` for the rest
of the session, and the program says so rather than failing silently. Both commands
manipulate overlapping session bookkeeping inside a single function — see
[Architecture](./architecture.md). Extracting session state into its own model is what
fixes this properly.

**The startup banner claims GPL terms on an MIT project.** `main.py` prints "ABSOLUTELY NO
WARRANTY", "free software", and "redistribute it under certain conditions", with a
2021-2024 copyright line. The repository is MIT and `LICENSE.md` is the MIT text. The
banner is a leftover and contradicts the actual licence.

**Two help outputs have drifted.** Help text is printed inline in two places in `main.py`.
One documents the `skip`/`stats` limitation; the other omits it, so which caveat you see
depends on where you asked.

**`video` requires editing source to work at all.** Paths are literals under
`# Video File Paths`. A command that does nothing until you modify the program is closer to
unimplemented than configurable.

## Structural gaps

**`main.py` is one ~600-line function.** Muscle-group selection, the command loop, timing,
statistics, help, and the exercise data all live inside `workout()`. This is the root cause
of the `skip`/`stats` defect and the duplicated help text, and it is why tests have to reach
the logic by patching `builtins.input` and `builtins.print` — there is no return value to
assert against.

**Coverage is around 54%.** Reasonable for a prompt-loop program tested through stdout, but
the untested half is where the timer and statistics logic lives.

**Exercises are hardcoded.** Adding your own means editing `main.py`. A data file would
make the program useful to someone whose routine differs.

**Nothing persists.** No history, no progress across sessions, no record that a workout
happened.

**The CLI and the GUI are unrelated programs.** `gui.py` tracks percentages for its own
fixed exercise list and shares nothing with `main.py`.

## Non-goals

- **Exercise prescription.** This is a timer and a checklist over one person's routine, not
  a training programme.
- **Accounts or sync.** It is a local script.
