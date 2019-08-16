"""
Author: Matheus Santos
Description: this class represents the dino.
The Dino can jump or bend in order to avoid the obstacles.
"""
from tkinter import NW
from PIL import Image, ImageTk

class Dino:
    def __init__(self, master, canvas, jump_height=100):
        self.master = master
        self.canvas = canvas
        self.jump_height = jump_height
        #TODO: change image names
        img_pil = Image.open("./assets/dino.png")
        self.image = ImageTk.PhotoImage(img_pil)
        self.id = self.canvas.create_image(100, 650, image=self.image, anchor=NW)
        #self.master.bind('<Up>', self.jump_call)
        #self.master.bind('<Down>', self.down)