"""
Author: Matheus Santos
Description: this class represents an obstacle of the cactus type.
The Dino can't colide with obstacles.
"""
from tkinter import NW
from PIL import Image, ImageTk

class Cactus:
    def __init__(self, master, canvas):
        self.master = master
        self.canvas = canvas
        img_pil = Image.open("./assets/obstacle-3x.png")
        self.image = ImageTk.PhotoImage(img_pil)
        self.id = self.canvas.create_image(700, 650, image=self.image, anchor=NW)