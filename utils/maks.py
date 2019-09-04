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

#printImage(pix_val, [48, 50])

def reduceImageTo(image_list, originalDimension, reduceRatio):
    new_height = int(originalDimension[1]/reduceRatio)
    new_width = int(originalDimension[0]/reduceRatio)
    new_pix = [0 for x in range(0, new_height*new_width)]
    
    new_index = 0

    depht_count = 1
    for index in range(0, len(image_list)):
        index_range = index+reduceRatio
        for index in range(index, index_range):
            has_dark_pixel = False
            if(depht_count*reduceRatio<=originalDimension[1]):
                depht = reduceRatio
            else:
                depht = (reduceRatio - ((depht_count*reduceRatio) - originalDimension[1]))
            for count in range(0, depht):
                if(image_list[index+ (originalDimension[0]*count)][3] == 255):
                    has_dark_pixel = True
                    break
            if(has_dark_pixel):
                new_pix[new_index] = 1
                index = index_range
                break
        new_index+=1
        if(index%originalDimension[0] == 0):
            depht_count+=1
    return new_pix
print(reduceImageTo(pix_val, [48, 50], 5))

