# PyWorkout Commands

**The following commands are available in PyWorkout:**
```
list    Lists the workout activities by muscle group.
start   Starts the workout and displays the first workout activity.
next    Moves to the next workout activity.
skip    Skips the current workout activity.
end     Completes the workout and display full workout statistics.
stats   Shows workout statistics at any point (does not work with the `skip` command).
video   Opens the workout video assigned to each muscle group.
license Shows the license. 
help    Prints this help text.
quit    Ends the program.
```

### `list`

Lists all of the workouts in a muscle group, as well as sets and reps. Example:

```
1. Situps                2 Sets of 25 Reps
2. Reverse Crunches      2 Sets of 25 Reps
3. Bicycle Crunches      2 Sets of 25 Reps
4. Flutter Kicks         2 Sets of 25 Reps
5. Leg Raises            2 Sets of 25 Reps
6. Elbow Planks          2 Sets of 2 Reps
```

### `start`

Starts the workout and the timer. Also displays the first workout activity. Example:

```
You have started the abs muscle group.
The current time is: 14:19:35
You have completed: 0%
Please complete 2 Sets of 25 Reps of Situps
```

### `next`

Moves to the next workout activity. Displays the elapsed time, and the percentage complete. Example:

```
You are in the abs muscle group.
The current time is: 14:23:01. 0:03:26.402040 has elapsed.
You have completed: 16%
Please complete 2 Sets of 25 Reps of Reverse Crunches
```

### `skip`

Skips to the next workout activity. Displays the elapsed time, and the percentage complete. **Does not work with the `stats` command.** Example:

```
You are in the abs muscle group.
The current time is: 14:26:15. 0:06:40.738759 has elapsed.
Activity skipped! Run the `next` command to move on.
```

### `end`

Finishes the workout. Displays the total time taken, and all the workouts that were completed. Example:

```
You have completed the abs muscle group.
It took 0:08:54.433515 to complete this workout.
The following activities were completed (time elapsed):
1. Situps               (0:08:54.433515)
Congratulations!
```

### `stats`

Displays the statistics from the workout. Includes current time, time elapsed, time elapsed per workout, workouts completed and workouts to go. **Does not work with the `skip` command.** Example:
```
You are in the abs muscle group.
The current time is: 14:29:49. 0:10:14.202242 has elapsed.
The following activities have been completed (time elapsed):
1. Situps               (0:08:54.433515)
The following activites still need to be completed:
1. Bicycle Crunches
2. Flutter Kicks
3. Leg Raises
4. Elbow Planks
You cannot use both the `skip` and `stats` commands, sorry!
```

### `video`

Launches the video assinged to each muscle group in the default video player for your device. **Must be configured by changing the `# Video File Paths` in `main.p`.** Example:

```
You are in the abs muscle group. 
The current time is: 14:33:04. 0:00:01.564038 has elapsed.
```

### `license`

Shows the GNU GPL v3 license text. The full license can be accessed in the `LICENSE.md` file. 

### `help`

Prints a list of each of the available commands. Example:

```
PyWorkout - (C) 2021-2022
Any of these options are available: 
list    Lists the workout activities by muscle group.
start   Starts the workout and displays the first workout activity.
next    Moves to the next workout activity.
skip    Skips the current workout activity.
end     Completes the workout and display full workout statistics.
stats   Shows workout statistics at any point (does not work with the `skip` command).
video   Opens the workout video assigned to each muscle group.
help    Prints this help text.
quit    Ends the program.
More documentation can be found on Github. Enjoy using the program! 
```

### `quit`

Exits the program. Useful for when the workout is completed. 
