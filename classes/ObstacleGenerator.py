"""
Author: Matheus Santos
Description: this class manage the obstacles spawn.
"""
from tkinter import Canvas, Tk, mainloop
import random
from classes.Cactus import Cactus
from classes.FlyingDino import FlyingDino
class ObstacleGenerator:
    def __init__(self, master, canvas, updateGameParams, increaseScore):
        self.canvas = canvas
        self.obstaclesOnScreen = 0
        self.master = master
        self.obstacles = [
            Cactus(self.master, self.canvas, self.updateFirstObstacle,3, self.decraseObstaclesOnscreen),
            Cactus(self.master, self.canvas, self.updateFirstObstacle, 1, self.decraseObstaclesOnscreen),
            Cactus(self.master, self.canvas, self.updateFirstObstacle,2, self.decraseObstaclesOnscreen),
            FlyingDino(self.master, self.canvas, self.updateFirstObstacle, self.decraseObstaclesOnscreen),
            FlyingDino(self.master, self.canvas, self.updateFirstObstacle,self.decraseObstaclesOnscreen, 625)]
        self.lastOnScreenIndex = 0
        self.skipDistance = 0
        self.updateGameParams = updateGameParams
        self.increaseScore = increaseScore
        self.obstaclesIndexQueue = []
        self.firstObstacle = None
    def run(self):
        if(len(self.obstaclesIndexQueue)>0):
            obstacle = self.obstacles[self.firstObstacle]
            # [left top right bottom]
            obstacle_box = obstacle.getBox()
            obstacle_distance = abs(int(obstacle_box[0]) - 150)
            #print(obstacle.height)
            self.updateGameParams(distance=obstacle_distance, height=obstacle.height, width=obstacle.width)
        self.canvas.after(20, self.updateSpawnState)

    def updateSpawnState(self):
        if(self.obstaclesOnScreen < 3 and self.obstacles[self.lastOnScreenIndex].getBoderRightDistance()>=self.skipDistance):
            self.spawnObstacle()
        self.run()
    def decraseObstaclesOnscreen(self):
        self.obstaclesOnScreen-=1
    def spawnObstacle(self):
        self.increaseScore(1)
        avaliable_index = []
        count = 0
        for obstacle in self.obstacles:
            if(not obstacle.onScreen):
                avaliable_index.append(count)
            count+=1
        self.obstaclesOnScreen+=1
        obstacle_index = avaliable_index[random.randint(0, len(avaliable_index)-1)]
        self.lastOnScreenIndex = obstacle_index
        self.skipDistance = random.randint(280, 410)
        self.obstacles[obstacle_index].canCollid = True
        self.obstacles[obstacle_index].draw()
        if(self.obstaclesOnScreen==1):
            self.firstObstacle = obstacle_index
        self.obstaclesIndexQueue.append(obstacle_index)
    def updateFirstObstacle(self):
        self.obstaclesIndexQueue.pop(0)
        self.firstObstacle = self.obstaclesIndexQueue[0]
        #print(self.obstaclesIndexQueue)
    def updateObstaclesSpeed(self, speed):
        for obstacle in self.obstacles:
            obstacle.changeSpeed(speed)
    def reset(self):
        for obstacle in self.obstacles:
            obstacle.reset()
        self.obstaclesOnScreen = 0
        self.lastOnScreenIndex = 0
        self.skipDistance = 0
        self.firstObstacle = None
        self.obstaclesIndexQueue = []