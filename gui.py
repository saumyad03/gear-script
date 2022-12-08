# Personal Notes For Updated GUI:
# constraints - ranges/min/max (input and output)
# input and output validation
# combinations - export to excel sheet

# imports tkinter (Python GUI library)
import tkinter as tk
# import gear_script.py file that contains function that generates outputs
from gear_script import *
# import find_optimal_gears.py file that contains function that generates 

# creates window, sets window title, sets window color, sets window dimensions
window = tk.Tk()
window.title("Gear Script")
window.configure(background="black")
window.geometry("500x500") # "widthxheight"

# creates labels and text entry pairs
# creates label on window with certain text, a black background, and white foreground (font)
# creates text entry box on window with width (in characters) and white background
# packs both label and text entry box to display it on window
dp_label = tk.Label(window, text="Diametral Pitch", bg="black", fg="white")
dp_entry = tk.Entry(window, width=20, bg="white", justify="center")
dp_label.pack()
dp_entry.pack()

sg1tc_label = tk.Label(window, text="Sun Gear 1 Tooth Count", bg="black", fg="white")
sg1tc_entry = tk.Entry(window, width=20, bg="white", justify="center")
sg1tc_label.pack()
sg1tc_entry.pack()

ag1tc_label = tk.Label(window, text="Annulus Gear 1 Tooth Count", bg="black", fg="white")
ag1tc_entry = tk.Entry(window, width=20, bg="white", justify="center")
ag1tc_label.pack()
ag1tc_entry.pack()

npic_label = tk.Label(window, text="Number of Planets in Carrier", bg="black", fg="white")
npic_entry = tk.Entry(window, width=20, bg="white", justify="center")
npic_label.pack()
npic_entry.pack()

ssm_label = tk.Label(window, text="Second Stage Multiplier", bg="black", fg="white")
ssm_entry = tk.Entry(window, width=20, bg="white", justify="center")
ssm_label.pack()
ssm_entry.pack()

#defines labels for output
pg1tc_label = tk.Label(window, text="", bg="black", fg="white")
odp_label = tk.Label(window, text="", bg="black", fg="white")
sg2tc_label = tk.Label(window, text="", bg="black", fg="white")
pg2tc_label = tk.Label(window, text="", bg="black", fg="white")
ag2tc_label = tk.Label(window, text="", bg="black", fg="white")
ot_label = tk.Label(window, text="", bg="black", fg="white")
rfso_label = tk.Label(window, text="", bg="black", fg="white")
rsso_label = tk.Label(window, text="", bg="black", fg="white")
foros_label = tk.Label(window, text="", bg="black", fg="white")
rfsi_label = tk.Label(window, text="", bg="black", fg="white")
rssi_label = tk.Label(window, text="", bg="black", fg="white")
foris_label = tk.Label(window, text="", bg="black", fg="white")
ro_label = tk.Label(window, text="", bg="black", fg="white")

# defines function that runs when submit button is clicked
def calculate():
    # retrieves inputs from entry boxes, casts them as floats for math, and stores them in variables
    input_diametral_pitch = float(dp_entry.get())
    sun_gear_1_tooth_count = float(sg1tc_entry.get())
    annulus_gear_1_tooth_count= float(ag1tc_entry.get())
    num_planets_in_carrier = float(npic_entry.get())
    second_stage_multiplier = float(ssm_entry.get())
    # calls gear_script function to calculate outputs and stores it to a variable (outputs is a list)
    outputs = gear_script(input_diametral_pitch, sun_gear_1_tooth_count, annulus_gear_1_tooth_count, num_planets_in_carrier, second_stage_multiplier, check_if_reasonable=False)
    # sets label text for output
    pg1tc_label.config(text = "Planet Gears 1 Tooth Count: " + str(outputs[0]))
    odp_label.config(text = "Output Diametral Pitch: " + str(outputs[1]))
    sg2tc_label.config(text = "Sun Gear 2 Tooth Count: " + str(outputs[2]))
    pg2tc_label.config(text = "Planet Gears 2 Tooth Count: " + str(outputs[3]))
    ag2tc_label.config(text = "Annulus Gear 2 Tooth Count: " + str(outputs[4]))
    ot_label.config(text = "Output Teeth: " + str(outputs[5]))
    rfso_label.config(text = "Ratio First Stage Output: " + str(outputs[6]))
    rsso_label.config(text = "Ratio Second Stage Output: " + str(outputs[7]))
    foros_label.config(text = "Final Output Ratio Output Shaft: " + str(outputs[8]))
    rfsi_label.config(text = "Ratio First Stage Input: " + str(outputs[9]))
    rssi_label.config(text = "Ratio Second Stage Input: " + str(outputs[10]))
    foris_label.config(text = "Final Output Ratio Input Shaft: " + str(outputs[11]))
    ro_label.config(text = "Ratio Overall: " + str(outputs[12]))
    
#creates empty label to push submit button down (for aesthetics)(will chage later)
empty_label = tk.Label(window, bg="black")
empty_label.pack()
# creates submit button and displays it
submit_btn = tk.Button(window, text="Generate", width=6, command=calculate)
submit_btn.pack()

# displays output labels
pg1tc_label.pack()
odp_label.pack()
sg2tc_label.pack()
pg2tc_label.pack()
ag2tc_label.pack()
ot_label.pack()
rfso_label.pack()
rsso_label.pack()
foros_label.pack()
rfsi_label.pack()
rssi_label.pack()
foris_label.pack()
ro_label.pack()

# calls mainloop function on window object - allows the window to be seen
window.mainloop()