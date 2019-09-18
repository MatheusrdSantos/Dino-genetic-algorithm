"""
Author: Matheus Santos
Description: this class represents an obstacle of the flying dino type.
The Dino can't colide with obstacles.
"""
from tkinter import NW
from PIL import Image, ImageTk
import pickle
class FlyingDino:
    def __init__(self, master, canvas, onScreenOut = lambda x=None: x, height=570):
        self.canvas = canvas
        self.master = master
        self.moving_id = None
        self.onScreen = False
        self.onScreenOut = onScreenOut
        self.height = height
        self.move_factor = {'x': 900, 'y': self.height}
        # load image
        img_pil = Image.open("./assets/flying-dino.png")
        self.image = ImageTk.PhotoImage(img_pil)
        self.id = canvas.create_image(900, self.height, image=self.image, anchor=NW)
        #load mask
        self.mask = pickle.load( open( "./data/mask/flying_dino_mask", "rb" ) )

    def draw(self):
        if(self.canvas.coords(self.id)[0]<1):
            self.move(900, 0)
            self.onScreen = False
            self.onScreenOut()
        else:
            self.onScreen = True
            self.move(-9, 0)
            self.moving_id = self.canvas.after(20, self.draw)

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
    
    def reset(self):
        self.move(900 - int(self.canvas.coords(self.id)[0]), 0)
        self.onScreen = False