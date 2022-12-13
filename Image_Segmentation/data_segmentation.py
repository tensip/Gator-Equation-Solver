"""
Author @Sippapas Sukpholtham
Master's Student in Mechanical and Aerospace Engineering
University of Florida
Dec, 2022

"""

import cv2
import os
import numpy as np

def remove_files(folder):
    '''Removing all images in the folder to prevent any segmented images from previous segmentation

    Parameter:
        folder (str): the path of the segmented folder

    '''

    # Remove all files in folder
    for f in os.listdir(folder):
        os.remove(os.path.join(folder, f))

def image_segmentation(file):
    '''Segmenting the input equation image to each character in the equation
       and save those images into the segmented folder
    
    Parameter:
        file (str): the directory of an image
    
    '''

    kernel = np.ones((3,3), np.uint8)
    img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    img = ~img
    gray = cv2.GaussianBlur(img, (7,7), 0)

    # Threshold the image
    _ , thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # Dilate the white portions
    dilate = cv2.dilate(thresh, kernel, iterations=1)

    # Remove noises in the image
    im = cv2.morphologyEx(dilate, cv2.MORPH_OPEN, kernel)
    im = cv2.morphologyEx(im, cv2.MORPH_CLOSE, kernel)

    # Find countours in the image
    cnts, _ = cv2.findContours(im.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    sorted_cnts = sorted(cnts, key=lambda cnt: cv2.boundingRect(cnt)[0])

    for i, cnt in enumerate(sorted_cnts):

        # Ignore some small contours
        if(cv2.contourArea(cnt) < 100):
            continue
        
        # Get bounding box
        x, y, w, h = cv2.boundingRect(cnt)

        # Cropping
        tol = 15
        char = img[y-tol:y+h+tol, x-tol:x+w+tol]

        # Resize the cropped image to (28,28)
        im_resize = cv2.resize(char, (28,28))

        # save the segmented characters into the folder
        cv2.imwrite("Image_Segmentation/segmented/char_" + str(i) + ".jpg",im_resize)


def clear_and_segment(image):
    '''Clear a segmented folder and save new segmented images from new equation
    
    Parameter:
        image(str): the directory of an image
    
    '''
    remove_files('Image_Segmentation/segmented')
    image_segmentation(image)
