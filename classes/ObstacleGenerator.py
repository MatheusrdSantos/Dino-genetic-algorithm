"""
Author: Matheus Santos
Description: this class manage the obstacles spawn.
"""
from tkinter import Canvas, Tk, mainloop
import random
from classes.Cactus import Cactus
from classes.FlyingDino import FlyingDino

class ObstacleGenerator:
    def __init__(self, master, canvas):
        self.canvas = canvas
        self.obstaclesOnScreen = 0
        self.master = master
        self.obstacles = [Cactus(self.master, self.canvas), FlyingDino(self.master, self.canvas)]
    def run(self):
        self.canvas.after(20, self.updateSpawnState)
    def updateSpawnState(self):
        if(self.obstaclesOnScreen == 0):
            self.spawnObstacle()
    def spawnObstacle(self):
        avaliable_index = []
        count = 0
        for obstacle in self.obstacles:
            if(obstacle.onScreen):
                avaliable_index.append(count)
            count+=1
        self.obstaclesOnScreen+=1
        self.obstacles[avaliable_index[random.randint(0, len(count)-1)]].drawn()