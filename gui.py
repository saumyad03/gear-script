# imports tkinter (Python GUI library)
import tkinter as tk

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
dp_entry = tk.Entry(window, width=20, bg="white")
dp_label.pack()
dp_entry.pack()

sg1tc_label = tk.Label(window, text="Sun Gear 1 Tooth Count", bg="black", fg="white")
sg1tc_entry = tk.Entry(window, width=20, bg="white")
sg1tc_label.pack()
sg1tc_entry.pack()

ag1tc_label = tk.Label(window, text="Annulus Gear 1 Tooth Count", bg="black", fg="white")
ag1tc_entry = tk.Entry(window, width=20, bg="white")
ag1tc_label.pack()
ag1tc_entry.pack()

npic_label = tk.Label(window, text="Number of Planets in Carrier", bg="black", fg="white")
npic_entry = tk.Entry(window, width=20, bg="white")
npic_label.pack()
npic_entry.pack()

ssm_label = tk.Label(window, text="Second Stage Multiplier", bg="black", fg="white")
ssm_entry = tk.Entry(window, width=20, bg="white")
ssm_label.pack()
ssm_entry.pack()

# defines function that runs when submit button is clicked
def calculate():
    input_diametral_pitch = dp_entry.get()
    sun_gear_1_tooth_count = sg1tc_entry.get()
    annulus_gear_1_tooth_count= ag1tc_entry.get()
    num_planets_in_carrier = npic_entry.get()
    second_stage_multiplier = ssm_entry.get()
    

# creates submit button and displays it
submit_btn = tk.Button(window, text="Generate", width=6, command=calculate)
submit_btn.pack()

# calls mainloop function on window object - allows the window to be seen
window.mainloop()