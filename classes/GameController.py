"""
Author: Matheus Santos
Description: this class manage the entire game state.
"""
from tkinter import Canvas, Tk, mainloop, NW, Label
from PIL import Image, ImageTk
from classes.CollisionMonitor import ColisionMonitor
from classes.Dino import Dino
from classes.Cactus import Cactus
from classes.FlyingDino import FlyingDino
from classes.CollisionMonitor import ColisionMonitor
from classes.ObstacleGenerator import ObstacleGenerator
from classes.DinoBrain import DinoBrain
import sys

class GameController:
    def __init__(self, mode):
        #can be either a train or a game
        self.mode = mode
        self.master = Tk()
        self.canvas = Canvas(self.master, width=800, height=800, bg='#fff')
        self.colisionMonitor = ColisionMonitor(self.master, self.canvas, self.stopGround)
        self.dinos = []
        self.dinosOnScreen = 0
        self.obstacles = []
        self.colisionMonitor = None
        self.obstacleGenerator = None
        self.initialDinoNum = 10
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
        self.interfaceObject = {}
        self.score = 0
    def prepareInterface(self):
        speedLabel = Label(self.master, text="Speed: "+str(self.game_params['speed']), bg='#fff')
        speedLabel.pack()
        self.interfaceObject['speedLabel'] = speedLabel

        dinosAlive = Label(self.master, text="Dinos: "+str(self.initialDinoNum), bg='#fff')
        dinosAlive.pack()
        self.interfaceObject['dinosAlive'] = dinosAlive
        
        scoreLabel = Label(self.master, text="Score: "+str(self.score), bg='#fff')
        scoreLabel.pack()
        self.interfaceObject['score'] = scoreLabel
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
            self.prepareInterface()
            self.canvas.pack()
            self.prepareTrain()
            self.animateGround()
            mainloop()
    def decreaseDinos(self):
        self.dinosOnScreen-=1
        self.colisionMonitor.dinosOnScreen = self.dinosOnScreen
        self.interfaceObject['dinosAlive'].config(text="Dinos: "+str(self.dinosOnScreen))

    def updateGameParams(self, distance=None, speed=None, height=None, width=None):
        if(not distance is None):
           self.game_params['distance'] = distance
        if(not speed is None):
           self.game_params['speed'] = speed
        if(not height is None):
           self.game_params['height'] = height 
        if(not width is None):
           self.game_params['width'] = width
        #print(self.game_params)
        
    # create game elements
    def prepareGame(self):
        self.dinos.append(Dino(self.master, self.canvas, DinoBrain(), self.game_params, self.decreaseDinos))
        self.obstacleGenerator = ObstacleGenerator(self.master, self.canvas, self.updateGameParams)
        self.obstacleGenerator.run()
        self.colisionMonitor = ColisionMonitor(self.master, self.canvas, self.stopGround, self.dinos, self.obstacleGenerator.obstacles)
        self.colisionMonitor.start()
    # create train elements
    def prepareTrain(self):
        for i in range(self.initialDinoNum):
            self.dinosOnScreen+=1
            self.dinos.append(Dino(self.master, self.canvas, DinoBrain(), self.game_params, self.decreaseDinos, mode=self.mode))
        self.obstacleGenerator = ObstacleGenerator(self.master, self.canvas, self.updateGameParams, self.increaseScore)
        self.obstacleGenerator.run()
        self.colisionMonitor = ColisionMonitor(self.master, self.canvas, self.stopGround, self.dinos, self.obstacleGenerator.obstacles, self.dinosOnScreen)
        self.colisionMonitor.run()
    def stopGround(self):
        print("New gen")
        self.game_params = {'distance': 100, 'speed': 20, 'height': 0, 'width': 50}
        self.canvas.after_cancel(self.ground_animation_id)
        brain_index = None
        for i, dino in enumerate(self.dinos):
            if(dino.best):
                brain_index = i
                print("best: ", brain_index)
        #self.dinos.append(Dino(self.master, self.canvas, self.dinos[0].brain.getClone(), self.game_params, mode=self.mode))
        #self.dinos[0].die()
        """ for i in range(9):
            self.dinos.append(Dino(self.master, self.canvas, self.dinos[0].brain.getClone(True), self.game_params, mode=self.mode)) """
        self.obstacleGenerator.reset()
        for  i, dino in enumerate(self.dinos):
            dino.reset()
            #print("reset",i)
            if(i != brain_index):
                dino.setBrain(self.dinos[brain_index].brain.getClone(True))
         
        for  i, dino in enumerate(self.dinos):
            dino.game_params = self.game_params
            dino.animate()
            dino.run()
        self.score = 0

        self.dinosOnScreen = len(self.dinos)
        self.colisionMonitor.dinosOnScreen = self.dinosOnScreen
        
        self.interfaceObject['dinosAlive'].config(text="Dinos: "+str(self.dinosOnScreen))
        self.interfaceObject['score'].config(text="Score: "+str(self.score))

        self.animateGround()
        self.colisionMonitor.run()
        self.obstacleGenerator.run()
    def increaseScore(self, score):
        self.score+=score
        self.interfaceObject['score'].config(text="Score: "+str(self.score))
    def restart(self, event):
        for dino in self.dinos:
            dino.reset()
        self.game_params = {'distance': 100, 'speed': 20, 'height': 0, 'width': 50}
        self.animateGround()
        self.obstacleGenerator.reset()
        self.obstacleGenerator.run()