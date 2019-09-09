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

def reduceImageTo(image_list, originalDimension, reduceRatio):
    new_height = int(originalDimension[1]/reduceRatio)
    new_width = int(originalDimension[0]/reduceRatio)
    print("h: ", new_height)
    print("w: ", new_width)
    new_image = [0 for x in range(0, new_height*new_width)]

    line_count = 0
    # iterates over the entire new image
    for i in range(0, len(new_image)):
        # iterates over the pixel on original image that represents
        # the pixel at i position on new_image
        if(i>0 and (i%new_width)==0):
            line_count+=1
        for j in range(0, reduceRatio):
            if(new_image[i] == 1):
                break
            # searchs in depht a black pixel 
            for k in range(0, reduceRatio):
                original_pixel_pos = (line_count*originalDimension[0]*(reduceRatio-1))+(i*reduceRatio)+j + ((k)*originalDimension[0])
                #print(original_pixel_pos)
                if(image_list[original_pixel_pos][3] == 255):
                    new_image[i] = 1
                    break
    return new_image
resized_image = reduceImageTo(pix_val, [48, 50], 1)
print(len(resized_image))

def printBinaryImage(image_vector, dimensions=[28,28], bg=False):
    for index, pixel in enumerate(image_vector, start=1):
        if bg:
            back = (pixel*255, pixel*255, pixel*255)
        else:
            back = (255-(pixel*255), 255-(pixel*255), 255-(pixel*255))
        if(index%dimensions[0]==0):
            print(color(' ', fore=back, back=back))
        else:
            print(color(' ', fore=back, back=back), end="")

printBinaryImage(resized_image, [48, 10])

def getBorder(image_vector, dimensions):
    new_image_vector = [0 for pixel in image_vector]
    # dimensions[0] = x (width) --> i
    # dimensions[1] = y (height) --> j
    for j in range(0, dimensions[1]):

        for i in range(0, dimensions[0]):

            original_index = (j*dimensions[0]) + i
            # check wether tha pixel is in the image
            # border or not
            if(j == 0 or i==0 or j==dimensions[1]-1 or i==dimensions[0]-1):
                if(image_vector[original_index] == 1):
                    new_image_vector[original_index] = 1
            else:
                if(image_vector[original_index] == 1):
                    
                    pixel_above = ((j-1)*dimensions[0]) + i
                    pixel_right = ((j)*dimensions[0]) + i + 1
                    pixel_bottom = ((j+1)*dimensions[0]) + i
                    pixel_left = ((j)*dimensions[0]) + i - 1
                    
                    if( image_vector[pixel_above]==0 or
                        image_vector[pixel_right] == 0 or
                        image_vector[pixel_bottom] == 0 or
                        image_vector[pixel_left] == 0):
                        new_image_vector[original_index] = 1
    return new_image_vector
print("---------")
border_only = getBorder(resized_image, [48, 50])
printBinaryImage(border_only, [48, 50])

def countBlackPixels(image_vector):
    count = 0
    for pixel in image_vector:
        if(pixel == 1):
            count+=1
    return count

print("Resize: ", countBlackPixels(resized_image))
print("Border only: ", countBlackPixels(border_only))