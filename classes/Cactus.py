"""
Author: Matheus Santos
Description: this class represents an obstacle of the cactus type.
The Dino can't colide with obstacles.
"""
from tkinter import SW, NW
from PIL import Image, ImageTk
import pickle

class Cactus:
    def __init__(self, master, canvas, onCollidChange,kind = 3, onScreenOut = lambda x=None: x):
        self.master = master
        self.canvas = canvas
        self.moving_id = None
        self.onScreenOut = onScreenOut
        self.onScreen = False
        self.height = 0
        self.onCollidChange = onCollidChange
        self.canCollid = False
        self.speed = 20
        if(kind == 3):
            img_pil = Image.open("./assets/obstacle-3x.png")
            self.mask = pickle.load( open( "./data/mask/obstacle_3_mask", "rb" ) )
            self.move_factor = {'x': 800, 'y': 652}
        elif(kind == 1):
            img_pil = Image.open("./assets/obstacle-1x.png")
            self.mask = pickle.load( open( "./data/mask/obstacle_1_mask", "rb" ) )
            self.move_factor = {'x': 800, 'y': 650}
        elif(kind == 2):
            img_pil = Image.open("./assets/obstacle-2x-small.png")
            self.mask = pickle.load( open( "./data/mask/obstacle_2_mask", "rb" ) )
            self.move_factor = {'x': 800, 'y': 665}
        self.width = img_pil.size[0]
        self.image = ImageTk.PhotoImage(img_pil)
        self.id = self.canvas.create_image(self.move_factor['x'], self.move_factor['y'], image=self.image, anchor=NW)

    def draw(self):
        if(self.canvas.coords(self.id)[0]<1):
            self.move(810, 0)
            self.onScreen = False
            self.onScreenOut()
        else:
            if(self.canvas.coords(self.id)[0]<50 and self.canCollid):
                self.canCollid = False
                self.onCollidChange()
            self.onScreen = True
            self.move(-9, 0)
            self.moving_id = self.canvas.after(self.speed, self.draw)

    def move(self, x=0, y=0):
        self.canvas.move(self.id, x, y)
        self.move_factor['x']+=x
        self.move_factor['y']+=y
    def getBoderRightDistance(self):
        block_coords = self.canvas.bbox(self.id)
        distance = 800 - block_coords[2]
        if(distance < 0):
            return 0
        return distance
    def getColisionInfo(self):
        block_coords = self.canvas.bbox(self.id)

        radius_block_x = abs(block_coords[0] - block_coords[2])/2
        block_center_x = radius_block_x + block_coords[0]
        radius_block_y = abs(block_coords[1] - block_coords[3])/2
        block_center_y = radius_block_y + block_coords[1]
        return {'radius_x': radius_block_x, 'radius_y': radius_block_y, 'coords': {'x': block_center_x, 'y': block_center_y}}
    def getBox(self):
         block_coords = self.canvas.bbox(self.id)
         return block_coords
    def changeSpeed(self, speed):
        self.speed = speed
    def reset(self):
        self.move(810 - int(self.canvas.coords(self.id)[0]), 0)
        self.onScreen = False
        self.canCollid = False