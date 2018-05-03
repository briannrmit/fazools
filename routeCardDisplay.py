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
