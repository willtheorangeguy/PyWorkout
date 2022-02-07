# PyWORKOUT CLI
# (C) 2021 - 2022

# Workout Options
# Item complete - show time completed, start new time, show percentage, move to next workout
# Workout finished - show total time, activities completed
# Stats - time, percentage complete
# Video - play video for that group

# Import Statements
import subprocess
from datetime import datetime, date 
import time

# Workout Lists
groups = ["Abs", "Quads", "Glutes", "Triceps", "Biceps", "Back", "Chest"]
abs = ["Situps\t", "Reverse Crunches", "Bicycle Crunches", "Flutter Kicks", "Leg Raises\t", "Elbow Planks\t"]
sunday_count = [25, 25, 25, 25, 25, 2]
monday = ["Lunges\t", "High Knees\t", "Side Kicks\t", "Mountain Climbers", "Plank Jump Ins", "Lunges & Step Ups"]
monday_count = [50, 50, 50, 25, 25, 50]
tuesday = ["Squats\t", "Donkey Kicks\t", "Bridges\t", "Step Ups\t", "Fly Steps\t", "Side Leg Raises"]
tuesday_count = [25, 25, 25, 25, 50, 50]
wednesday = ["Diamond Pushups", "Tricep Dips\t", "Tricep Extensions", "Get Ups\t", "Punches\t", "Side to Side Chops"]
wednesday_count = [25, 25, 25, 50, 50, 50]
thursday = ["Backlists\t", "Doorframe Rows", "Decline Pushups", "Side Plank\t", "Pushups\t"]
thursday_count = [50, 50, 25, 2, 25]
friday = ["Scapular Shrugs", "Supermans\t", "Back Lifts\t", "Arm/Leg Plank", "Reverse Angels"]
friday_count = [25, 25, 25, 2, 25]
saturday = ["Pushups\t", "Chest Expansions", "Chest Squeezes", "Pike Pushups\t", "Shoulder Taps"]
saturday_count = [25, 25, 25, 25, 25, 25]
complete = []

# Videos 
def openvideo():
    sunday = subprocess.Popen(["C:\Program Files\VideoLAN\VLC\vlc.exe", "file:\\\D:\Videos\Workout Videos\10 Minute Ab Workout.mp4"])

# Percentage
def percent(group, no):
    num = int((no/len(group))*100)
    num = str(num) + "%"
    return num 

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
        print("Sorry that is incorrect. Please try again!")
        run_options = True

# Ask What They Want to Do
run_activity = True
while run_activity == True:
    activity = str(input("What do you want to do? "))
    if activity.lower() == "list":
        if select == "abs":
            for i in range(len(sunday)):
                print(str(i+1) + ". " + str(sunday[i]) + "\t 2 Sets of " + str(sunday_count[i]) + " Reps")
            print("")
        elif select == "quads":
            for i in range(len(monday)):
                print(str(i+1) + ". " + str(monday[i]) + "\t 2 Sets of " + str(monday_count[i]) + " Reps")
            print("")
        elif select == "glutes":
            for i in range(len(tuesday)):
                print(str(i+1) + ". " + str(tuesday[i]) + "\t 2 Sets of " + str(tuesday_count[i]) + " Reps")
            print("")
        elif select == "triceps":
            for i in range(len(wednesday)):
                print(str(i+1) + ". " + str(wednesday[i]) + "\t 2 Sets of " + str(wednesday_count[i]) + " Reps")
            print("")
        elif select == "biceps":
            for i in range(len(thursday)):
                print(str(i+1) + ". " + str(thursday[i]) + "\t 2 Sets of " + str(thursday_count[i]) + " Reps")
            print("")
        elif select == "back":
            for i in range(len(friday)):
                print(str(i+1) + ". " + str(friday[i]) + "\t 2 Sets of " + str(friday_count[i]) + " Reps")
            print("")
        elif select == "chest":
            for i in range(len(saturday)):
                print(str(i+1) + ". " + str(saturday[i]) + "\t 2 Sets of " + str(saturday_count[i]) + " Reps")
            print("")
        run_activity = True 
    elif activity.lower() == "start":
        global activity_num
        global start_time 
        start_time = date.today()
        activity_num = 0
        print("You have started the " + select + " muscle group. ")
        print("The current time is: " + str(time.strftime("%H:%M:%S")) + " - " + str(date.today()-start_time) + " has elapsed.")
        print("You have completed: " + percent(select, 0))
        if select == "abs":
            print("Please complete 2 Sets of " + str(sunday_count[activity_num]) + " Reps of " + str(abs[activity_num]))
        elif select == "quads":
            for i in range(len(monday)):
                print(str(i+1) + ". " + str(monday[i]) + "\t 2 Sets of " + str(monday_count[i]))
            print("")
        elif select == "glutes":
            for i in range(len(tuesday)):
                print(str(i+1) + ". " + str(tuesday[i]) + "\t 2 Reps of " + str(tuesday_count[i]))
            print("")
        elif select == "triceps":
            for i in range(len(wednesday)):
                print(str(i+1) + ". " + str(wednesday[i]) + "\t 2 Reps of " + str(wednesday_count[i]))
            print("")
        elif select == "biceps":
            for i in range(len(thursday)):
                print(str(i+1) + ". " + str(thursday[i]) + "\t 2 Reps of " + str(thursday_count[i]))
            print("")
        elif select == "back":
            for i in range(len(friday)):
                print(str(i+1) + ". " + str(friday[i]) + "\t 2 Reps of " + str(friday_count[i]))
            print("")
        elif select == "chest":
            for i in range(len(saturday)):
                print(str(i+1) + ". " + str(saturday[i]) + "\t 2 Reps of " + str(saturday_count[i]))
            print("")
        print("")
        activity_num = activity_num + 1
        run_activity = True 
    elif activity.lower() == "next":
        print("You are in the " + select + " muscle group. ")
        print("The current time is: " + str(time.strftime("%H:%M:%S")) + " - " + str(date.today()-start_time) + " has elapsed.")
        print("You have completed: " + percent(select, activity_num))
        if select == "abs":
            print("Please complete 2 Sets of " + str(sunday_count[activity_num]) + " Reps of " + str(sunday[activity_num]))
        elif select == "quads":
            for i in range(len(monday)):
                print(str(i+1) + ". " + str(monday[i]) + "\t 2 Sets of " + str(monday_count[i]))
            print("")
        elif select == "glutes":
            for i in range(len(tuesday)):
                print(str(i+1) + ". " + str(tuesday[i]) + "\t 2 Reps of " + str(tuesday_count[i]))
            print("")
        elif select == "triceps":
            for i in range(len(wednesday)):
                print(str(i+1) + ". " + str(wednesday[i]) + "\t 2 Reps of " + str(wednesday_count[i]))
            print("")
        elif select == "biceps":
            for i in range(len(thursday)):
                print(str(i+1) + ". " + str(thursday[i]) + "\t 2 Reps of " + str(thursday_count[i]))
            print("")
        elif select == "back":
            for i in range(len(friday)):
                print(str(i+1) + ". " + str(friday[i]) + "\t 2 Reps of " + str(friday_count[i]))
            print("")
        elif select == "chest":
            for i in range(len(saturday)):
                print(str(i+1) + ". " + str(saturday[i]) + "\t 2 Reps of " + str(saturday_count[i]))
            print("")
        print("")
        activity_num = activity_num + 1
        run_activity = True 
    elif activity.lower() == "quit":
        run_activity = False
        exit()
        break 
    else:
        print("Sorry that is not an option. Please see this list of options below:")
        run_activity = True 
