"""
Author: Matheus Santos
Description: this class represents an obstacle of the cactus type.
The Dino can't colide with obstacles.
"""
from tkinter import SW, NW
from PIL import Image, ImageTk

class Cactus:
    def __init__(self, master, canvas, kind = 3, onScreenOut = lambda x=None: x):
        self.master = master
        self.canvas = canvas
        if(kind == 3):
            img_pil = Image.open("./assets/obstacle-3x.png")
        elif(kind == 1):
            img_pil = Image.open("./assets/obstacle-1x.png")
        elif(kind == 2):
            img_pil = Image.open("./assets/obstacle-2x-small.png")
        self.image = ImageTk.PhotoImage(img_pil)
        self.id = self.canvas.create_image(800, 700, image=self.image, anchor=SW)
        self.moving_id = None
        self.onScreenOut = onScreenOut
        self.onScreen = False
        #self.draw()
        #self.getColisionInfo()
    def draw(self):
        if(self.canvas.coords(self.id)[0]<1):
            self.canvas.move(self.id, 810, 0)
            self.onScreen = False
            self.onScreenOut()
        else:
            self.onScreen = True
            self.canvas.move(self.id, -8.7, 0)
            self.moving_id = self.canvas.after(20, self.draw)
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

        #self.canvas.create_oval(block_coords[0], block_coords[1], block_coords[2], block_coords[3], fill="#fff")
        return {'radius_x': radius_block_x, 'radius_y': radius_block_y, 'coords': {'x': block_center_x, 'y': block_center_y}}

