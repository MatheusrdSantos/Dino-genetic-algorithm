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
        self.moving = False
        self.distance = 0
        self.jumping_id = None
        #TODO: change image names
        img_pil = Image.open("./assets/dino.png")
        self.image = ImageTk.PhotoImage(img_pil)
        self.id = self.canvas.create_image(100, 650, image=self.image, anchor=NW)
        self.master.bind('<Up>', self.jump_call)
        self.master.bind('<Down>', self.down)

    def jump_call(self, event):
        if(not self.moving):
            self.moving = True
            self.jump(event)
    def jump(self, event):
        if(self.distance<self.jump_height):
            self.distance+=1
            self.canvas.move(self.id, 0, -1)
            self.jumping_id = self.canvas.after(3, self.jump, event)
        elif(self.distance>=self.jump_height and self.distance<self.jump_height*2):
            self.distance+=1
            self.canvas.move(self.id, 0, 1)
            self.jumping_id = self.canvas.after(3, self.jump, event)
        else:
            self.distance = 0
            self.moving = False

    def down(self, event):
        pass