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
        self.obstacles = [
            Cactus(self.master, self.canvas, 3, self.decraseObstaclesOnscreen),
            Cactus(self.master, self.canvas, 1, self.decraseObstaclesOnscreen),
            Cactus(self.master, self.canvas, 2, self.decraseObstaclesOnscreen),
            FlyingDino(self.master, self.canvas, self.decraseObstaclesOnscreen),
            FlyingDino(self.master, self.canvas, self.decraseObstaclesOnscreen, 650)]
        self.lastOnScreenIndex = 0
        self.skipDistance = 0
    def run(self):
        self.canvas.after(20, self.updateSpawnState)
    def updateSpawnState(self):
        if(self.obstaclesOnScreen < 3 and self.obstacles[self.lastOnScreenIndex].getBoderRightDistance()>=self.skipDistance):
            self.spawnObstacle()
        self.run()
    def decraseObstaclesOnscreen(self):
        self.obstaclesOnScreen-=1
    def spawnObstacle(self):
        avaliable_index = []
        count = 0
        for obstacle in self.obstacles:
            if(not obstacle.onScreen):
                avaliable_index.append(count)
            count+=1
        self.obstaclesOnScreen+=1
        obstacle_index = avaliable_index[random.randint(0, len(avaliable_index)-1)]
        self.lastOnScreenIndex = obstacle_index
        self.skipDistance = random.randint(250, 400)
        self.obstacles[obstacle_index].draw()