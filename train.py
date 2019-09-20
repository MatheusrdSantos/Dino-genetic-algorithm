"""
Author: Matheus Santos
Description: file to call the main function in order to see dino training 
"""

from classes.GameController import GameController

game = GameController("train")
game.run()