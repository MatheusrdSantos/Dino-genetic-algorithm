"""
Author: Matheus Santos
Description: file to call the main function in order to run the game 
"""
import sys
from classes.GameController import GameController
args = sys.argv
game = GameController(args[1])
game.run()