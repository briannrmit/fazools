import numpy as np 
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from routeCardsAidanwithfloor import createRandomRoute #Will need this file in same directory
import cv2 

#list to be replaced with an actual list of players held routecards
playerXRouteCard = []
playerXRouteCardSmall = [None]*40
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())

root =tk.Tk()

arraySize = len(playerXRouteCard)

panel1 = None
panel2 = None
panel3 = None
panel4 = None
panel5 = None

index = 0

# Converting cv2 image objects to ImageTk objects for whole array
for x in range(0,arraySize) :
    b,g,r = cv2.split(playerXRouteCard[x])
    playerXRouteCard[x] = cv2.merge((r,g,b))
    im = Image.fromarray(playerXRouteCard[x])
    playerXRouteCard[x] = ImageTk.PhotoImage(image=im)
    playerXRouteCardSmall[x] = im.resize((100, 76), Image.ANTIALIAS)

class nextButton:
    def __init__(self):
        
        self.nextButton = Button(root, text="->", command = self.nextButtonPress)
        self.nextButton.pack(side=LEFT, padx = 10)
        
    def nextButtonPress(self):
        global index
        if  index < 15 :
            index += 5
            refreshCards()
        else:
            self.nextButton.config(background="red")
            self.nextButton.after(5000, self.refresh())
        refreshCards()

    def refresh(self):
        self.nextButton.config(background = "gray")

class previousButton:
    def __init__(self):
        
        self.previousButton = Button(root, text="<-", command = self.previousButtonPress)
        self.previousButton.pack(side=LEFT, padx = 10)
        
    def previousButtonPress(self):
        global index
        if  index > 0 :
            index -= 5
            refreshCards()
        else:
            self.previousButton.config(background="red")
        
    
def refreshCards() :
    global panel1
    global panel2
    global panel3
    global panel4
    global panel5
    panel1.config(image=playerXRouteCard[0 + index])
    panel2.config(image=playerXRouteCard[1 + index])
    panel3.config(image=playerXRouteCard[2 + index])
    panel4.config(image=playerXRouteCard[3 + index])
    panel5.config(image=playerXRouteCard[4 + index])

previous = previousButton()
panel1 = Button(root, image=playerXRouteCard[0 + index])
panel1.pack(side=LEFT)
panel2 = Button(root, image=playerXRouteCard[1 + index])
panel2.pack(side=LEFT)
panel3 = Button(root, image=playerXRouteCard[2 + index])
panel3.pack(side=LEFT)
panel4 = Button(root, image=playerXRouteCard[3 + index])
panel4.pack(side=LEFT)
panel5 = Button(root, image=playerXRouteCard[4 + index])
panel5.pack(side=LEFT)
next = nextButton()
