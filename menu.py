from tkinter import *

# ------------------- constants ------------------
FONT_NAME = "Courier"
THEME_COLOR = "#375362"
# ------------------- menu setup ------------------
window = Tk()
window.title("Hockey Night")
window.config(padx=100, pady=50, bg=THEME_COLOR)

title_label = Label(text="NHL Hockey Night", font=(FONT_NAME, 35, "bold"), bg=THEME_COLOR)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, highlightthickness=0, bg=THEME_COLOR)
nhl_logo = PhotoImage(file="nhl-logo.png")
canvas.create_image(100, 112, image=nhl_logo)
canvas.grid(column=1, row=1)

simulate_game_button = Button(text="Simulate Game", highlightthickness=0)
simulate_game_button.grid(column=0, row=2)
show_data_button = Button(text="Show Data", highlightthickness=0)
show_data_button.grid(column=0, row=3)
parameters_button = Button(text="Parameters", highlightthickness=0)
parameters_button.grid(column=0, row=4)
reset_data_button = Button(text="Reset Data", highlightthickness=0)
reset_data_button.grid(column=0, row=5)

window.mainloop()

