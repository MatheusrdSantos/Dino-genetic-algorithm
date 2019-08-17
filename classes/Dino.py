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
        self.moving_id = None
        #TODO: change image names
        img_pil = Image.open("./assets/dino.png")
        self.image = ImageTk.PhotoImage(img_pil)
        self.id = self.canvas.create_image(100, 650, image=self.image, anchor=NW)
        self.master.bind('<Up>', self.jump_call)
        self.master.bind('<Down>', self.down)
        #self.getColisionInfo()
    def jump_call(self, event):
        if(not self.moving):
            self.moving = True
            self.jump(event)
    def jump(self, event):
        if(self.distance<self.jump_height):
            self.distance+=1
            self.canvas.move(self.id, 0, -1)
            self.moving_id = self.canvas.after(3, self.jump, event)
        elif(self.distance>=self.jump_height and self.distance<self.jump_height*2):
            self.distance+=1
            self.canvas.move(self.id, 0, 1)
            self.moving_id = self.canvas.after(3, self.jump, event)
        else:
            self.distance = 0
            self.moving = False

    def down(self, event):
        if(self.moving):
            self.master.after_cancel(self.moving_id)
            self.moving = False
            self.distance = 0
            coords = self.canvas.coords(self.id)
            self.canvas.move(self.id, 0, 650-coords[1])
    def getColisionInfo(self):
        # [left, top, right, bottom]
        block_coords = self.canvas.bbox(self.id)

        # the radius at the x axis
        radius_block_x = abs(block_coords[0] - block_coords[2])/2
        
        # the x coord of the middle point
        block_center_x = radius_block_x + block_coords[0]
        
        # the radius at the y axis
        radius_block_y = abs(block_coords[1] - block_coords[3])/2
        # the y coord of the middle point
        block_center_y = radius_block_y + block_coords[1]

        #self.canvas.create_oval(block_coords[0], block_coords[1], block_coords[2], block_coords[3], fill="#fff")
        return {'radius_x': radius_block_x, 'radius_y': radius_block_y, 'coords': {'x': block_center_x, 'y': block_center_y}}