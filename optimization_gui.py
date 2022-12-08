# imports tkinter (Python GUI library)
import tkinter as tk
# imports find_optimal_gears.py to utilize find_optimal_gears function
from find_optimal_gears import *

# creates window object and sets its title, background color, and dimensions
window = tk.Tk()
window.title("Gear Script")
window.configure(background="black")
window.geometry("500x500") # "widthxheight"

# function that returns created label, taking the label text as a parameter
def createLabel(t):
    return tk.Label(window, text=t, bg="black", fg="white")
# function that returns created entry box
def createEntry():
    return tk.Entry(window, width=15, bg="white", justify="center")
# function that returns created button, taking button text
def createButton(t):
    return tk.Button(window, text=t, width=10)
# function that returns created button for toggling between inputting ranges and single values
def createToggle():
    return createButton("Single Value")

# creates all gui widgets
teeth_label = createLabel("Tooth Count")
min_teeth_entry = createEntry()
max_teeth_entry = createEntry()
teeth_toggle = createToggle()

planets_label = createLabel("Number of Planets in Carrier")
min_planets_entry = createEntry()
max_planets_entry = createEntry()
planets_toggle = createToggle()

diametral_pitch_label = createLabel("Diametral Pitch")
diametral_pitch_entry = createEntry()

generate_button = createButton("Generate")

message_label = createLabel("asdf")
# configures message label so that text wraps
message_label.configure(wraplength=200)

# function that toggles tooth count range/single value
def toggleText(btn):
    text = btn.cget('text')
    if (text == "Single Value"):
        btn.configure(text = "Range")
    else:
        btn.configure(text = "Single Value")
# function that toggles entry boxes, taking the high end entry box, its row, and its column
def toggleEntry(high, r, c):
    # if the high end range is visible, hide it
    if (high.grid_info()):
        high.grid_remove()
    # otherwise, show it
    else:
        high.grid(row = r, column = c)
# function that toggles text and entry boxes for teeth
def toggleTeeth():
    toggleText(teeth_toggle)
    toggleEntry(max_teeth_entry, 1, 1)
# function that toggles text and entry boxes for planets
def togglePlanets():
    toggleText(planets_toggle)
    toggleEntry(max_planets_entry, 3, 1)
    
teeth_toggle.configure(command=toggleTeeth)
planets_toggle.configure(command=togglePlanets)

# lays all gui widgets out in a grid format
teeth_label.grid(row = 0, column = 0)
min_teeth_entry.grid(row = 1, column = 0)
max_teeth_entry.grid(row = 1, column = 1)
teeth_toggle.grid(row = 1, column = 2)

planets_label.grid(row = 2, column = 0)
min_planets_entry.grid(row = 3, column = 0)
max_planets_entry.grid(row = 3, column = 1)
planets_toggle.grid(row = 3, column = 2)

diametral_pitch_label.grid(row = 4, column = 0)
diametral_pitch_entry.grid(row = 5, column = 0)

generate_button.grid(row = 6, column = 0, columnspan = 2)

message_label.grid(row = 7, column = 0, columnspan = 2)

# function that validates all data is reasonable and performs the optimization
def valCalc():
    msg = ""
    min_teeth = 13
    max_teeth = 100
    min_planets = 3
    max_planets = 5
    diametral_pitch = 1
    # if we're getting a range for teeth
    if (max_teeth_entry.grid_info()):   
        # gets teeth data
        min_teeth = min_teeth_entry.get()
        max_teeth = max_teeth_entry.get()
        # validates teeth data
        try:
            min_teeth = int(min_teeth)
            max_teeth = int(max_teeth)
            if (min_teeth > max_teeth):
                msg += "Minimum teeth exceed maximum teeth. "
            if (min_teeth < 13):
                msg += "Minimum teeth cannot be less than 13. "
            if (max_teeth > 101):
                msg += "Maximum teeth cannot exceed 100. "
        except:
            msg += "Minimum and maximum teeth must be integer values. "
    # if we're taking a single value for teeth
    else:
        # gets teeth data
        min_teeth = min_teeth_entry.get()
        max_teeth = min_teeth
        # validates teeth data
        try:
            min_teeth = int(min_teeth)
            max_teeth = int(max_teeth)
            if (min_teeth < 13 or min_teeth > 100):
                msg += "Teeth must be between 13 and 100 inclusive. "
        except:
            msg += "Teeth must be an integer value. "
    # if we're getting a range for planets
    if (max_planets_entry.grid_info()):
        # gets planet data
        min_planets = min_planets_entry.get()
        max_planets = max_planets_entry.get()
        # validates planet data
        try:
            min_planets = int(min_planets)
            max_planets = int(max_planets)
            if (min_planets not in [3,4,5] or max_planets not in [3,4,5]):
                msg += "There must be either 3, 4, or 5 planets. "
            else:
                if (min_planets > max_planets):
                    msg += "Minimum planets cannot exceed maximum plamets. "
        except:
            msg += "Planets must be an integer. "
    # if we're taking a single value for planets
    else:
        # gets planet data
        min_planets = min_planets_entry.get()
        max_planets = min_planets
        # validates planet data
        try:
            min_planets = int(min_planets)
            max_planets = int(max_planets)
            if (min_planets not in [3,4,5]):
                msg += "Planets must be either 3, 4, or 5. "
        except:
            msg += "Planets must be an integer. "
    # gets diametral pitch data   
    diametral_pitch = diametral_pitch_entry.get()
    # validates diametral pitch
    try:
        diametral_pitch = float(diametral_pitch)
        if (diametral_pitch <= 0):
            msg += "Diametral pitch must be positive. "
    except:
        msg += "Invalid diametral pitch. "
    # if no errors, utilize optimization script to generate values
    if (msg == ""):
        find_optimal_gears(min_teeth, max_teeth, min_planets, max_planets, diametral_pitch)
        message_label.configure(text = "Output successfully generated.")
    else: 
        message_label.configure(text = msg)

#configures generate button so that validation and calculation function is called when it is clicked
generate_button.configure(command = valCalc)

# calls mainloop method on window object -> allows the window to be displayed
window.mainloop()