# This is the GUI frontend for the PyWorkout CLI interface. It is not yet completed.
"""
PyWORKOUT CLI
Copyright (C) 2021-2023 @willtheorangeguy

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
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as box
import time

window = Tk()

# Window Settings
window.title("PyWorkout")

# Get Percentages
def percentages(loc):
    step = 1
    percents = []
    for i in range(12):
        percent = int((step / 12) * 100)
        percents.append(percent)
        step += 1
    return str(percents[loc])


# Titles
activity = Label(window, text="ACTIVITY")
perc = Label(window, text="PERCENTAGES")
complete = Label(window, text="SELECT PERCENTAGE COMPLETE")
progress = Label(window, text="WORKOUT PROGRESS")

# Activity Labels
plank = Label(window, text="Plank:")
pushup = Label(window, text="Push Ups:")
situp = Label(window, text="Sit Ups:")
diamond = Label(window, text="Diamond Push Ups:")
squat = Label(window, text="Squats:")
wallsit = Label(window, text="Wall Sit:")

# Percentage Labels
plank1 = Label(window, text=percentages(0) + "%")
pushup1 = Label(window, text=percentages(1) + "%")
situp1 = Label(window, text=percentages(2) + "%")
diamond1 = Label(window, text=percentages(3) + "%")
squat1 = Label(window, text=percentages(4) + "%")
wallsit1 = Label(window, text=percentages(5) + "%")

plank2 = Label(window, text=percentages(6) + "%")
pushup2 = Label(window, text=percentages(7) + "%")
situp2 = Label(window, text=percentages(8) + "%")
diamond2 = Label(window, text=percentages(9) + "%")
squat2 = Label(window, text=percentages(10) + "%")
wallsit2 = Label(window, text=percentages(11) + "%")

# Percentage Complete Display
# Switch Rounds
first_round = True


def round_switch():
    global first_round
    if first_round == True:
        first_round = False
    else:
        first_round = True


round_btn = Button(window, text="Switch Activity Round", command=round_switch)
# User Selects Radiobuttons
percentage_frame = Frame(window)
activity_complete = StringVar()
radio1 = Radiobutton(
    percentage_frame, text="Plank", variable=activity_complete, value="plank"
)
radio2 = Radiobutton(
    percentage_frame, text="Push Ups", variable=activity_complete, value="pushup"
)
radio3 = Radiobutton(
    percentage_frame, text="Sit Ups", variable=activity_complete, value="situp"
)
radio4 = Radiobutton(
    percentage_frame,
    text="Diamond Push Ups",
    variable=activity_complete,
    value="diamond",
)
radio5 = Radiobutton(
    percentage_frame, text="Squats", variable=activity_complete, value="squat"
)
radio6 = Radiobutton(
    percentage_frame, text="Wall Sit", variable=activity_complete, value="wallsit"
)
# radio1.select()

# Percentage Complete Return
# Function
def percent_dialog():
    value = str(activity_complete.get())
    if value.lower() == "plank" and first_round == True:
        box.showinfo(
            "Workout Percentage",
            "You are " + percentages(0) + "%" + " complete! \nKeep it up!",
        )
        bar["value"] = percentages(0)
        window.update_idletasks()
    elif value.lower() == "pushup" and first_round == True:
        box.showinfo(
            "Workout Percentage",
            "You are " + percentages(1) + "%" + " complete! \nKeep it up!",
        )
        bar["value"] = percentages(1)
        window.update_idletasks()
    elif value.lower() == "situp" and first_round == True:
        box.showinfo(
            "Workout Percentage",
            "You are " + percentages(2) + "%" + " complete! \nKeep it up!",
        )
        bar["value"] = percentages(2)
        window.update_idletasks()
    elif value.lower() == "diamond" and first_round == True:
        box.showinfo(
            "Workout Percentage",
            "You are " + percentages(3) + "%" + " complete! \nKeep it up!",
        )
        bar["value"] = percentages(3)
        window.update_idletasks()
    elif value.lower() == "squat" and first_round == True:
        box.showinfo(
            "Workout Percentage",
            "You are " + percentages(4) + "%" + " complete! \nKeep it up!",
        )
        bar["value"] = percentages(4)
        window.update_idletasks()
    elif value.lower() == "wallsit" and first_round == True:
        box.showinfo(
            "Workout Percentage",
            "You are " + percentages(5) + "%" + " complete! \nKeep it up!",
        )
        bar["value"] = percentages(5)
        window.update_idletasks()
    elif value.lower() == "plank" and first_round == False:
        box.showinfo(
            "Workout Percentage",
            "You are " + percentages(6) + "%" + " complete! \nKeep it up!",
        )
        bar["value"] = percentages(6)
        window.update_idletasks()
    elif value.lower() == "pushup" and first_round == False:
        box.showinfo(
            "Workout Percentage",
            "You are " + percentages(7) + "%" + " complete! \nKeep it up!",
        )
        bar["value"] = percentages(7)
        window.update_idletasks()
    elif value.lower() == "situp" and first_round == False:
        box.showinfo(
            "Workout Percentage",
            "You are " + percentages(8) + "%" + " complete! \nKeep it up!",
        )
        bar["value"] = percentages(8)
        window.update_idletasks()
    elif value.lower() == "diamond" and first_round == False:
        box.showinfo(
            "Workout Percentage",
            "You are " + percentages(9) + "%" + " complete! \nKeep it up!",
        )
        bar["value"] = percentages(9)
        window.update_idletasks()
    elif value.lower() == "squat" and first_round == False:
        box.showinfo(
            "Workout Percentage",
            "You are " + percentages(10) + "%" + " complete! \nKeep it up!",
        )
        bar["value"] = percentages(10)
        window.update_idletasks()
    elif value.lower() == "wallsit" and first_round == False:
        box.showinfo(
            "Workout Percentage",
            "You are " + percentages(11) + "%" + " complete! \nKeep it up!",
        )
        bar["value"] = percentages(11)
        window.update_idletasks()
    else:
        box.showerror("Whoops", "That percentage is not possible!")


# Button
percent_button = Button(
    percentage_frame, text="Check Percentage", command=percent_dialog
)

# Percentage Progress Bar
bar = Progressbar(window, orient=HORIZONTAL, length=100, mode="determinate")
progress_info = Label(window, text=str(bar["value"]) + "%")

# Pack
activity.grid(row=1, column=1, padx=10)
perc.grid(row=1, column=2, columnspan=2, padx=10)
complete.grid(row=1, column=4, padx=10)
progress.grid(row=1, column=5, padx=10)

plank.grid(row=2, column=1, padx=10)
pushup.grid(row=3, column=1, padx=10)
situp.grid(row=4, column=1, padx=10)
diamond.grid(row=5, column=1, padx=10)
squat.grid(row=6, column=1, padx=10)
wallsit.grid(row=7, column=1, padx=10)

plank1.grid(row=2, column=2, padx=10)
pushup1.grid(row=3, column=2, padx=10)
situp1.grid(row=4, column=2, padx=10)
diamond1.grid(row=5, column=2, padx=10)
squat1.grid(row=6, column=2, padx=10)
wallsit1.grid(row=7, column=2, padx=10)

plank2.grid(row=2, column=3, padx=10)
pushup2.grid(row=3, column=3, padx=10)
situp2.grid(row=4, column=3, padx=10)
diamond2.grid(row=5, column=3, padx=10)
squat2.grid(row=6, column=3, padx=10)
wallsit2.grid(row=7, column=3, padx=10)

round_btn.grid(row=2, column=4, padx=10, pady=5)
radio1.pack(side=TOP)
radio2.pack(side=TOP)
radio3.pack(side=TOP)
radio4.pack(side=TOP)
radio5.pack(side=TOP)
radio6.pack(side=TOP)
percent_button.pack(side=TOP, pady=5)
percentage_frame.grid(row=3, rowspan=5, column=4, padx=10)

bar.grid(row=2, column=5, padx=10, pady=5)
progress_info.grid(row=3, column=5, padx=10)

# Sustain Window
window.mainloop()
