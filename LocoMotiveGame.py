import tkinter as tk
from tkinter import *
import numpy as np 
from PIL import ImageTk, Image
from routeCardsAidanwithfloor import createRandomRoute #Will need this file in same directory
import cv2
import math
import random

#playerList=[None]*6

#def numPlayers():
root = tk.Tk()
screenWidth=root.winfo_screenwidth()
screenHeight=root.winfo_screenheight()
p1BlueNum=0
p1GreenNum=0
p1RedNum=0
p1PinkNum=0
p1OrangeNum=0
p1YellowNum=0
p1LocoNum=0
p1Routes=0
p1Carriages=0
p1CarriageRem=40
p1Turn=0



class playingBoard(object):
    #def drawBoard():
    #root = tk.Tk()

#width, height = Image.open(image.png).size
    def __init__(self,master):
        top=window=Toplevel(master)
        #top=self.top=Toplevel(master)
        self.r=top
        self.f=Frame(self.r)
        self.f.pack(fill="both",expand=True)
        self.c = Canvas(self.f, width=1800, height=2659,background="#DCDCDC")
        self.c.pack(fill="both", expand=True)
        self.c.create_text(1185, 20, fill="green", font="courier 25 bold", text ="Loco Motive", width=1200, anchor="nw")
        image1 = ImageTk.PhotoImage(file="board2.png")
        photoLabel1=Label(image=image1)
        photoLabel1.image=image1
        photoLabel1.pack()
        self.c.create_image(-100,0, image=image1,anchor = NW)
        image2 = ImageTk.PhotoImage(file="scoreboard_template.png")
        photoLabel2=Label(image=image2)
        photoLabel2.image=image2
        photoLabel2.pack()
        self.c.create_image(1080,500, image=image2,anchor = NW)
        window.title('Loco Motive')
        image3 = ImageTk.PhotoImage(file="carriage_blue.png")
        photoLabel3=Label(image=image3)
        photoLabel3.image=image3
        photoLabel3.pack()
        self.c.create_image(10,820, image=image3,anchor = NW)
        image4 = ImageTk.PhotoImage(file="carriage_yellow.png")
        photoLabel4=Label(image=image4)
        photoLabel4.image=image4
        photoLabel4.pack()
        self.c.create_image(240,820, image=image4,anchor = NW)
        image5 = ImageTk.PhotoImage(file="carriage_red.png")
        photoLabel5=Label(image=image5)
        photoLabel5.image=image5
        photoLabel5.pack()
        self.c.create_image(470,820, image=image5,anchor = NW)
        image6 = ImageTk.PhotoImage(file="carriage_green.png")
        photoLabel6=Label(image=image6)
        photoLabel6.image=image6
        photoLabel6.pack()
        self.c.create_image(700,820, image=image6,anchor = NW)
        image7 = ImageTk.PhotoImage(file="carriage_orange.png")
        photoLabel7=Label(image=image7)
        photoLabel7.image=image7
        photoLabel7.pack()
        self.c.create_image(930,820, image=image7,anchor = NW)
        image8 = ImageTk.PhotoImage(file="carriage_pink.png")
        photoLabel8=Label(image=image8)
        photoLabel8.image=image8
        photoLabel8.pack()
        self.c.create_image(1160,820, image=image8,anchor = NW)
        image9 = ImageTk.PhotoImage(file="train_card.png")
        photoLabel9=Label(image=image9)
        photoLabel9.image=image9
        photoLabel9.pack()
        self.c.create_image(1400,820, image=image9,anchor = NW)
        self.c.create_text(170, 860, fill="green", font="courier 25 bold", text ="x "+str(p1BlueNum), width=1200, anchor="nw")
        self.c.create_text(400, 860, fill="green", font="courier 25 bold", text ="x "+str(p1YellowNum), width=1200, anchor="nw")
        self.c.create_text(630, 860, fill="green", font="courier 25 bold", text ="x "+str(p1RedNum), width=1200, anchor="nw")
        self.c.create_text(860, 860, fill="green", font="courier 25 bold", text ="x "+str(p1GreenNum), width=1200, anchor="nw")
        self.c.create_text(1090, 860, fill="green", font="courier 25 bold", text ="x "+str(p1OrangeNum), width=1200, anchor="nw")
        self.c.create_text(1330, 860, fill="green", font="courier 25 bold", text ="x "+str(p1PinkNum), width=1200, anchor="nw")
        self.c.create_text(1560, 860, fill="green", font="courier 25 bold", text ="x "+str(p1LocoNum), width=1200, anchor="nw")
        self.b1 = tk.Button(self.r, text = " Carriage card",font=("courier", 15),  command =drawTrainCards, anchor = 'w',width = 16,height = 2,activebackground = "#33B5E5")
        pickcarriagecard_button_window = self.c.create_window(1070, 80, anchor='nw', window=self.b1)    
        self.b2 = tk.Button(self.r, text = "   Route card",font=("courier", 15),  command = drawRouteCards, anchor = 'w', width = 18,height = 2, activebackground = "#33B5E5")
        pickroute_button_window = self.c.create_window(1290, 80, anchor='nw', window=self.b2)
        self.b3 = tk.Button(self.r, text = "  Claim a route",font=("courier", 15),  command = root.quit, anchor = 'w', width = 16,height = 2, activebackground = "#33B5E5")
        claimroute_button_window = self.c.create_window(1070, 150, anchor='nw', window=self.b3)
        self.b4 = tk.Button(self.r, text = "    End Turn",font=("courier", 15),  command = root.quit, anchor = 'w', width = 18,height = 2, activebackground = "#33B5E5")
        endturn_button_window = self.c.create_window(1290, 150, anchor='nw', window=self.b4)
        howtoplay_button = tk.Button(self.r, text = "   How to Play",font=("courier", 15),  command = clickHowToPlay, anchor = 'w', width = 18,height = 1, activebackground = "#33B5E5")
        howtoplay_button_window = self.c.create_window(1210, 220, anchor='nw', window=howtoplay_button)
        routesList=routesListInfo()
        carriagesList=carriagesListInfo()
        carriagesRemList=carriagesRemInfo()
        x=0
        y=595
        while(x<len(playerList)):
            self.c.create_text(1125,y, fill="white", font="courier 15 bold", text =str(routesList[x]), width=1200, anchor="nw")
            self.c.create_text(1175,y, fill="white", font="courier 12 bold", text =str(playerList[x]), width=1200, anchor="nw")
            self.c.create_text(1300,y, fill="white", font="courier 15 bold", text =str(carriagesList[x]), width=1200, anchor="nw")
            self.c.create_text(1400,y, fill="white", font="courier 15 bold", text =str(carriagesRemList[x]), width=1200, anchor="nw")
            y+=23
            x+=1

class drawTrainCards(object):
    
    def __init__(self):
        toplevel=tk.Toplevel()
        self.r=toplevel
        self.f=Frame(self.r)
        self.f.pack(fill="both",expand=True)
        if p1Turn==0:
            w=850
        else:
            w=340
        self.c = Canvas(self.f, width=w, height=240,background="#DCDCDC")
        self.c.pack(fill="both", expand=True)
        imageList=cardList()
        i=0
        x=20
        while (i<len(imageList)):
            image= ImageTk.PhotoImage(file=imageList[i])
            photoLabel=Label(image=image)
            photoLabel.image=image
            photoLabel.pack()
            self.c.create_image(x,20, image=image,anchor = NW)
            i+=1
            x+=170
        self.b = tk.Button(self.r, text = " OK",font=("courier", 15),  command = self.refresh, anchor = 'w', width = 5,height = 2, activebackground = "#33B5E5")
        endturn_button_window = self.c.create_window(w-75, 170, anchor='nw', window=self.b)
     
    def refresh(self):
        #otherWindow.destroy()
        app=playingBoard(root)
        #self.root.destroy()

    
def cardList():
    card1="carriage_blue.png"
    card2="carriage_yellow.png"
    card3="carriage_red.png"
    card4="carriage_green.png"
    card5="carriage_orange.png"
    card6="carriage_pink.png"
    card7="train_card.png"
    cardList=[card1,card2,card3,card4,card5,card6,card7]
    if p1Turn==0:
        maxCards=5
    else:
        maxCards=2
    drawnList=[]
    x=0
    while (x<maxCards):
        drawnCard=random.choice(cardList)
        drawnList.append(drawnCard)
        x+=1
    addCards(drawnList)     
    print(drawnList)
    return(drawnList)    

def addCards(drawnList):
    i=0
    while(i<len(drawnList)):
        if drawnList[i]=="carriage_blue.png":
            global p1BlueNum
            p1BlueNum+=1
        if drawnList[i]=="carriage_green.png":
            global p1GreenNum
            p1GreenNum+=1
        if drawnList[i]=="carriage_red.png":
            global p1RedNum
            p1RedNum+=1
        if drawnList[i]=="carriage_pink.png":
            global p1PinkNum
            p1PinkNum+=1
        if drawnList[i]=="carriage_orange.png":
            global p1OrangeNum
            p1OrangeNum+=1
        if drawnList[i]=="carriage_yellow.png":
            global p1YellowNum
            p1YellowNum+=1
        if drawnList[i]=="train_card.png":
            global p1LocoNum
            p1LocoNum+=1
        i+=1
    

def routesListInfo():
    numPlayers=len(playerList)
    routesList=[0]*numPlayers
    #print (playerList)
    return (routesList)        

def carriagesListInfo():
    numPlayers=len(playerList)
    carriagesList=[0]*numPlayers
    #print (playerList)
    return(carriagesList)

def carriagesRemInfo():
    numPlayers=len(playerList)
    carriageRemList=[40]*numPlayers
    #print (playerList)
    return(carriageRemList)

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
    toplevel.title("How To Play")
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


routeScoresList = {
    'BroomeDarwin':7,
    'KarrathaBroome':4,
    'NewmanBroome':5,
    'KarrathaNewman':2,
    'NewmanLeonora':3,
    'MtmagnetNewman':3,
    'SharkbayMtmagnet':2,
    'MtmagnetLeonora':2,
    'PerthMtmagnet':2,
    'AugustaPerth':1,
    'AugustaAlbany':2,
    'AlbanyEsperance':3,
    'EsperanceBordervillage':4,
    'LeonoraEsperance':5,
    'EsperanceAlicesprings':6,
    'HallscreekAlicesprings':5,
    'BroomeHallscreek':3,
    'DarwinAlicesprings':7,
    'DarwinNhulunbuy':3,
    'NhulunbuyBurketown':4,
    'AlicespringsBurketown':5,
    'BurketownKarumba':1,
    'AlicespringsCooberpedy':5,
    'BordervillageAdelaide':6,
    'CooberpedyAdelaide':3,
    'AdelaidePortland':4,
    'CooberpedyMtisa':7,
    'KarumbaMtisa':4,
    'PortlandMelbourne':2,
    'KarumbaCapeyork':6,
    'CapeyorkCooktown':2,
    'CooktownMackay':2,
    'CapeyorkMackay':6,
    'MtisaMackay':3,
    'MackayBundaberg':4,
    'MtisaBourke':4,
    'BourkeBundaberg':5,
    'BundabergBrisbane':2,
    'MilduraBourke':3,
    'MelbourneMildura':3,
    'HobartMelbourne':4,
    'MelbourneCanberra':3,
    'MelbourneSydney':7,
    'CanberraSydney':3,
    'BourkeSydney':4,
    'SydneyBrisbane':4
}

#  For each player give them a starting array that will contain their completed routes.
#  But assume for now, 1 player.
players = [] #players should be named player1, player2 etc.
player1Routes = []
player2Routes = []
player3Routes = []
player4Routes = []
player5Routes = []  
scores = []

#  Add players to game
def addPlayers(name: str):
    players.append(name)

#  Assigns completed route (string such as CanberraSydney) to player's routelist array
def recordCompletedRoute(route: str, playerRouteList: list):
    # Note: Need to check if route is valid based on routeScoresList
    if route in routeScoresList.keys():
        playerRouteList.append(route)
        print('Route has been successfully entered into the player''s completed routes')
    else:
        print('Route entered is invalid or misspelled')
    
#  Calculates total score of the player based on their completed routes list/array
def scoreCounter(playerRouteList: list):
    score = 0
    for x in playerRouteList:
        score = score + routeScoresList[x]
    return score

#  Displays all end scores of each player
def endScoreDisplay(players):
    for i in range(0,len(players)-1):
        playerScore = scoreCounter(eval(players[i] + 'Routes'))
        print(players[i] + ' final score is ' + playerScore)

playerList=[]
compList=[]
 
class popupWindow(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.l=Label(top,text="Human Player Name")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
        
     
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()
    

class mainWindow(object):
    def __init__(self,master):
        self.master=master
        self.b=Button(master,text="Add Human Player",command=self.popup)
        self.b.pack()
        self.b2=Button(master,text="Add Computer Player",command=self.addComputer)
        self.b2.pack()
        self.b3=Button(master,text="Start",command=self.popup2)
        self.b3.pack()

    def popup(self):
        self.w=popupWindow(self.master)
        self.b["state"] = "disabled" 
        self.master.wait_window(self.w.top)
        self.b["state"] = "normal"
        playerList.append(self.w.value)
        return playerList

    def popup2(self):
        self.w=playingBoard(self.master)
        #self.b2["state"] = "disabled" 
        #self.master.wait_window(self.w.top)
        #self.b2["state"] = "normal"
        self.cleanup #trying to make it close that random extra window with the start menu and pic - no idea why that happens

    
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()
        

    def addComputer(self):
        compList.append("Computer")
        compNum=len(compList)
        compPlayer="Computer "+str(compNum)
        playerList.append(compPlayer)
     
    def entryValue(self):
        print (playerList)
        numPlayers=len(playerList)
        routesList=[0]*numPlayers
        carriagesList=[0]*numPlayers
        carriageRemList=[40]*numPlayers
        print (routesList)
        print(carriagesList)
        print(carriageRemList)
        

mainWindow(root)
root.mainloop()
