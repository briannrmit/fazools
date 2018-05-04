import tkinter as tk
from tkinter import *
import numpy as np 
from PIL import ImageTk, Image
from routeCardsAidanwithfloor import createRandomRoute #Will need this file in same directory
import cv2 


def drawBoard():
    root = tk.Tk()

#width, height = Image.open(image.png).size


    canvas = tk.Canvas(root, width=1800, height=2659,background="#DCDCDC")
    canvas.pack()
    image = ImageTk.PhotoImage(file="board2.png")
    canvas.create_image(0,790, image=image,anchor = SW)
    root.title('Loco Motive')

#option menu buttons hosting area
    pickcarriagecard_button = tk.Button(root, text = " Carriage card",font=("courier", 15),  command = root.quit, anchor = 'w',width = 16,height = 2,activebackground = "#33B5E5")
    pickcarriagecard_button_window = canvas.create_window(1070, 80, anchor='nw', window=pickcarriagecard_button)    
    pickroute_button = tk.Button(root, text = "   Route card",font=("courier", 15),  command = drawRouteCards, anchor = 'w', width = 18,height = 2, activebackground = "#33B5E5")
    pickroute_button_window = canvas.create_window(1290, 80, anchor='nw', window=pickroute_button)
    claimroute_button = tk.Button(root, text = "  Claim a route",font=("courier", 15),  command = root.quit, anchor = 'w', width = 16,height = 2, activebackground = "#33B5E5")
    claimroute_button_window = canvas.create_window(1070, 150, anchor='nw', window=claimroute_button)
    endturn_button = tk.Button(root, text = "    End Turn",font=("courier", 15),  command = root.quit, anchor = 'w', width = 18,height = 2, activebackground = "#33B5E5")
    endturn_button_window = canvas.create_window(1290, 150, anchor='nw', window=endturn_button)
    howtoplay_button = tk.Button(root, text = "   How to Play",font=("courier", 15),  command = clickHowToPlay, anchor = 'w', width = 18,height = 1, activebackground = "#33B5E5")
    howtoplay_button_window = canvas.create_window(1210, 220, anchor='nw', window=howtoplay_button)
    #scoreboard_button = tk.Button(root, text = "",font=("courier", 15), command = root.quit, anchor = 'w', width =37,height = 10, activebackground = "#33B5E5")
    #scoareboard_button_window = canvas.create_window(1065, 450, anchor='nw', window=scoreboard_button)

# carriage cards
    #carriagecard1_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w',width =16,height = 2, activebackground = "#33B5E5")
    #carriagecard1_button_window = canvas.create_window(20, 795, anchor='nw', window=carriagecard1_button)

    #carriagecard2_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w',width =16,height = 2, activebackground = "#33B5E5")
   # carriagecard2_button_window = canvas.create_window(160, 795, anchor='nw', window=carriagecard2_button)
    #carriagecard3_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w',width =16,height = 2, activebackground = "#33B5E5")
   # carriagecard3_button_window = canvas.create_window(300, 795, anchor='nw', window=carriagecard3_button)

   # carriagecard4_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w',width =16,height = 2, activebackground = "#33B5E5")
   # carriagecard4_button_window = canvas.create_window(438, 795, anchor='nw', window=carriagecard4_button)

    #carriagecard5_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w',width =16,height = 2, activebackground = "#33B5E5")
   # carriagecard5_button_window = canvas.create_window(576, 795, anchor='nw', window=carriagecard5_button)

    #carriagecard6_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w', width =16,height = 2, activebackground = "#33B5E5")
   # carriagecard6_button_window = canvas.create_window(717, 795, anchor='nw', window=carriagecard6_button)

   # carriagecard7_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w',width =16,height = 2, activebackground = "#33B5E5")
   # carriagecard7_button_window = canvas.create_window(855, 795, anchor='nw', window=carriagecard7_button)

  #  carriagecard8_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w',width =16,height = 2, activebackground = "#33B5E5")
  #  carriagecard8_button_window = canvas.create_window(995, 795, anchor='nw', window=carriagecard8_button)

   # carriagecard9_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w', width =16,height = 2, activebackground = "#33B5E5")
  #  carriagecard9_button_window = canvas.create_window(1147, 795, anchor='nw', window=carriagecard9_button)

   # carriagecard10_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w',width =16,height = 2, activebackground = "#33B5E5")
  #  carriagecard10_button_window = canvas.create_window(20, 843, anchor='nw', window=carriagecard10_button)

  #  carriagecard11_button = tk.Button(root, text =" Carriage Card", command = root.quit, anchor = 'w',width =16,height = 2, activebackground = "#33B5E5")
   # carriagecard11_button_window = canvas.create_window(170, 843, anchor='nw', window=carriagecard11_button)

   # carriagecard12_button = tk.Button(root, text = " Carriage Card",command = root.quit, anchor = 'w',  width =16,height = 2, activebackground = "#33B5E5")
  #  carriagecard12_button_window = canvas.create_window(320, 843, anchor='nw', window=carriagecard12_button)

   # carriagecard13_button = tk.Button(root, text = " Carriage Card", command = root.quit, anchor = 'w', width =16,height = 2, activebackground = "#33B5E5")
 #   carriagecard13_button_window = canvas.create_window(460, 843, anchor='nw', window=carriagecard13_button)

   # carriagecard14_button = tk.Button(root, text = " Carriage Card", command = root.quit, anchor = 'w',  width =16,height = 2, activebackground = "#33B5E5")
  #  carriagecard14_button_window = canvas.create_window(590, 843, anchor='nw', window=carriagecard14_button)

  #  carriagecard15_button = tk.Button(root, text = " Carriage Card", command = root.quit, anchor = 'w', width =16,height = 2, activebackground = "#33B5E5")
  #  carriagecard15_button_window = canvas.create_window(720, 843, anchor='nw', window=carriagecard15_button)

    canvas_id = canvas.create_text(1225, 20, anchor="nw")
    canvas.itemconfig(canvas_id, text="Loco Motive "*1, width=1200)
    canvas.itemconfig(canvas_id, font=("courier", 25))


    root.mainloop()

def clickHowToPlay():
    ABOUT_TEXT = """HOW TO PLAY

    
    Choose number of human players 1-6
    Choose number of computer players (to make 2-6 players total)
    Each player given 40 train tracks of their colour.
    Each player given 3 route cards
    Each players can choose to discard 0, 1 route cards at the start.
    Must keep at least 2 to begin with.
    Each player given 5 train cards.
    Randomise who goes first.

    On player turn, they choose only one of the following plays:
    a.Pick up 2 more train cards
    b. Pick up 3 more route cards (can then discard 0,1 or 2 of newly
    picked up cards,must keep original route cards and at least one of new
    three picked up)
    c. Claim a route (exchange at least 1 locomotive card and the correct
    number of correct coloured carriage cards to place train carriages
     along the route of the matching colour)

    (The claim a route here is different to the original to make our game a bit different.
    So on our board, you would need a locomotive card and 7 yellow cards to claim Broome
    to Darwin. You would need a Locomotive card and 1 red card to claim Perth to Bunbury (Augusta))

    When a player claims a route the following points are awarded:
    1 carriage=1 point
    2 carriages=2 points
    3 carriages=4 points
    4 carriages=7 points
    5 carriages=10 points
    6 carriages=15 points
    7 carriages=20 points

    When a player completes a route they are awarded the number of points indicated on the route card.
    This is based on the distance between the cities regardless of the route taken.
    Points are added to the players score as they complete the route.

    The game ends when a player has 0, 1 or 2 carriages left.  
    Any uncompleted route card values are subtracted from the player’s score. 
    The player with the highest points wins."""
    toplevel = Toplevel()
    label1 = Label(toplevel, text=ABOUT_TEXT,font=("courier", 12,), height=0, width=120)
    label1.pack()
    c = Button(toplevel, text="Close Window", width=20, command=label1.destroy)
    c.pack(side='top',padx=5,pady=30)



#list to be replaced with an actual list of players held routecards
def drawRouteCards():
    drawnRouteCard = []
    drawnRouteCardSmall = [None]*40
    drawnRouteCard.append(createRandomRoute())
    drawnRouteCard.append(createRandomRoute())
    drawnRouteCard.append(createRandomRoute())
    #playerXRouteCard.append(createRandomRoute())
    #playerXRouteCard.append(createRandomRoute())
    #playerXRouteCard.append(createRandomRoute())
    #playerXRouteCard.append(createRandomRoute())
    #playerXRouteCard.append(createRandomRoute())
    #playerXRouteCard.append(createRandomRoute())
    #playerXRouteCard.append(createRandomRoute())
    #playerXRouteCard.append(createRandomRoute())
    #playerXRouteCard.append(createRandomRoute())
    #playerXRouteCard.append(createRandomRoute())
    #playerXRouteCard.append(createRandomRoute())
    #playerXRouteCard.append(createRandomRoute())
    #playerXRouteCard.append(createRandomRoute())
    #playerXRouteCard.append(createRandomRoute())
    #playerXRouteCard.append(createRandomRoute())
    #playerXRouteCard.append(createRandomRoute())
    #playerXRouteCard.append(createRandomRoute())
    #playerXRouteCard.append(createRandomRoute())
    #playerXRouteCard.append(createRandomRoute())
    #playerXRouteCard.append(createRandomRoute())
    #playerXRouteCard.append(createRandomRoute())
    root =tk.Tk()
    w = Canvas(root, width=500, height=700)
    w.pack()
    arraySize = len(drawnRouteCard)
    panel1 = None
    panel2 = None
    panel3 = None
    panel4 = None
    panel5 = None
    index = 0
    # Converting cv2 image objects to ImageTk objects for whole array
    for x in range(0,arraySize) :
        b,g,r = cv2.split(drawnRouteCard[x])
        drawnRouteCard[x] = cv2.merge((r,g,b))
        im = Image.fromarray(drawnRouteCard[x])
        drawnRouteCard[x] = ImageTk.PhotoImage(image=im)
        i = im.resize((100, 76), Image.ANTIALIAS)
        drawnRouteCardSmall[x] = ImageTk.PhotoImage(image=i)
    class nextButton:
        def __init__(self):
        
            self.nextButton = Button(w, text="->", command = self.nextButtonPress)
            self.nextButton.pack(side=LEFT, padx = 10)
        
        def nextButtonPress(self):
            global index
            if  index < 15 :
                index += 5
                refreshCards()
            else:
                 self.nextButton.config(background="red")
                 refreshCards()
        def refresh(self):
             self.nextButton.config(background = "gray")

    class previousButton:
         def __init__(self):
        
             self.previousButton = Button(w, text="<-", command = self.previousButtonPress)
             self.previousButton.pack(side=LEFT, padx = 10)
            
         def previousButtonPress(self):
             global index
             if  index > 0 :
                 index -= 5
                 refreshCards()
             else:
                 self.previousButton.config(background="red")

    class panel:
        def __init__(self, position):
            global index
            self.position = position
            self.panel  = Button(w, image=drawnRouteCardSmall[position + index])
            self.panel.bind("<Enter>", self.maximize)
            self.panel.bind("<Leave>", self.minimize)
            self.panel.pack(side=LEFT)

        def maximize(self, event):
            self.panel.config(image=drawnRouteCard[self.position + index])

        def minimize(self, event) :
            self.panel.config(image=drawnRouteCardSmall[self.position + index])
        def refresh(self):
            self.panel.config(image=drawnRouteCardSmall[self.position + index])
        
    
    def refreshCards() :
        panel1.refresh()
        panel2.refresh()
        panel3.refresh()
        panel4.refresh()
        panel5.refresh()

    previous = previousButton()
    panel1 = panel(0)
    panel2 = panel(1)
    panel3 = panel(2)
    panel4 = panel(3)
    panel5 = panel(4)
    next = nextButton()


