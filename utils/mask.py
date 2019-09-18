from PIL import Image
import numpy as np
from colr import color

def printImage(image_path, bg=False):
    img_pil = Image.open(image_path)
    dimensions = img_pil.size
    image_vector = list(img_pil.getdata())
    for index, pixel in enumerate(image_vector, start=1):
        if bg:
            back = (pixel[3], pixel[3], pixel[3])
        else:
            back = (255-pixel[3], 255-pixel[3], 255-pixel[3])
        if(index%dimensions[0]==0):
            print(color(' ', fore=back, back=back))
        else:
            print(color(' ', fore=back, back=back), end="")

def reduceImageTo(image_path, reduceRatio):
    img_pil = Image.open(image_path)
    originalDimension = img_pil.size
    image_list = list(img_pil.getdata())

    new_height = int(originalDimension[1]/reduceRatio)
    new_width = int(originalDimension[0]/reduceRatio)

    new_image = [0 for x in range(new_height*new_width)]

    line_count = 0
    # iterates over the entire new image
    for i in range(0, len(new_image)):
        # iterates over the pixel on original image that represents
        # the pixel at i position on new_image
        if(i>0 and (i%new_width)==0):
            line_count+=1
        for j in range(reduceRatio):
            if(new_image[i] == 1):
                break
            # searchs in depht a black pixel 
            for k in range(0, reduceRatio):
                original_pixel_pos = (line_count*originalDimension[0]*(reduceRatio-1))+(i*reduceRatio)+j + ((k)*originalDimension[0])
                if(image_list[original_pixel_pos][3] == 255):
                    new_image[i] = 1
                    break
    return {'image': new_image, 'dimensions': (new_width, new_height)}

def printBinaryImage(image_vector, dimensions, bg=False):
    for index, pixel in enumerate(image_vector, start=1):
        if bg:
            back = (pixel*255, pixel*255, pixel*255)
        else:
            back = (255-(pixel*255), 255-(pixel*255), 255-(pixel*255))
        if(index%dimensions[0]==0):
            print(color(' ', fore=back, back=back))
        else:
            print(color(' ', fore=back, back=back), end="")

def getBorder(image_vector, dimensions):
    new_image_vector = [0 for pixel in image_vector]
    # dimensions[0] = x (width) --> i
    # dimensions[1] = y (height) --> j
    for j in range(dimensions[1]):

        for i in range(dimensions[0]):

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
    return {'image': new_image_vector, 'dimensions': dimensions}

def countBlackPixels(image_vector):
    count = 0
    for pixel in image_vector:
        if(pixel == 1):
            count+=1
    return count

def getBorderCoords(image_vector, dimensions):
    border_mask = []
    # dimensions[0] = x (width) --> i
    # dimensions[1] = y (height) --> j
    for j in range(dimensions[1]):

        for i in range(dimensions[0]):

            original_index = (j*dimensions[0]) + i
            if(image_vector[original_index] == 1):
                border_mask.append({'x': i, 'y': j})
    return border_mask

def sortAxis(image_vector):
    img_length = len(image_vector)
    # sort by X axis
    smallest = 0
    for i in range(img_length-1):
        for j in range(img_length-1):
            if(image_vector[j]['x']>image_vector[j+1]['x']):
                image_vector[j], image_vector[j+1] = image_vector[j+1], image_vector[j]

    # sort by Y axis
    init = 0
    while init<img_length-1:
        curr_pixel = image_vector[init]
        end = init
        while (image_vector[end]['x'] == curr_pixel['x']) and end<img_length-1:
            end+=1
        for i in range(init, end):
            for j in range(init, end-1):
                if(image_vector[j]['y']>image_vector[j+1]['y']):
                    image_vector[j], image_vector[j+1] = image_vector[j+1], image_vector[j]
        init = end
    return image_vector

def hasPixel(image_vector, pixel):
    image_length = len(image_vector)
    init = 0
    end = image_length
    count = 0
    while True:
        count+=1
        i = int((end-init)/2) + init
        # binary search
        if(image_vector[i]['x'] == pixel['x']):
            back_count = 0
            while image_vector[i-back_count]['x'] == pixel['x']:
                back_count+=1
            back_count-=1
            # sequential search
            while image_vector[i-back_count]['x'] == pixel['x']:
                if(image_vector[i-back_count]['y'] == pixel['y']):
                    return True
                i+=1
            return False
        elif(image_vector[i]['x'] > pixel['x']):
            end = i
        else:
            init = i + 1
        if (end-init)<0:
            return False