import tkinter as tk
from tkinter import *
from PIL import ImageTk


root = tk.Tk()

#width, height = Image.open(image.png).size

canvas = tk.Canvas(root, width=1400, height=5000)
canvas.pack()

image = ImageTk.PhotoImage(file="board.png")
canvas.create_image(0, 0, image=image,anchor =NW)
pickcarriagecard_button = tk.Button(root, text = "Pick up carriage card", command = root.quit, anchor = 'w',
                    width = 16,height = 2, activebackground = "#33B5E5")
pickcarriagecard_button_window = canvas.create_window(1200, 80, anchor='nw', window=pickcarriagecard_button)    
pickroute_button = tk.Button(root, text = "Pick up route card", command = root.quit, anchor = 'w',
                    width = 16,height = 2, activebackground = "#33B5E5")
pickroute_button_window = canvas.create_window(1335, 80, anchor='nw', window=pickroute_button)
claimroute_button = tk.Button(root, text = "      Claim a route", command = root.quit, anchor = 'w',
                    width = 16,height = 2, activebackground = "#33B5E5")
claimroute_button_window = canvas.create_window(1200, 130, anchor='nw', window=claimroute_button)
endturn_button = tk.Button(root, text = "         End Turn", command = root.quit, anchor = 'w',
                    width = 16,height = 2, activebackground = "#33B5E5")
endturn_button_window = canvas.create_window(1335, 130, anchor='nw', window=endturn_button)
howtoplay_button = tk.Button(root, text = "      How to Play", command = root.quit, anchor = 'w',
                    width = 14,height = 1, activebackground = "#33B5E5")
howtoplay_button_window = canvas.create_window(1280, 180, anchor='nw', window=howtoplay_button)
scoreboard_button = tk.Button(root, text = "                              Score Board", command = root.quit, anchor = 'w',
                    width =35,height = 7, activebackground = "#33B5E5")
scoareboard_button_window = canvas.create_window(1200, 212, anchor='nw', window=scoreboard_button)
carriagecard1_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w',
                    width =16,height = 2, activebackground = "#33B5E5")
carriagecard1_button_window = canvas.create_window(-50, 5, anchor='nw', window=carriagecard1_button)

carriagecard2_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w',
                    width =16,height = 2, activebackground = "#33B5E5")
carriagecard2_button_window = canvas.create_window(-50, 50, anchor='nw', window=carriagecard2_button)


carriagecard3_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w',
                    width =16,height = 2, activebackground = "#33B5E5")
carriagecard3_button_window = canvas.create_window(-50, 96, anchor='nw', window=carriagecard3_button)

carriagecard4_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w',
                    width =16,height = 2, activebackground = "#33B5E5")
carriagecard4_button_window = canvas.create_window(-50, 143, anchor='nw', window=carriagecard4_button)

carriagecard5_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w',
                    width =16,height = 2, activebackground = "#33B5E5")
carriagecard5_button_window = canvas.create_window(-50, 96, anchor='nw', window=carriagecard3_button)





canvas_id = canvas.create_text(1240, 20, anchor="nw")
canvas.itemconfig(canvas_id, text="Loco Motive "*1, width=1200)
canvas.itemconfig(canvas_id, font=("courier", 18))


root.mainloop()

