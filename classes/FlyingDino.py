"""
Author: Matheus Santos
Description: this class represents an obstacle of the flying dino type.
The Dino can't colide with obstacles.
"""
from tkinter import NW
from PIL import Image, ImageTk
class FlyingDino:
    def __init__(self, master, canvas, onScreenOut = lambda x=None: x):
        self.canvas = canvas
        self.master = master
        img_pil = Image.open("./assets/flying-dino.png")
        self.image = ImageTk.PhotoImage(img_pil)
        self.id = canvas.create_image(900, 550, image=self.image, anchor=NW)
        self.moving_id = None
        self.onScreen = False
        self.onScreenOut = onScreenOut
        #self.draw()
    def draw(self):
        if(self.canvas.coords(self.id)[0]<1):
            self.canvas.move(self.id, 900, 0)
            self.onScreen = False
            self.onScreenOut()
        else:
            self.onScreen = True
            self.canvas.move(self.id, -8.7, 0)
            self.moving_id = self.canvas.after(20, self.draw)
    def getColisionInfo(self):
        block_coords = self.canvas.bbox(self.id)

        radius_block_x = abs(block_coords[0] - block_coords[2])/2
        block_center_x = radius_block_x + block_coords[0]
        radius_block_y = abs(block_coords[1] - block_coords[3])/2
        block_center_y = radius_block_y + block_coords[1]

        #self.canvas.create_oval(block_coords[0], block_coords[1], block_coords[2], block_coords[3], fill="#fff")
        return {'radius_x': radius_block_x, 'radius_y': radius_block_y, 'coords': {'x': block_center_x, 'y': block_center_y}}