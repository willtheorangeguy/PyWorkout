"""
PyWORKOUT CLI
Copyright (C) 2021-2026  @willtheorangeguy
"""

# pylint: disable=redefined-builtin, too-many-branches, too-many-statements, too-many-locals

import os
import subprocess
import sys
import time
from datetime import datetime

try:
    import config as config_mod
    import history as history_mod
except ImportError:  # installed as part of the package
    from . import config as config_mod
    from . import history as history_mod


def _play_video(path):
    """Open a video file with the OS default player."""
    if sys.platform == "win32":
        os.startfile(path)  # pylint: disable=no-member
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, path])


def _now_line(start_time):
    """Return the standard 'current time / elapsed' status line."""
    now = datetime.now()
    return (
        "The current time is: "
        + str(time.strftime("%H:%M:%S"))
        + ". "
        + str(now - start_time)
        + " has elapsed."
    )


def _elapsed_for(presented, index):
    """Seconds an item was on screen: until the next item, or until now."""
    start_ts = presented[index]["ts"]
    if index + 1 < len(presented):
        end_ts = presented[index + 1]["ts"]
    else:
        end_ts = datetime.now()
    return end_ts - start_ts


def workout(preselect=None, config_path=None):
    """PyWorkout interactive CLI."""
    workouts = config_mod.load_config(config_path)
    order = config_mod.group_order(workouts)

    # Per-workout state.
    select = None
    start_time = None
    presented = []  # [{"name", "ts", "kind"}], kind in {"exercise", "video"}

    def exercises_done():
        """Number of exercise activities presented so far."""
        return sum(1 for p in presented if p["kind"] == "exercise")

    def present_exercise():
        """Show the next exercise (or the 'all done' message) for the group."""
        items = workouts[select]["exercises"]
        total = len(items)
        index = exercises_done()
        if index < total:
            name, reps = items[index]
            percent = int(index / total * 100)
            print("You have completed: " + str(percent) + "%")
            print(
                "Please complete 2 Sets of "
                + str(reps)
                + " Reps of "
                + str(name)
            )
            presented.append({"name": name, "ts": datetime.now(), "kind": "exercise"})
        else:
            print("You have completed all the workouts for this set!")
            print("Run the `end` command to finish the workout. \n")

    def print_completed():
        """Print every presented activity with the time it took."""
        for i, item in enumerate(presented):
            elapsed = _elapsed_for(presented, i)
            print(str(i + 1) + ". " + str(item["name"]) + "\t(" + str(elapsed) + ")")

    # Welcome banner.
    print("         WELCOME TO PyWORKOUT")
    print("Please select a group from those below.")
    for i, key in enumerate(order):
        print(str(i + 1) + ". " + key.capitalize())
    print(
        "A reminder that today is: "
        + datetime.today().strftime("%A")
        + ". Consider option "
        + str(int(datetime.today().strftime("%w")) + 1)
        + "."
    )

    # Group selection (skipped when a valid group is preselected via CLI).
    if preselect is not None and preselect.lower() in workouts:
        select = preselect.lower()
        print(workouts[select]["display"] + " muscle group selected!\n")
    else:
        while select is None:
            choice = str(input("\nGroup? ")).lower()
            if choice == "quit":
                sys.exit()
            matched = None
            for i, key in enumerate(order):
                if choice == key or choice == str(i + 1):
                    matched = key
                    break
            if matched is None:
                print("Sorry that is incorrect. Please try again! \n")
            else:
                select = matched
                print(workouts[select]["display"] + " muscle group selected!\n")

    # Command loop.
    while True:
        activity = str(input("What do you want to do? ")).lower()

        if activity == "list":
            for i, (name, reps) in enumerate(workouts[select]["exercises"]):
                print(
                    str(i + 1)
                    + ". "
                    + str(name)
                    + "\t 2 Sets of "
                    + str(reps)
                    + " Reps"
                )
            print("")

        elif activity == "start":
            start_time = datetime.now()
            presented.clear()
            print("You have started the " + select + " muscle group. ")
            print("The current time is: " + str(time.strftime("%H:%M:%S")))
            present_exercise()
            print("")

        elif activity == "next":
            if start_time is None:
                print("Run the `start` command first! \n")
                continue
            print("You are in the " + select + " muscle group. ")
            print(_now_line(start_time))
            present_exercise()
            print("")

        elif activity == "skip":
            if not presented:
                print("Nothing to skip yet. Run `start` first. \n")
                continue
            print("You are in the " + select + " muscle group. ")
            print(_now_line(start_time))
            presented.pop()
            print("Activity skipped! Run the `next` command to move on. \n")

        elif activity == "end":
            if start_time is None:
                print("Run the `start` command first! \n")
                continue
            now = datetime.now()
            duration = now - start_time
            print("You have completed the " + select + " muscle group.")
            print("It took " + str(duration) + " to complete this workout.")
            print("The following activities were completed (time elapsed):")
            print_completed()
            history_mod.record_workout(
                select, duration.total_seconds(), [p["name"] for p in presented]
            )
            print("Congratulations! \n")

        elif activity == "stats":
            if start_time is None:
                print("Run the `start` command first! \n")
                continue
            print("You are in the " + select + " muscle group. ")
            print(_now_line(start_time))
            print("The following activities have been completed (time elapsed):")
            print_completed()
            print("The following activities still need to be completed:")
            remaining = workouts[select]["exercises"][exercises_done():]
            for i, (name, _reps) in enumerate(remaining):
                print(str(i + 1) + ". " + str(name))
            print("")

        elif activity == "video":
            if start_time is not None:
                print("You are in the " + select + " muscle group. ")
                print(_now_line(start_time))
            path = workouts[select].get("video") or ""
            if path:
                _play_video(path)
                presented.append(
                    {"name": select.capitalize() + " Video", "ts": datetime.now(), "kind": "video"}
                )
            else:
                print(
                    "No video configured for "
                    + select
                    + ". Set one in your config (run with --init-config)."
                )
            print("")

        elif activity == "history":
            print(history_mod.format_history())
            print("")

        elif activity == "license":
            print("PyWorkout Copyright (C) 2021-2026  @willtheorangeguy")
            print(
                "This program comes with ABSOLUTELY NO WARRANTY; for details view the license."
            )
            print("This is free software, and you are welcome to redistribute it")
            print("under certain conditions; view the license for details. \n")

        elif activity == "quit":
            sys.exit()

        elif activity == "help":
            print("PyWorkout - (C) 2021-2026")
            print("Any of these options are available: ")
            print("list    Lists the workout activities by muscle group.")
            print("start   Starts the workout and displays the first workout activity.")
            print("next    Moves to the next workout activity.")
            print("skip    Skips the current workout activity.")
            print("end     Completes the workout and display full workout statistics.")
            print("stats   Shows workout statistics at any point.")
            print("video   Opens the workout video assigned to each muscle group.")
            print("history Shows your past completed workouts.")
            print("license Show the license.")
            print("help    Prints this help text.")
            print("quit    Ends the program.")
            print(
                "More documentation can be found on Github. Enjoy using the program! \n"
            )

        else:
            print("Sorry that is not an option. Please see this list of options below:")
            print("list    Lists the workout activities by muscle group.")
            print("start   Starts the workout and displays the first workout activity.")
            print("next    Moves to the next workout activity.")
            print("skip    Skips the current workout activity.")
            print("end     Completes the workout and display full workout statistics.")
            print("stats   Shows workout statistics at any point.")
            print("video   Opens the workout video assigned to each muscle group.")
            print("history Shows your past completed workouts.")
            print("license Show the license.")
            print("help    Prints a similar help text.")
            print("quit    Ends the program. \n")


if __name__ == "__main__":
    # Running `python main.py` launches the interactive REPL directly.
    # For command-line flags use the `pyworkout` script or `python -m PyWorkout`.
    workout()
