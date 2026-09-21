# Known Issues — PyWorkout

Concrete defects and gaps found while writing this repository's documentation in
August 2026. **Nothing here was changed** — each one needs a code, configuration, or
licensing decision rather than a documentation one.

Ordered by severity. See [`docs/roadmap.md`](../roadmap.md) for the narrative version,
which also covers deliberate non-goals.

**1 open, 3 resolved:** 1 medium open; 2 medium and 1 low resolved by the `cli.py` /
`config.py` / `data.py` / `history.py` module split (ported from the
`refactor-data-config-history-cli` branch).

## 1. Startup banner claims GPL terms on an MIT project

**Severity:** Medium
**Where:** `main.py`

**What:** The program prints GPL boilerplate at startup — "ABSOLUTELY NO WARRANTY", "free software", "redistribute it under certain conditions" — with a 2021-2024 copyright line. The repository is MIT and `LICENSE.md` is the MIT text.

**Why it matters:** The program tells every user it is under terms that do not govern it.

**Suggested fix:** Replace the banner with the MIT notice, or drop it. `LICENSE.md` is authoritative either way.

**Status:** Still open. The `license`/`help` text ported from `refactor-data-config-history-cli` keeps the same GPL-style wording; this fix was out of scope for that refactor.

## 2. `skip` and `stats` are mutually exclusive — RESOLVED

**Severity:** Medium (was)
**Where:** `main.py`, around lines 484-561 (pre-refactor)

**What:** Using `skip` disabled `stats` for the rest of the session; the program printed "You cannot use both the `skip` and `stats` commands, sorry!"

**Resolution:** `main.py` now tracks presented activities as a list of `{name, ts, kind}` records instead of parallel lists with an index that `skip` could desync. `skip` pops the last presented record; `stats` reads the same list. The two commands no longer interfere.

## 3. Help text is printed twice and the copies had drifted — RESOLVED

**Severity:** Low (was)
**Where:** `main.py`, around lines 613 and 632 (pre-refactor)

**What:** Help was printed inline in two places. One documented the `skip`/`stats` limitation; the other omitted it.

**Resolution:** Since issue #2 is fixed, the `skip`/`stats` caveat no longer applies, so both copies (the `help` command and the unrecognised-command fallback) now agree. They are still two separate `print` blocks rather than a single source, so a future edit could redrift them — worth a follow-up if anyone touches that code again.

## 4. The `video` command needs source edits to do anything — RESOLVED

**Severity:** Low (was)
**Where:** `main.py`, under the `# Video File Paths` comment (pre-refactor)

**What:** Video paths were literals in the source and pointed nowhere useful by default.

**Resolution:** Video paths now live in `~/.pyworkout/config.json` (see `config.py`, `docs/config.sample.json`), written with `pyworkout --init-config`. The `video` command reports "No video configured" instead of silently doing nothing when a group has none set.

**Documentation note:** `README.md` and `docs/usage.md`/`docs/commands.md`/`docs/configuration.md` still describe the pre-refactor model (video paths edited directly in `main.py`, exercises customized by "editing plain Python lists", nine muscle groups). Those pages predate this module split and were already drifted from the shipped code before it (see the top of this file); they still need a documentation pass to describe the `cli.py`/`config.py`/`data.py`/`history.py` structure, the new CLI flags, and the config file. Not attempted here to avoid guessing at the intended house style for that doc set.

---

## Also, across every repository

**`.bandit` is present on disk but untracked in git.** Verified in PyWorkout, treklogger,
skyscanner-cli, booking-cli, piggy, and aibot — the config file exists locally in each but
`git ls-files` does not know about it, so none of it reached GitHub.

The August 2026 security sweep therefore looks complete locally and landed nowhere. Worth
checking across all 44 repositories it covered.
