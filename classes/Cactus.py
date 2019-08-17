"""
Author: Matheus Santos
Description: this class represents an obstacle of the cactus type.
The Dino can't colide with obstacles.
"""
from tkinter import NW
from PIL import Image, ImageTk

class Cactus:
    def __init__(self, master, canvas, kind = 3):
        self.master = master
        self.canvas = canvas
        img_pil = Image.open("./assets/obstacle-3x.png")
        self.image = ImageTk.PhotoImage(img_pil)
        self.id = self.canvas.create_image(800, 650, image=self.image, anchor=NW)
        self.moving_id = None
        self.draw()
    def draw(self):
        if(self.canvas.coords(self.id)[0]<1):
            self.canvas.move(self.id, 800, 0)
        else:
            self.canvas.move(self.id, -8.7, 0)
        self.moving_id = self.canvas.after(20, self.draw)