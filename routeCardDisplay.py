<<<<<<< HEAD
import math
import random
import numpy as np 
import cv2 
import os
import tkinter as tk
from tkinter import *
from PIL import ImageTk
from routeCardsAidan import createRandomRoute #Will need this file in same directory

#list to be replaced with an actual list of players held routecards
playerXRouteCard = []
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())

root =tk.Tk()

canvas = tk.Canvas(root, width=1400, height=500)
canvas.pack()

canvas.create_image(0,0, image = playerXRouteCard[0])
=======
import math
import random
import numpy as np 
import cv2 
import os
import tkinter as tk
from tkinter import *
from PIL import ImageTk
from routeCardsAidan import createRandomRoute #Will need this file in same directory

#list to be replaced with an actual list of players held routecards
playerXRouteCard = []
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())

root =tk.Tk()

canvas = tk.Canvas(root, width=1400, height=500)
canvas.pack()

canvas.create_image(0,0, image = playerXRouteCard[0])
>>>>>>> 4cfb907d1c1fc4f6da1d537478fb9f34fe8d96a4
