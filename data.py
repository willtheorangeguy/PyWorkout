"""
PyWorkout default exercise data.

Single source of truth for muscle groups, their exercises, rep counts, and
default video paths. The CLI iterates these structures instead of the old
parallel-list / if-elif layout, so exercises and rep counts can never drift
out of sync and per-group bounds always come from ``len()``.

User config (see ``config.py``) is deep-merged over ``WORKOUTS`` at runtime,
so anything here is just the built-in default.
"""

# Order groups are presented in the selection menu. The day-of-week
# recommendation maps datetime "%w" (Sun=0) + 1 onto this 1-based list.
GROUP_ORDER = ["abs", "quads", "glutes", "triceps", "biceps", "back", "chest"]

# Each group: a human "display" word (used in "<display> muscle group selected!")
# and a list of (exercise name, reps) pairs. "video" is the default path opened
# by the `video` command; empty by default so users set their own via config.
WORKOUTS = {
    "abs": {
        "display": "Ab",
        "video": "",
        "exercises": [
            ("Situps", 25),
            ("Reverse Crunches", 25),
            ("Bicycle Crunches", 25),
            ("Flutter Kicks", 25),
            ("Leg Raises", 25),
            ("Elbow Planks", 2),
        ],
    },
    "quads": {
        "display": "Quad",
        "video": "",
        "exercises": [
            ("Lunges", 50),
            ("High Knees", 50),
            ("Side Kicks", 50),
            ("Mountain Climbers", 25),
            ("Plank Jump Ins", 25),
            ("Lunges & Step Ups", 50),
        ],
    },
    "glutes": {
        "display": "Glutes",
        "video": "",
        "exercises": [
            ("Squats", 25),
            ("Donkey Kicks", 25),
            ("Bridges", 25),
            ("Step Ups", 25),
            ("Fly Steps", 50),
            ("Side Leg Raises", 50),
        ],
    },
    "triceps": {
        "display": "Tricep",
        "video": "",
        "exercises": [
            ("Diamond Pushups", 25),
            ("Tricep Dips", 25),
            ("Tricep Extensions", 25),
            ("Get Ups", 50),
            ("Punches", 50),
            ("Side to Side Chops", 50),
        ],
    },
    "biceps": {
        "display": "Bicep",
        "video": "",
        "exercises": [
            ("Backlists", 50),
            ("Doorframe Rows", 50),
            ("Decline Pushups", 25),
            ("Side Plank", 2),
            ("Pushups", 25),
        ],
    },
    "back": {
        "display": "Back",
        "video": "",
        "exercises": [
            ("Scapular Shrugs", 25),
            ("Supermans", 25),
            ("Back Lifts", 25),
            ("Arm/Leg Plank", 2),
            ("Reverse Angels", 25),
        ],
    },
    "chest": {
        "display": "Chest",
        "video": "",
        "exercises": [
            ("Pushups", 25),
            ("Chest Expansions", 25),
            ("Chest Squeezes", 25),
            ("Pike Pushups", 25),
            ("Shoulder Taps", 25),
        ],
    },
}
