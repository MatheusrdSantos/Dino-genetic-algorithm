"""
Author: Matheus Santos
Description: this class represents the dino.
The Dino can jump or bend in order to avoid the obstacles.
"""
from tkinter import NW
from PIL import Image, ImageTk
import pickle
import keyboard

class Dino:
    def __init__(self, master, canvas, jump_height=100):
        self.master = master
        self.canvas = canvas
        self.jump_height = jump_height
        self.moving = False
        self.bent = False
        self.distance = 0
        self.moving_id = None
        self.moving_bent_id = None
        #TODO: change image names
        self.img_pil_bent = Image.open("./assets/dino-down.png")
        self.img_pil_default = Image.open("./assets/dino.png")
        self.image = ImageTk.PhotoImage(self.img_pil_default)
        self.id = self.canvas.create_image(100, 650, image=self.image, anchor=NW)
        self.mask_bent = pickle.load( open( "./data/mask/dino_down_mask", "rb" ) )
        self.mask_default = pickle.load( open( "./data/mask/dino_mask", "rb" ) )
        self.mask = self.mask_default
        self.move_factor = {'x': 100, 'y': 650}
        self.onScreen = False
        keyboard.on_press_key('down', self.down)
        keyboard.on_release_key('down', self.awake)
        self.master.bind('<Up>', self.jump_call)
        #self.master.bind('<Down>', self.down)
        #self.master.bind('<DownLeave>', self.awake)
        #self.getColisionInfo()
    def jump_call(self, event):
        if(not self.moving):
            self.moving = True
            self.jump(event)
    def jump(self, event):
        if(self.distance<self.jump_height):
            self.distance+=1
            #self.canvas.move(self.id, 0, -1)
            self.move(0, -1)
            self.moving_id = self.canvas.after(3, self.jump, event)
        elif(self.distance>=self.jump_height and  self.canvas.coords(self.id)[-1]<650):
            self.distance+=1
            #self.canvas.move(self.id, 0, 1)
            self.move(0, 1)
            self.moving_id = self.canvas.after(3, self.jump, event)
        else:
            self.distance = 0
            self.moving = False
    def move(self, x=0, y=0):
        self.canvas.move(self.id, x, y)
        self.move_factor['x']+=x
        self.move_factor['y']+=y
        

    def down(self, event):
        if(self.moving):
            #self.master.after_cancel(self.moving_id)
            #self.moving = False
            self.distance = self.jump_height
            #coords = self.canvas.coords(self.id)
            #self.canvas.move(self.id, 0, 650-coords[1])
        else:
            if(not self.bent):
                self.mask = self.mask_bent
                self.move(0, 26)
                self.image = ImageTk.PhotoImage(self.img_pil_bent)
                self.canvas.itemconfig(self.id, image = self.image)
                self.bent = True
            """ if(self.moving_bent_id != None):
                self.canvas.after_cancel(self.moving_bent_id)
            self.moving_bent_id = self.canvas.after(400, self.awake) """
    def awake(self):
        if(self.bent):
            self.mask = self.mask_default
            self.move(0, -26)
            self.image = ImageTk.PhotoImage(self.img_pil_default)
            self.canvas.itemconfig(self.id, image = self.image)
            self.bent = False
            self.moving_bent_id = None
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
    def reset(self):
        self.moving = 0
        self.distance = 0
        coords = self.canvas.coords(self.id)
        #self.canvas.move(self.id, 0, 650-coords[1])
        self.move(0, 650-int(coords[1]))
    def pixelInMask(self, pixel, move_factor):
        #print("move f:", move_factor)
        #print("pixel: ", pixel)
        image_length = len(self.mask)
        init = 0
        end = image_length
        count = 0
        while True:
            count+=1
            i = int((end-init)/2) + init
            # binary search
            #print(i)
            #print(count)
            #print(self.move_factor)
            if(self.mask[i]['x']+self.move_factor['x'] == pixel['x']+move_factor['x']):
                back_count = 0
                while self.mask[i-back_count]['x']+self.move_factor['x'] == pixel['x']+move_factor['x']:
                    back_count+=1
                back_count-=1
                #print(back_count)
                # sequential search
                while (i-back_count)>-1 and (i-back_count)<image_length and self.mask[i-back_count]['x']+self.move_factor['x'] == pixel['x']+move_factor['x']:
                    #print(self.mask[i-back_count]['y']+self.move_factor['y'], "- ", pixel['y']+move_factor['y'])
                    if(self.mask[i-back_count]['y']+self.move_factor['y'] == pixel['y']+move_factor['y']):
                        #print(count)
                        return True
                    i+=1
                #print(count)
                return False
            elif(self.mask[i]['x']+self.move_factor['x'] > pixel['x']+move_factor['x']):
                end = i
            else:
                init = i + 1
            if (end-init)<=0:
                #print("cond: ", count)
                return False
