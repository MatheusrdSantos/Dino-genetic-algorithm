"""
Author: Matheus Santos
Description: this class monitors the game elements. If a collision is detected, this class must notify the game controller.
"""
from math import sqrt, pow
class ColisionMonitor:
    def __init__(self, master, canvas, elements = [], obstacles = []):
        self.master = master
        self.canvas = canvas
        # elements that can't crash with blocks
        self.elements = elements
        self.obstacles = obstacles
    def start(self):
        self.verify_colisions()
        self.canvas.after(1, self.start)
    def verify_colisions(self):
        for element in self.elements:
            for obstacle in self.obstacles:
                if(self.crash(element, obstacle)):
                    self.stop_all()
                    return True
    def crash(self, element, obstacle):
        el_info = element.getColisionInfo()
        ob_info = obstacle.getColisionInfo()

        distance = sqrt(pow(ob_info['coords']['x'] - el_info['coords']['x'], 2) + pow(ob_info['coords']['y'] - el_info['coords']['y'], 2))

        if(distance<=el_info['radius_x']+ob_info['radius_x'] or distance<=el_info['radius_y']+ob_info['radius_y']):
            for pixel in obstacle.mask:
                if(element.pixelInMask(pixel)):
                    return True
            return False
    def stop_all(self):
        for element in self.elements:
            if(element.moving_id):
                self.canvas.after_cancel(element.moving_id)
        for obstacle in self.obstacles:
            if(obstacle.moving_id):
                self.canvas.after_cancel(obstacle.moving_id)