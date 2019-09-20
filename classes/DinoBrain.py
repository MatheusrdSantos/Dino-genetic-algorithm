"""
Author: Matheus Santos
Description: this class represents the dino decision script. The decisions are made
by a simple neural net that receives inputs and compute an decision. 
"""

import numpy as np

class DinoBrain:
    def __init__(self, jumpAction = lambda x = None: x, bendAction = lambda x = None: x, W = np.random.rand(4,2), B = np.zeros((1,2))):
        self.jumpAction = jumpAction
        self.bendAction = bendAction
        self.W = W
        self.B = B
    def takeAction(self, X):
        Z = np.matmul(X, self.W) + (self.B)

        with np.nditer(Z, op_flags=['readwrite']) as it:
            for item in it:
                if(item<0):
                    print(item)
                    item[...] = 0
        if(Z[0][0]>Z[0][1]):
            self.jumpAction(None)
        else:
            self.bendAction(None)
    # mutate the brain params with random noise
    def mutate(self):
        pass
    def getClone(self):
        return DinoBrain(self.jumpAction, self.bendAction, W=np.array(self.W), B=np.array(self.B))