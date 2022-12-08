# imports tkinter (Python GUI library)
import tkinter as tk

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

# dummy function used as placeholder before functions are defined with actual functionality
def dummy():
    pass

# creates all gui widgets
teeth_label = createLabel("Tooth Count")
min_teeth_entry = createEntry()
max_teeth_entry = createEntry()
teeth_toggle = createToggle()
teeth_validation_label = createLabel("asf")

planets_label = createLabel("Number of Planets in Carrier")
min_planets_entry = createEntry()
max_planets_entry = createEntry()
planets_toggle = createToggle()
planets_validation_label = createLabel("asdf")

diametral_pitch_label = createLabel("Diametral Pitch")
diametral_pitch_entry = createEntry()
diametral_pitch_validation_label = createLabel("asdf")

generate_button = createButton("Generate")

message_label = createLabel("asdf")

# function that toggles tooth count range/single value
def toggleText(btn):
    text = btn.cget('text')
    if (text == "Single Value"):
        btn.configure(text = "Range")
    else:
        btn.configure(text = "Single Value")
# function that toggles entry boxes
def toggleEntry(low, high):
    pass
# function that toggles text and entry boxes for teeth
def toggleTeeth():
    toggleText(teeth_toggle)
# function that toggles text and entry boxes for planets
def togglePlanets():
    toggleText(planets_toggle)
    
teeth_toggle.configure(command=toggleTeeth)
planets_toggle.configure(command=togglePlanets)

# lays all gui widgets out in a grid format
teeth_label.grid(row = 0, column = 0)
min_teeth_entry.grid(row = 1, column = 0)
max_teeth_entry.grid(row = 1, column = 1)
teeth_toggle.grid(row = 1, column = 2)
teeth_validation_label.grid(row = 1, column = 3)

planets_label.grid(row = 2, column = 0)
min_planets_entry.grid(row = 3, column = 0)
max_planets_entry.grid(row = 3, column = 1)
planets_toggle.grid(row = 3, column = 2)
planets_validation_label.grid(row = 3, column = 3)

diametral_pitch_label.grid(row = 4,)
diametral_pitch_entry.grid(row = 5, column = 0)
diametral_pitch_validation_label.grid(row = 5, column = 1)

generate_button.grid(row = 6, column = 0)

message_label.grid(row = 7, column = 0)

# calls mainloop method on window object -> allows the window to be displayed
window.mainloop()