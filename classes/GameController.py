"""
Author: Matheus Santos
Description: this class manage the entire game state.
"""
from tkinter import Canvas, Tk, mainloop, NW
from PIL import Image, ImageTk
from classes.CollisionMonitor import ColisionMonitor
from classes.Dino import Dino
from classes.Cactus import Cactus
from classes.FlyingDino import FlyingDino
from classes.CollisionMonitor import ColisionMonitor
from classes.ObstacleGenerator import ObstacleGenerator
from classes.DinoBrain import DinoBrain

class GameController:
    def __init__(self, mode):
        #can be either a train or a game
        self.mode = mode
        self.master = Tk()
        self.canvas = Canvas(self.master, width=800, height=800, bg='#eee')
        self.colisionMonitor = ColisionMonitor(self.master, self.canvas, self.stopGround)
        self.dinos = []
        self.obstacles = []
        self.colisionMonitor = None
        self.obstacleGenerator = None
        self.game_params = {'distance': 100, 'speed': 20, 'height': 0, 'width': 50}
        self.master.bind('<r>', self.restart)
        self.imgs_pil_ground = [
            Image.open("./assets/ground.png"),
            Image.open("./assets/ground-1.png")]
        self.ground = ImageTk.PhotoImage(self.imgs_pil_ground[0])
        self.ground_1 = ImageTk.PhotoImage(self.imgs_pil_ground[1])
        # display image on canvas
        self.ground_id = self.canvas.create_image(0, 695, image=self.ground, anchor=NW)
        self.ground_id_1 = self.canvas.create_image(400, 695, image=self.ground_1, anchor=NW)
        self.ground_id_2 = self.canvas.create_image(800, 695, image=self.ground, anchor=NW)
        self.ground_animation_id = None
    def animateGround(self):
        self.canvas.move(self.ground_id, -9, 0)
        self.canvas.move(self.ground_id_1, -9, 0)
        self.canvas.move(self.ground_id_2, -9, 0)
        #[left top right bottom]
        if(self.canvas.coords(self.ground_id)[0]<-400):
            self.canvas.move(self.ground_id, 1200, 0)
        if(self.canvas.coords(self.ground_id_1)[0]<-400):
            self.canvas.move(self.ground_id_1, 1200, 0)
        if(self.canvas.coords(self.ground_id_2)[0]<-400):
            self.canvas.move(self.ground_id_2, 1200, 0)
        self.ground_animation_id = self.canvas.after(20, self.animateGround)
    
    def run(self):
        if(self.mode == "game"):
            self.canvas.pack()
            self.prepareGame()
            self.animateGround()
            mainloop()
        elif(self.mode == "train"):
            self.canvas.pack()
            self.prepareTrain()
            self.animateGround()
            mainloop()

    def updateGameParams(self, distance=None, speed=None, height=None, width=None):
        if(distance):
           self.game_params['distance'] = distance 
        if(speed):
           self.game_params['speed'] = speed 
        if(height):
           self.game_params['height'] = height 
        if(width):
           self.game_params['width'] = width 
        
    # create game elements
    def prepareGame(self):
        self.dinos.append(Dino(self.master, self.canvas, DinoBrain(), self.game_params))
        self.obstacleGenerator = ObstacleGenerator(self.master, self.canvas, self.updateGameParams)
        self.obstacleGenerator.run()
        self.colisionMonitor = ColisionMonitor(self.master, self.canvas, self.stopGround, self.dinos, self.obstacleGenerator.obstacles)
        self.colisionMonitor.start()
    # create train elements
    def prepareTrain(self):
        self.dinos.append(Dino(self.master, self.canvas, DinoBrain(), self.game_params, mode=self.mode))
        self.dinos.append(Dino(self.master, self.canvas, DinoBrain(), self.game_params, mode=self.mode))
        self.dinos.append(Dino(self.master, self.canvas, DinoBrain(), self.game_params, mode=self.mode))
        self.dinos.append(Dino(self.master, self.canvas, DinoBrain(), self.game_params, mode=self.mode))
        self.dinos.append(Dino(self.master, self.canvas, DinoBrain(), self.game_params, mode=self.mode))
        self.dinos.append(Dino(self.master, self.canvas, DinoBrain(), self.game_params, mode=self.mode))
        self.obstacleGenerator = ObstacleGenerator(self.master, self.canvas, self.updateGameParams)
        self.obstacleGenerator.run()
        self.colisionMonitor = ColisionMonitor(self.master, self.canvas, self.stopGround, self.dinos, self.obstacleGenerator.obstacles)
        self.colisionMonitor.start()
    def stopGround(self):
        self.canvas.after_cancel(self.ground_animation_id)
    def restart(self, event):
        for dino in self.dinos:
            dino.reset()
        self.animateGround()
        self.obstacleGenerator.reset()
        self.obstacleGenerator.run()