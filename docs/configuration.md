# PyWorkout — Configuration

PyWorkout keeps its workout data as plain Python lists in `main.py`, so changing it means editing that file directly — there is no config file or database.

You need [Python](https://www.python.org/downloads/) and [a text editor](https://code.visualstudio.com/), and you need to be running PyWorkout [from source](installation.md#from-source). Edits to `main.py` have no effect on a `pip`-installed copy or the Windows executable.

## Add a Workout

To add a workout, you follow many of the same steps as adding a muscle group.

1. Open the `main.py` file with a text editor.
2. Navigate to the `# Workout Lists` section.
3. Find the variables for the muscle group you want to add this workout to. For example, select the `ab` muscle group. These are the two variables you need:

```python
abs = ["Situps\t", "Reverse Crunches", "Bicycle Crunches", "Flutter Kicks", "Leg Raises\t", "Elbow Planks\t"]
abs_count = [25, 25, 25, 25, 25, 2]
```

4. Add the name of the activity to the first list, in between double quotes (`""`).
5. Add the number of reps for that activity to the second list.
6. Navigate to the `elif activity.lower() == "next":` line.
7. Find the `if`/`elif` statement for the muscle group you have selected. For example:

```python
if select == "abs":
        if activity_num < 6:
            print("You have completed: " + str((int(activity_num/len(abs_count)*100))) + "%")
            print("Please complete 2 Sets of " + str(abs_count[activity_num]) + " Reps of " + str(abs[activity_num]) + "\n")
            complete.append(abs[activity_num])
        else:
            print("You have completed all the workouts for this set!")
            print("Run the `end` command to finish the workout. \n")
```

8. Increase the number in the second line by the number of workouts you have added.
9. Save and run the program!

## Change the Number of Reps

Changing the number of reps of a workout is extremely easy!

1. Open the `main.py` file with a text editor.
2. Navigate to the `# Workout Lists` section.
3. Find the variables that end with `..._count`. They should look like this:

```python
abs_count = [25, 25, 25, 25, 25, 2]
```

4. Change the number to the actual number of that workout that you want to do. Each item in the list corresponds to the workout activity list in the variable above it. For example, the `abs` and `abs_count` list correspond to one another.
5. Save the file and run the program!

## Change the Videos

The `video` command opens a local video file for the current muscle group. The paths shipped in `main.py` point at one particular machine, so this command does nothing useful until you set your own.

1. Choose your videos — recorded yourself, or downloaded. Workout videos by [Pamela Reif](https://www.youtube.com/@PamelaRf1) work well.
2. Open the `main.py` file with a text editor.
3. Navigate to the `# Video File Paths` section. It looks like this:

```python
# Video File Paths
abs_video = "D:\\Videos\\Workout Videos\\10 Minute Ab Workout.mp4" # change these to personal video path
quads_video = "D:\\Videos\\Workout Videos\\12 Min Leg Workout.mp4"
glutes_video = "D:\\Videos\\Workout Videos\\10 Minute Glute Bridge Workout.mp4"
triceps_video = "D:\\Videos\\Workout Videos\\10 Minute Upper Body Workout.mp4"
biceps_video = "D:\\Videos\\Workout Videos\\15 Minute Full Body HIIT Workout.mp4"
back_video = "D:\\Videos\\Workout Videos\\20 Minute Full Body Workout.mp4"
chest_video = "D:\\Videos\\Workout Videos\\15 Minute Intense Bodyweight Workout.mp4"
```

4. Change each of the variables to the **absolute** path of the video you want for each muscle group. **Double slashes (`\\`) are only required on Windows.**
5. Save the file and run the program!
