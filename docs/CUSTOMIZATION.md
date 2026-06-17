# PyWorkout Customization

PyWorkout is heavily customizable. You can add workouts, change rep counts, and
set your own videos — **without editing any source code**. Everything lives in a
single JSON config file.

## The config file

Customization is done through `~/.pyworkout/config.json` (on Windows,
`C:\Users\<you>\.pyworkout\config.json`). The file is **deep-merged over the
built-in defaults**, so you only have to specify the parts you want to change —
every group and field you leave out keeps its default.

### Create a starter config

Run:

```bash
pyworkout --init-config
```

This writes the full default config to `~/.pyworkout/config.json`, which you can
then trim down and edit. A minimal example lives at
[`docs/config.sample.json`](config.sample.json).

Each group has a `display` name, a `video` path, and an `exercises` list of
`[name, reps]` pairs:

```json
{
  "abs": {
    "video": "/home/you/Videos/10 Minute Ab Workout.mp4",
    "exercises": [
      ["Situps", 25],
      ["Reverse Crunches", 25]
    ]
  }
}
```

## Add a Workout

1. Open `~/.pyworkout/config.json` (run `pyworkout --init-config` first if it
   doesn't exist).
2. Find the group you want to add to, e.g. `"abs"`.
3. Add a new `["Activity Name", reps]` pair to that group's `exercises` list.
4. Save and run `pyworkout`. The percentage, list, and stats all adjust
   automatically — there are no counts to keep in sync.

## Change the Number of Reps

1. Open `~/.pyworkout/config.json`.
2. Change the second number in any `["Activity Name", reps]` pair.
3. Save and run the program.

## Change the Videos

1. Choose your videos. Workout videos by
   [Pamela Reif](https://www.youtube.com/channel/UChVRfsT_ASBZk10o0An7Ucg) are a
   great start. You can use a local file path **or** a web/YouTube URL.
2. Open `~/.pyworkout/config.json`.
3. Set the `"video"` field for each muscle group to your file path or URL.
   On Windows, escape backslashes in JSON (`"C:\\Videos\\abs.mp4"`).
4. Save and run the program, then use the `video` command in a workout.

## Add a whole new muscle group

Add a brand-new top-level key to the config with `display`, `video`, and
`exercises`. It appears in the selection menu automatically (after the built-in
groups).
