"""
PyWorkout command-line interface.

Wraps the interactive ``workout()`` REPL with argparse flags for scriptable,
non-interactive use. With no arguments it simply launches the REPL, so the
existing interactive behaviour (and its test suite) is unchanged.
"""

import argparse
import sys

try:
    import config as config_mod
    import history as history_mod
    from main import workout
except ImportError:  # installed as part of the package
    from . import config as config_mod
    from . import history as history_mod
    from .main import workout

__version__ = "1.3.0"


def build_parser():
    """Construct the argument parser."""
    parser = argparse.ArgumentParser(
        prog="pyworkout",
        description="A minimal CLI to keep you inspired during your workout!",
    )
    parser.add_argument(
        "-g", "--group", help="preselect a muscle group and skip the prompt"
    )
    parser.add_argument(
        "--list",
        nargs="?",
        const="__ALL__",
        metavar="GROUP",
        help="list exercises (optionally for one group) and exit",
    )
    parser.add_argument(
        "--history", action="store_true", help="print past workouts and exit"
    )
    parser.add_argument(
        "--init-config",
        action="store_true",
        help="write a default config file you can edit, then exit",
    )
    parser.add_argument(
        "--config", metavar="PATH", help="use an alternate config file"
    )
    parser.add_argument(
        "--version", action="version", version="pyworkout " + __version__
    )
    return parser


def parse_args(argv=None):
    """Parse ``argv`` (defaults to ``sys.argv``) into a namespace."""
    return build_parser().parse_args(argv)


def _print_group(workouts, key):
    """Print one group's exercises."""
    print(key.capitalize() + ":")
    for i, (name, reps) in enumerate(workouts[key]["exercises"]):
        print(f"{i + 1}. {name}\t 2 Sets of {reps} Reps")


def _do_list(args):
    """Handle ``--list``."""
    workouts = config_mod.load_config(args.config)
    if args.list == "__ALL__":
        for key in config_mod.group_order(workouts):
            _print_group(workouts, key)
            print("")
    else:
        key = args.list.lower()
        if key not in workouts:
            print(f"Unknown group: {args.list}")
            return 1
        _print_group(workouts, key)
    return 0


def main(argv=None):
    """Entry point: dispatch flags or launch the interactive REPL."""
    args = parse_args(argv)

    if args.init_config:
        path = config_mod.write_default_config(args.config)
        print(f"Wrote default config to {path}")
        return 0

    if args.history:
        print(history_mod.format_history())
        return 0

    if args.list is not None:
        return _do_list(args)

    workout(preselect=args.group, config_path=args.config)
    return 0


if __name__ == "__main__":
    sys.exit(main())
