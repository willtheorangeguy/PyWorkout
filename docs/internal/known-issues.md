# Known Issues — PyWorkout

Concrete defects and gaps found while writing this repository's documentation in
August 2026. **Nothing here was changed** — each one needs a code, configuration, or
licensing decision rather than a documentation one.

Ordered by severity. See [`docs/roadmap.md`](../roadmap.md) for the narrative version,
which also covers deliberate non-goals.


**4 open:** 2 medium, 2 low.

## 1. Startup banner claims GPL terms on an MIT project

**Severity:** Medium  
**Where:** `main.py`

**What:** The program prints GPL boilerplate at startup — "ABSOLUTELY NO WARRANTY", "free software", "redistribute it under certain conditions" — with a 2021-2024 copyright line. The repository is MIT and `LICENSE.md` is the MIT text.

**Why it matters:** The program tells every user it is under terms that do not govern it.

**Suggested fix:** Replace the banner with the MIT notice, or drop it. `LICENSE.md` is authoritative either way.

## 2. `skip` and `stats` are mutually exclusive

**Severity:** Medium  
**Where:** `main.py`, around lines 484-561

**What:** Using `skip` disables `stats` for the rest of the session; the program prints "You cannot use both the `skip` and `stats` commands, sorry!"

**Why it matters:** Both commands manipulate overlapping session bookkeeping inside a single ~600-line `workout()` function, so neither can be fixed without untangling that state.

**Suggested fix:** Extract session state into its own model. That is also what would make the two help outputs collapse into one.

## 3. Help text is printed twice and the copies have drifted

**Severity:** Low  
**Where:** `main.py`, around lines 613 and 632

**What:** Help is printed inline in two places. One documents the `skip`/`stats` limitation; the other omits it.

**Why it matters:** Which caveat a user sees depends on where they asked for help.

**Suggested fix:** Single source the help text.

## 4. The `video` command needs source edits to do anything

**Severity:** Low  
**Where:** `main.py`, under the `# Video File Paths` comment

**What:** Video paths are literals in the source and point nowhere useful by default.

**Why it matters:** A command that does nothing until you modify the program is closer to unimplemented than to configurable.

**Suggested fix:** Move paths into a config file, or make the command report that none are set.


---

## Also, across every repository

**`.bandit` is present on disk but untracked in git.** Verified in PyWorkout, treklogger,
skyscanner-cli, booking-cli, piggy, and aibot — the config file exists locally in each but
`git ls-files` does not know about it, so none of it reached GitHub.

The August 2026 security sweep therefore looks complete locally and landed nowhere. Worth
checking across all 44 repositories it covered.
