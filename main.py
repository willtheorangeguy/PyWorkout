"""
PyWORKOUT CLI
Copyright (C) 2021-2022  @willtheorangeguy

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# Import Statements
from datetime import datetime
import time
import os
import sys
import subprocess

# PyWorkout Function
def workout():
    # Workout Lists
    groups = ["Abs", "Quads", "Glutes", "Triceps", "Biceps", "Back", "Chest"]
    abs = ["Situps\t", "Reverse Crunches", "Bicycle Crunches", "Flutter Kicks", "Leg Raises\t", "Elbow Planks\t"]
    abs_count = [25, 25, 25, 25, 25, 2]
    quads = ["Lunges\t", "High Knees\t", "Side Kicks\t", "Mountain Climbers", "Plank Jump Ins", "Lunges & Step Ups"]
    quads_count = [50, 50, 50, 25, 25, 50]
    glutes = ["Squats\t", "Donkey Kicks\t", "Bridges\t", "Step Ups\t", "Fly Steps\t", "Side Leg Raises"]
    glutes_count = [25, 25, 25, 25, 50, 50]
    triceps = ["Diamond Pushups", "Tricep Dips\t", "Tricep Extensions", "Get Ups\t", "Punches\t", "Side to Side Chops"]
    triceps_count = [25, 25, 25, 50, 50, 50]
    biceps = ["Backlists\t", "Doorframe Rows", "Decline Pushups", "Side Plank\t", "Pushups\t"]
    biceps_count = [50, 50, 25, 2, 25]
    back = ["Scapular Shrugs", "Supermans\t", "Back Lifts\t", "Arm/Leg Plank", "Reverse Angels"]
    back_count = [25, 25, 25, 2, 25]
    chest = ["Pushups\t", "Chest Expansions", "Chest Squeezes", "Pike Pushups\t", "Shoulder Taps"]
    chest_count = [25, 25, 25, 25, 25, 25]
    complete = []
    times = []

    # Video File Paths
    abs_video = "D:\\Videos\\Workout Videos\\10 Minute Ab Workout.mp4" # change these to personal video path
    quads_video = "D:\\Videos\\Workout Videos\\12 Min Leg Workout.mp4"
    glutes_video = "D:\\Videos\\Workout Videos\\10 Minute Glute Bridge Workout.mp4"
    triceps_video = "D:\\Videos\\Workout Videos\\10 Minute Upper Body Workout.mp4"
    biceps_video = "D:\\Videos\\Workout Videos\\15 Minute Full Body HIIT Workout.mp4"
    back_video = "D:\\Videos\\Workout Videos\\20 Minute Full Body Workout.mp4"
    chest_video = "D:\\Videos\\Workout Videos\\15 Minute Intense Bodyweight Workout.mp4"

    # Video Function
    def video(path):
        if sys.platform == "win32":
            os.startfile(path)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, path])   

    # Welcome
    print("         WELCOME TO PyWORKOUT")
    print("Please select a group from those below.")
    for i in range(len(groups)):
        print(str(i+1) + ". " + str(groups[i]))
    print("A reminder that today is: " + datetime.today().strftime('%A') + ". Consider option " + str(int(datetime.today().strftime('%w')) + 1) + ".")

    # Display Workout Options
    run_options = True
    while run_options == True:
        global select 
        select = str(input("\nGroup? "))
        if select.lower() == "1" or select.lower() == "abs":
            print("Ab muscle group selected!\n")
            select = "abs"
            run_options = False
        elif select.lower() == "2" or select.lower() == "quads":
            print("Quad muscle group selected!\n")
            select = "quads"
            run_options = False
        elif select.lower() == "3" or select.lower() == "glutes":
            print("Glutes muscle group selected!\n")
            select = "glutes"
            run_options = False
        elif select.lower() == "4" or select.lower() == "triceps":
            print("Tricep muscle group selected!\n")
            select = "triceps"
            run_options = False
        elif select.lower() == "5" or select.lower() == "biceps":
            print("Bicep muscle group selected!\n")
            select = "biceps"
            run_options = False
        elif select.lower() == "6" or select.lower() == "back":
            print("Back muscle group selected!\n")
            select = "back"
            run_options = False
        elif select.lower() == "7" or select.lower() == "chest":
            print("Chest muscle group selected!\n")
            select = "chest"
            run_options = False
        elif select.lower() == "quit":
            exit()
            break 
        else:
            print("Sorry that is incorrect. Please try again! \n")
            run_options = True

    # Ask What They Want to Do
    run_activity = True
    while run_activity == True:
        activity = str(input("What do you want to do? "))
        if activity.lower() == "list":
            if select == "abs":
                for i in range(len(abs)):
                    print(str(i+1) + ". " + str(abs[i]) + "\t 2 Sets of " + str(abs_count[i]) + " Reps")
            elif select == "quads":
                for i in range(len(quads)):
                    print(str(i+1) + ". " + str(quads[i]) + "\t 2 Sets of " + str(quads_count[i]) + " Reps")
            elif select == "glutes":
                for i in range(len(glutes)):
                    print(str(i+1) + ". " + str(glutes[i]) + "\t 2 Sets of " + str(glutes_count[i]) + " Reps")
            elif select == "triceps":
                for i in range(len(glutes)):
                    print(str(i+1) + ". " + str(triceps[i]) + "\t 2 Sets of " + str(triceps_count[i]) + " Reps")
            elif select == "biceps":
                for i in range(len(biceps)):
                    print(str(i+1) + ". " + str(biceps[i]) + "\t 2 Sets of " + str(biceps_count[i]) + " Reps")
            elif select == "back":
                for i in range(len(back)):
                    print(str(i+1) + ". " + str(back[i]) + "\t 2 Sets of " + str(back_count[i]) + " Reps")
            elif select == "chest":
                for i in range(len(chest)):
                    print(str(i+1) + ". " + str(chest[i]) + "\t 2 Sets of " + str(chest_count[i]) + " Reps")
            print("")
            run_activity = True 
        elif activity.lower() == "start":
            global activity_num
            activity_num = 0
            global start
            start = datetime.now()
            times.append(start)
            print("You have started the " + select + " muscle group. ")
            print("The current time is: " + str(time.strftime("%H:%M:%S")))
            if select == "abs":
                print("You have completed: " + str((int(activity_num/len(abs_count)))) + "%")
                print("Please complete 2 Sets of " + str(abs_count[activity_num]) + " Reps of " + str(abs[activity_num]))
                complete.append(abs[activity_num])
            elif select == "quads":
                print("You have completed: " + str((int(activity_num/len(quads_count)))) + "%")
                print("Please complete 2 Sets of " + str(quads_count[activity_num]) + " Reps of " + str(quads[activity_num]))
                complete.append(quads[activity_num])
            elif select == "glutes":
                print("You have completed: " + str((int(activity_num/len(glutes_count)))) + "%")
                print("Please complete 2 Sets of " + str(glutes_count[activity_num]) + " Reps of " + str(glutes[activity_num]))
                complete.append(glutes[activity_num])
            elif select == "triceps":
                print("You have completed: " + str((int(activity_num/len(triceps_count)))) + "%")
                print("Please complete 2 Sets of " + str(triceps_count[activity_num]) + " Reps of " + str(triceps[activity_num]))
                complete.append(triceps[activity_num])
            elif select == "biceps":
                print("You have completed: " + str((int(activity_num/len(biceps_count)))) + "%")
                print("Please complete 2 Sets of " + str(biceps_count[activity_num]) + " Reps of " + str(biceps[activity_num]))
                complete.append(biceps[activity_num])
            elif select == "back":
                print("You have completed: " + str((int(activity_num/len(back_count)))) + "%")
                print("Please complete 2 Sets of " + str(back_count[activity_num]) + " Reps of " + str(back[activity_num]))
                complete.append(back[activity_num])
            elif select == "chest":
                print("You have completed: " + str((int(activity_num/len(chest_count)))) + "%")
                print("Please complete 2 Sets of " + str(chest_count[activity_num]) + " Reps of " + str(chest[activity_num]))
                complete.append(chest[activity_num])
            print("")
            activity_num = activity_num + 1
            run_activity = True 
        elif activity.lower() == "next":
            now = datetime.now()
            times.append(now)
            print("You are in the " + select + " muscle group. ")
            print("The current time is: " + str(time.strftime("%H:%M:%S")) + ". " + str(now-start) + " has elapsed.")
            if select == "abs":
                if activity_num < 6:
                    print("You have completed: " + str((int(activity_num/len(abs_count)*100))) + "%")
                    print("Please complete 2 Sets of " + str(abs_count[activity_num]) + " Reps of " + str(abs[activity_num]) + "\n")
                    complete.append(abs[activity_num])
                else:
                    print("You have completed all the workouts for this set!")
                    print("Run the `end` command to finish the workout. \n")
            elif select == "quads":
                if activity_num < 6:
                    print("You have completed: " + str((int(activity_num/len(quads_count)*100))) + "%")
                    print("Please complete 2 Sets of " + str(quads_count[activity_num]) + " Reps of " + str(quads[activity_num]) + "\n")
                    complete.append(quads[activity_num])
                else:
                    print("You have completed all the workouts for this set!")
                    print("Run the `end` command to finish the workout. \n")
            elif select == "glutes":
                if activity_num < 6:
                    print("You have completed: " + str((int(activity_num/len(glutes_count)*100))) + "%")
                    print("Please complete 2 Sets of " + str(glutes_count[activity_num]) + " Reps of " + str(glutes[activity_num]) + "\n")
                    complete.append(glutes[activity_num])
                else:
                    print("You have completed all the workouts for this set!")
                    print("Run the `end` command to finish the workout. \n")
            elif select == "triceps":
                if activity_num < 6:
                    print("You have completed: " + str((int(activity_num/len(triceps_count)*100))) + "%")
                    print("Please complete 2 Sets of " + str(triceps_count[activity_num]) + " Reps of " + str(triceps[activity_num]) + "\n")
                    complete.append(triceps[activity_num])
                else:
                    print("You have completed all the workouts for this set!")
                    print("Run the `end` command to finish the workout. \n")
            elif select == "biceps":
                if activity_num < 5:
                    print("You have completed: " + str((int(activity_num/len(biceps_count)*100))) + "%")
                    print("Please complete 2 Sets of " + str(biceps_count[activity_num]) + " Reps of " + str(biceps[activity_num]) + "\n")
                    complete.append(biceps[activity_num])
                else:
                    print("You have completed all the workouts for this set!")
                    print("Run the `end` command to finish the workout. \n")
            elif select == "back":
                if activity_num < 5:
                    print("You have completed: " + str((int(activity_num/len(back_count)*100))) + "%")
                    print("Please complete 2 Sets of " + str(back_count[activity_num]) + " Reps of " + str(back[activity_num]) + "\n")
                    complete.append(back[activity_num])
                else:
                    print("You have completed all the workouts for this set!")
                    print("Run the `end` command to finish the workout. \n")
            elif select == "chest":
                if activity_num < 6:
                    print("You have completed: " + str((int(activity_num/len(chest_count)*100))) + "%")
                    print("Please complete 2 Sets of " + str(chest_count[activity_num]) + " Reps of " + str(chest[activity_num]) + "\n")
                    complete.append(chest[activity_num])
                else:
                    print("You have completed all the workouts for this set!")
                    print("Run the `end` command to finish the workout. \n")
            activity_num = activity_num + 1
            run_activity = True 
        elif activity.lower() == "skip":
            now = datetime.now()
            print("You are in the " + select + " muscle group. ")
            print("The current time is: " + str(time.strftime("%H:%M:%S")) + ". " + str(now-start) + " has elapsed.")
            complete.pop(-1)
            times.pop(-1)
            print("Activity skipped! Run the `next` command to move on. \n")
            run_activity = True
        elif activity.lower() == "end":
            now = datetime.now()
            times.append(now)
            print("You have completed the " + select + " muscle group.")
            print("It took " + str(now-start) + " to complete this workout.")
            print("The following activities were completed (time elapsed):")
            for i in range(len(complete)):
                print(str(i+1) + ". " + str(complete[i]) + "\t(" + str(times[i+1]-times[i]) + ")")
            print("Congratulations! \n")
            run_activity = True
        elif activity.lower() == "stats":
            try:
                now = datetime.now()
                times.append(now)
                print("You are in the " + select + " muscle group. ")
                print("The current time is: " + str(time.strftime("%H:%M:%S")) + ". " + str(now-start) + " has elapsed.")
                print("The following activities have been completed (time elapsed):")
                for i in range(len(complete)):
                    print(str(i+1) + ". " + str(complete[i]) + "\t(" + str(times[i+1]-times[i]) + ")")
                print("The following activities still need to be completed:")
                if select == "abs":
                    for i in range(len(abs)-len(complete)):
                        print(str(i+1) + ". " + str(abs[i+activity_num]))
                elif select == "quads":
                    for i in range(len(quads)-len(complete)):
                        print(str(i+1) + ". " + str(quads[i+activity_num]))
                elif select == "glutes":
                    for i in range(len(glutes)-len(complete)):
                        print(str(i+1) + ". " + str(glutes[i+activity_num]))
                elif select == "triceps":
                    for i in range(len(triceps)-len(complete)):
                        print(str(i+1) + ". " + str(triceps[i+activity_num]))
                elif select == "biceps":
                    for i in range(len(biceps)-len(complete)):
                        print(str(i+1) + ". " + str(biceps[i+activity_num]))
                elif select == "back":
                    for i in range(len(back)-len(complete)):
                        print(str(i+1) + ". " + str(back[i+activity_num]))
                elif select == "chest":
                    for i in range(len(chest)-len(complete)):
                        print(str(i+1) + ". " + str(chest[i+activity_num]))
                print("")
            except IndexError:
                print("You cannot use both the `skip` and `stats` commands, sorry! \n")
            run_activity = True
        elif activity.lower() == "video":
            now = datetime.now()
            times.append(now)
            print("You are in the " + select + " muscle group. ")
            print("The current time is: " + str(time.strftime("%H:%M:%S")) + ". " + str(now-start) + " has elapsed.")
            if select == "abs":
                video(abs_video)
                complete.append("Abs Video \t")
            elif select == "quads":
                video(quads_video)
                complete.append("Quads Video \t")
            elif select == "glutes":
                video(glutes_video)
                complete.append("Glutes Video")
            elif select == "triceps":
                video(triceps_video)
                complete.append("Triceps Video")
            elif select == "biceps":
                video(biceps_video)
                complete.append("Biceps Video\t")
            elif select == "back":
                video(back_video)
                complete.append("Back Video \t")
            elif select == "chest":
                video(chest_video)
                complete.append("Chest Video \t")
            print("")
            run_activity = True
        elif activity.lower() == "license":
            print("PyWorkout Copyright (C) 2021-2022  @willtheorangeguy")
            print("This program comes with ABSOLUTELY NO WARRANTY; for details view the license.")
            print("This is free software, and you are welcome to redistribute it")
            print("under certain conditions; view the license for details. \n")
        elif activity.lower() == "quit":
            run_activity = False
            exit()
            break 
        elif activity.lower() == "help":
            print("PyWorkout - (C) 2021-2022")
            print("Any of these options are available: ")
            print("list    Lists the workout activities by muscle group.")
            print("start   Starts the workout and displays the first workout activity.")
            print("next    Moves to the next workout activity.")
            print("skip    Skips the current workout activity.")
            print("end     Completes the workout and display full workout statistics.")
            print("stats   Shows workout statistics at any point (does not work with the `skip` command).")
            print("video   Opens the workout video assigned to each muscle group.")
            print("license Show the license.")
            print("help    Prints this help text.")
            print("quit    Ends the program.")
            print("More documentation can be found on Github. Enjoy using the program! \n")
            run_activity = True
        else:
            print("Sorry that is not an option. Please see this list of options below:")
            print("list    Lists the workout activities by muscle group.")
            print("start   Starts the workout and displays the first workout activity.")
            print("next    Moves to the next workout activity.")
            print("skip    Skips the current workout activity.")
            print("end     Completes the workout and display full workout statistics.")
            print("stats   Shows workout statistics at any point.")
            print("video   Opens the workout video assigned to each muscle group.")
            print("license Show the license.")
            print("help    Prints a similar help text.")
            print("quit    Ends the program. \n")
            run_activity = True

if __name__ == '__main__':
    workout()
