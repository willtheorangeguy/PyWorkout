# PyWorkout — Usage

A workout has three phases: choose a muscle group, step through the exercises, then finish and read your statistics.

## Choosing a Muscle Group

Start PyWorkout and you are asked which muscle group to work:

```console
$ pyworkout
Which muscle group would you like to work out?
```

Answer with either the name or its number. `abs` and `1` do the same thing.

Nine groups are available: **abs**, **quads**, **hamstrings**, **calves**, **chest**, **back**, **shoulders**, **biceps**, and **triceps**.

If you enter something unrecognised, PyWorkout asks again rather than exiting.

## Stepping Through a Workout

Once a group is selected you are at the command prompt. A typical session:

```console
> list
1. Situps                2 Sets of 25 Reps
2. Reverse Crunches      2 Sets of 25 Reps
3. Bicycle Crunches      2 Sets of 25 Reps
4. Flutter Kicks         2 Sets of 25 Reps
5. Leg Raises            2 Sets of 25 Reps
6. Elbow Planks          2 Sets of 2 Reps

> start
You have started the abs muscle group.
The current time is: 14:19:35
You have completed: 0%
Please complete 2 Sets of 25 Reps of Situps

> next
You are in the abs muscle group.
The current time is: 14:23:01. 0:03:26 has elapsed.
You have completed: 16%
Please complete 2 Sets of 25 Reps of Reverse Crunches
```

`start` begins the timer, so run it when you actually begin. Every `next` records how long the previous exercise took.

Once you have worked through the whole list, `next` tells you there is nothing left and prompts you to run `end`.

## Skipping and Statistics

`skip` moves past an exercise without recording it as complete — useful when equipment is unavailable or something hurts.

`stats` shows your progress mid-workout, and `end` finishes the workout and prints the full breakdown.

> **`skip` and `stats` do not work together.** Skipping leaves a gap in the timing data that the statistics calculation cannot account for. If you have skipped anything this session, `stats` will be wrong — use `end` instead. See [Commands](commands.md#stats).

## Watching a Video

`video` opens the video assigned to the current muscle group in your default player. This needs local file paths configured first — see [Configuration](configuration.md#change-the-videos). Without that, the command has nothing to open.

## Full Command Reference

Every command, with example output, is documented in [Commands](commands.md). `help` prints the same list inside the program.
