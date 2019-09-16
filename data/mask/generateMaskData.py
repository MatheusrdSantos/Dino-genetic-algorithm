import pickle
import sys, os

# chage this path to work in any computer directory
sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from utils.mask import reduceImageTo, getBorder, getBorderCoords, sortAxis

dino = reduceImageTo("./assets/dino.png", 1)
dino_border = getBorder(dino['image'], dino['dimensions'])
dino_border_coords = getBorderCoords(dino_border['image'], dino_border['dimensions'])
dino_border_coords = sortAxis(dino_border_coords)

with open('./data/mask/dino_mask', 'wb') as f:
    pickle.dump(dino_border_coords, f)

flying_dino = reduceImageTo("./assets/flying-dino.png", 1)
flying_dino_border = getBorder(flying_dino['image'], flying_dino['dimensions'])
flying_dino_border_coords = getBorderCoords(flying_dino_border['image'], flying_dino_border['dimensions'])
flying_dino_border_coords = sortAxis(flying_dino_border_coords)

with open('./data/mask/flying_dino_mask', 'wb') as f:
    pickle.dump(flying_dino_border_coords, f)

obstacle_1 = reduceImageTo("./assets/obstacle-1x.png", 1)
obstacle_1_border = getBorder(obstacle_1['image'], obstacle_1['dimensions'])
obstacle_1_border_coords = getBorderCoords(obstacle_1_border['image'], obstacle_1_border['dimensions'])
obstacle_1_border_coords = sortAxis(obstacle_1_border_coords)

with open('./data/mask/obstacle_1_mask', 'wb') as f:
    pickle.dump(obstacle_1_border_coords, f)

obstacle_2 = reduceImageTo("./assets/obstacle-2x-small.png", 1)
obstacle_2_border = getBorder(obstacle_2['image'], obstacle_2['dimensions'])
obstacle_2_border_coords = getBorderCoords(obstacle_2_border['image'], obstacle_2_border['dimensions'])
obstacle_2_border_coords = sortAxis(obstacle_1_border_coords)

with open('./data/mask/obstacle_2_mask', 'wb') as f:
    pickle.dump(obstacle_2_border_coords, f)

obstacle_3 = reduceImageTo("./assets/obstacle-3x.png", 1)
obstacle_3_border = getBorder(obstacle_3['image'], obstacle_3['dimensions'])
obstacle_3_border_coords = getBorderCoords(obstacle_3_border['image'], obstacle_3_border['dimensions'])
obstacle_3_border_coords = sortAxis(obstacle_1_border_coords)

with open('./data/mask/obstacle_3_mask', 'wb') as f:
    pickle.dump(obstacle_3_border_coords, f)