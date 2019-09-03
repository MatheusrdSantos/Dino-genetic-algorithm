from PIL import Image
import numpy as np
from colr import color
img_pil = Image.open("./assets/dino.png")
#a = np.asarray(img_pil)
pix_val = list(img_pil.getdata())

def printImage(image_vector, dimensions=[28,28], bg=False):
    for index, pixel in enumerate(image_vector, start=1):
        if bg:
            back = (pixel[3], pixel[3], pixel[3])
        else:
            back = (255-pixel[3], 255-pixel[3], 255-pixel[3])
        if(index%dimensions[0]==0):
            print(color(' ', fore=back, back=back))
        else:
            print(color(' ', fore=back, back=back), end="")

printImage(pix_val, [48, 50])

def reduceImageTo(image, originalDimension=[48, 50], newRation):
    pass
