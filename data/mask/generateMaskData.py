import pickle
import sys, os
sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from utils.mask import generateMaskData

generateMaskData("dino.png", "dino_mask")
generateMaskData("dino-down.png", "dino_down_mask")
generateMaskData("flying-dino.png", "flying_dino_mask")
generateMaskData("obstacle-1x.png", "obstacle_1_mask")
generateMaskData("obstacle-2x-small.png", "obstacle_2_mask")
generateMaskData("obstacle-3x.png", "obstacle_3_mask")