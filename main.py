# PyWORKOUT CLI
# (C) 2021 - 2022

# Import Statements
import subprocess
from datetime import datetime 
import time 

# Workout Lists
groups = ["Abs", "Quads", "Glutes", "Triceps", "Biceps", "Back", "Chest"]
sunday = ["Situps", "Reverse Crunches", "Bicycle Crunches", "Flutter Kicks", "Leg Raises", "Elbow Planks"]
sunday_count = [25, 25, 25, 25, 25, 4]
monday = ["Lunges", "High Knees", "Side Kicks", "Mountain Climbers", "Plank Jump Ins", "Lunges & Step Ups"]
monday_count = [50, 50, 50, 25, 25, 50]
tuesday = ["Squats", "Donkey Kicks", "Bridges", "Step Ups", "Fly Steps", "Side Leg Raises"]
tuesday_count = [25, 25, 25, 25, 50, 50]
wednesday = ["Diamond Pushups", "Tricep Dips", "Tricep Extensions", "Get Ups", "Punches", "Side to Side Chops"]
wednesday_count = [25, 25, 25, 50, 50, 50]
thursday = ["Backlists", "Doorframe Rows", "Decline Pushups", "Side Plank", "Pushups"]
thursday_count = [50, 50, 25, 4, 25]
friday = ["Scapular Shrugs", "Supermans", "Back Lifts", "Aternating Arm/Leg Plank", "Reverse Angels"]
friday_count = [25, 25, 25, 4, 25]
saturday = ["Pushups", "Chest Expansions", "Chest Squeezes", "Pike Pushups", "Shoulder Taps"]
thursday_count = [25, 25, 25, 25, 25, 25]
complete = []

# Videos 
def openvideo():
    sunday = subprocess.Popen(["C:\Program Files\VideoLAN\VLC\vlc.exe", "file:\\\D:\Videos\Workout Videos\10 Minute Ab Workout.mp4"])

# Welcome
print("         WELCOME TO PyWORKOUT")
print("Please select a group from those below. \n")
for i in range(len(groups)):
    print(str(i+1) + ". " + str(groups[i]))
print("A reminder that today is: " + datetime.today().strftime('%A') + ". Consider option " + str((datetime.today().strftime('%w'))+1))

# Display Workout Options
run_options = True
while run_options == True:
    select = str(input("Group? "))
    if select.lower() == "1" or select.lower() == "abs":
        print("\nAb group selected!")
        run_options = False
    elif select.lower() == "2" or select.lower() == "quads":
        print("\nQuad group selected!")
        run_options = False
    elif select.lower() == "3" or select.lower() == "glutes":
        print("\nGlutes group selected!")
        run_options = False
    elif select.lower() == "4" or select.lower() == "triceps":
        print("\nTricep group selected!")
        run_options = False
    elif select.lower() == "5" or select.lower() == "biceps":
        print("\nBicep group selected!")
        run_options = False
    elif select.lower() == "6" or select.lower() == "back":
        print("\nBack group selected!")
        run_options = False
    elif select.lower() == "7" or select.lower() == "chest":
        print("\nChest group selected!")
        run_options = False
    else:
        print("Sorry that is incorrect. Please try again!")
        run_options = True

# Ask What They Want to Do
run_activity = True
while run_activity == True:
    activity = str(input("What do you want to do? "))
    if activity.lower() == "start":
        start_time = time.gettime()
        print("Starting Workout...")
    elif activity.lower() == "list":
        print("Listing activities...")
    elif activity.lower() == "percent":
        print("Percent complete and to go")
    elif activity.lower() == "done":
        print("Workout finished")
