"""
Author: Matheus Santos
Description: this class monitors the game elements. If a collision is detected, this class must notify the game controller.
"""

class ColisionMonitor:
    def __init__(self, master, canvas, elements = [], obstacles = []):
        self.master = master
        self.canvas = canvas
        # elements that can't crash with blocks
        self.elements = elements
        self.obstacles = obstacles