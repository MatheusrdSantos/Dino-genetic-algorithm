"""
Author: Matheus Santos
Description: this class manage the entire game state.
"""
from tkinter import *
from PIL import Image, ImageTk
from classes.CollisionMonitor import ColisionMonitor
from classes.Dino import Dino
from classes.Cactus import Cactus

class GameController:
    def __init__(self, mode):
        #can be either a train or a game
        self.mode = mode
        self.master = Tk()
        self.canvas = Canvas(self.master, width=800, height=800, bg='#eee')
        self.colisionMonitor = ColisionMonitor(self.master, self.canvas)
        self.dino = None
        self.cactus = None
    def run(self):
        if(self.mode == "game"):
            self.canvas.pack()
            self.prepareGame()
            mainloop()
    # create game elements
    def prepareGame(self):
        self.dino = Dino(self.master, self.canvas)
        self.cactus = Cactus(self.master, self.canvas)