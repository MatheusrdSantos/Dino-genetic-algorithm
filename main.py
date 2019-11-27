"""
Author: Matheus Santos
Description: file to call the main function in order to run the game 
"""
import sys
from classes.GameController import GameController
import weakref
args = sys.argv
game = GameController(args[1])
f = weakref.finalize(game, game.saveGeneralRecord)
game.run()