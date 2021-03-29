# Import Statements
from tkinter import *
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

# Percentage Complete Display
# Switch Rounds
first_round = True
def round_switch():
    global first_round
    if first_round == True:
        first_round = False
    else:
        first_round = True
round_btn = Button(window, text = "Switch Activity Round", command = round_switch)
# User Selects
complete = Label(window, text = "SELECT PERCENTAGE COMPLETE")
percentage_frame = Frame(window)
activity_complete = StringVar()
radio1 = Radiobutton(percentage_frame, text = "Plank", variable = activity_complete, value = "plank")
radio2 = Radiobutton(percentage_frame, text = "Push Ups", variable = activity_complete, value = "pushup")
radio3 = Radiobutton(percentage_frame, text = "Sit Ups", variable = activity_complete, value = "situp")
radio4 = Radiobutton(percentage_frame, text = "Diamond Push Ups", variable = activity_complete, value = "diamond")
radio5 = Radiobutton(percentage_frame, text = "Squats", variable = activity_complete, value = "squat")
radio6 = Radiobutton(percentage_frame, text = "Wall Sit", variable = activity_complete, value = "wallsit")
radio1.select()

# Percentage Complete Return
# Function
def percent_dialog():
    value = str(activity_complete.get())
    if value.lower() == "plank" and first_round == True:
        box.showinfo("Workout Percentage", "You are " + percentages(0)+"%" + " complete! \n Keep it up!")
    elif value.lower() == "pushup" and first_round == True:
        box.showinfo("Workout Percentage", "You are " + percentages(1)+"%" + " complete! \n Keep it up!")
    elif value.lower() == "situp" and first_round == True:
        box.showinfo("Workout Percentage", "You are " + percentages(2)+"%" + " complete! \n Keep it up!")
    elif value.lower() == "diamond" and first_round == True:
        box.showinfo("Workout Percentage", "You are " + percentages(3)+"%" + " complete! \n Keep it up!")
    elif value.lower() == "squat" and first_round == True:
        box.showinfo("Workout Percentage", "You are " + percentages(4)+"%" + " complete! \n Keep it up!")
    elif value.lower() == "wallsit" and first_round == True:
        box.showinfo("Workout Percentage", "You are " + percentages(5)+"%" + " complete! \n Keep it up!")
    elif value.lower() == "plank" and first_round == False:
        box.showinfo("Workout Percentage", "You are " + percentages(6)+"%" + " complete! \n Keep it up!")
    elif value.lower() == "pushup" and first_round == False:
        box.showinfo("Workout Percentage", "You are " + percentages(7)+"%" + " complete! \n Keep it up!")
    elif value.lower() == "situp" and first_round == False:
        box.showinfo("Workout Percentage", "You are " + percentages(8)+"%" + " complete! \n Keep it up!")
    elif value.lower() == "diamond" and first_round == False:
        box.showinfo("Workout Percentage", "You are " + percentages(9)+"%" + " complete! \n Keep it up!")
    elif value.lower() == "squat" and first_round == False:
        box.showinfo("Workout Percentage", "You are " + percentages(10)+"%" + " complete! \n Keep it up!")
    elif value.lower() == "wallsit" and first_round == False:
        box.showinfo("Workout Percentage", "You are " + percentages(11)+"%" + " complete! \n Keep it up!")
    else:
        box.showerror("Whoops", "That percentage is not possible!")

# Button
percent_button = Button(percentage_frame, text = "Check Percentage", command = percent_dialog)

# Pack
activity.grid(row = 1, column = 1, padx = 10)
perc.grid(row = 1, column = 2, columnspan = 2, padx = 10)
complete.grid(row = 1, column = 4, padx = 10)

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

round_btn.grid(row = 2, column = 4, padx = 10)
radio1.pack(side = TOP)
radio2.pack(side = TOP)
radio3.pack(side = TOP)
radio4.pack(side = TOP)
radio5.pack(side = TOP)
radio6.pack(side = TOP)
percent_button.pack(side = TOP)
percentage_frame.grid(row = 3, rowspan = 5, column = 4, padx = 10)

# Sustain Window
window.mainloop()