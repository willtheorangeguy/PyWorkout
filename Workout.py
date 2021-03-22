# Import Statements
from tkinter import *
import time
window = Tk()

# Window Settings
window.title("PyWorkout")

# Get Percentages
def percentages(loc):
    step = 1
    percents = []
    for i in range(12):
        percent = int((step / 12)*100)
        percents.append(percent)
        step += 1
    return str(percents[loc])

# Titles
activity = Label(window, text="ACTIVITY")
perc = Label(window, text="PERCENTAGES")

# Activity Labels
plank = Label(window, text="Plank:")
pushup = Label(window, text="Push Ups:")
situp = Label(window, text="Sit Ups:")
diamond = Label(window, text="Diamond Push Ups:")
squat = Label(window, text="Squats:")
wallsit = Label(window, text="Wall Sit:")

# Percentage Labels
plank1 = Label(window, text=percentages(0)+"%")
pushup1 = Label(window, text=percentages(1)+"%")
situp1 = Label(window, text=percentages(2)+"%")
diamond1 = Label(window, text=percentages(3)+"%")
squat1 = Label(window, text=percentages(4)+"%")
wallsit1 = Label(window, text=percentages(5)+"%")

plank2 = Label(window, text=percentages(6)+"%")
pushup2 = Label(window, text=percentages(7)+"%")
situp2 = Label(window, text=percentages(8)+"%")
diamond2 = Label(window, text=percentages(9)+"%")
squat2 = Label(window, text=percentages(10)+"%")
wallsit2 = Label(window, text=percentages(11)+"%")

# Total Timer
btnstart = Button(window, text = "Start Timer")
timer = Label(window, text = "00:00")
btnend = Button(window, text = "End Timer")

# Timer Backend
def starttime():
    global now
    now = time.time()

def endtime():
    end = time.time()
    global now
    total = round((end - now), 2)
    min_total = 00
    while total >=60:
        if total >= 60:
            min_total += 1
            total -= 60
    timer.configure(text = (str(min_total)+ ":" + str(round(total, 2))))

btnstart.configure(command = starttime)
btnend.configure(command = endtime)

# Pack
activity.grid(row = 1, column = 1, padx = 10)
perc.grid(row = 1, column = 2, columnspan = 2, padx = 10)

plank.grid(row = 2, column = 1, padx = 10)
pushup.grid(row = 3, column = 1, padx = 10)
situp.grid(row = 4, column = 1, padx = 10)
diamond.grid(row = 5, column = 1, padx = 10)
squat.grid(row = 6, column = 1, padx = 10)
wallsit.grid(row = 7, column = 1, padx = 10)

plank1.grid(row = 2, column = 2, padx = 10)
pushup1.grid(row = 3, column = 2, padx = 10)
situp1.grid(row = 4, column = 2, padx = 10)
diamond1.grid(row = 5, column = 2, padx = 10)
squat1.grid(row = 6, column = 2, padx = 10)
wallsit1.grid(row = 7, column = 2, padx = 10)

plank2.grid(row = 2, column = 3, padx = 10)
pushup2.grid(row = 3, column = 3, padx = 10)
situp2.grid(row = 4, column = 3, padx = 10)
diamond2.grid(row = 5, column = 3, padx = 10)
squat2.grid(row = 6, column = 3, padx = 10)
wallsit2.grid(row = 7, column = 3, padx = 10)

btnstart.grid(row = 8, column = 1, padx = 10, pady = 10)
timer.grid(row = 8, column = 2, padx = 10, pady = 10)
btnend.grid(row = 8, column = 3, padx = 10, pady = 10)

# Sustain Window
window.mainloop()