import cv2
import os
import numpy as np

def remove_files(folder):
    for f in os.listdir(folder):
        os.remove(os.path.join(folder, f))

def image_segmentation(file):
    kernel = np.ones((3,3), np.uint8)
    img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    img = ~img
    gray = cv2.GaussianBlur(img, (7,7), 0)

    # Threshold the image
    _ , thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # Dilate the white portions
    dilate = cv2.dilate(thresh, kernel, iterations=1)

    # remove noises in the image
    im = cv2.morphologyEx(dilate, cv2.MORPH_OPEN, kernel)
    im = cv2.morphologyEx(im, cv2.MORPH_CLOSE, kernel)

    # Find countours in the image
    cnts, _ = cv2.findContours(im.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    sorted_cnts = sorted(cnts, key=lambda cnt: cv2.boundingRect(cnt)[0])
    
    # cnt = cnts[0]
    
    orig = img.copy()

    for i, cnt in enumerate(sorted_cnts):

        if(cv2.contourArea(cnt) < 100):
            continue
        
        # Get bounding box
        x, y, w, h = cv2.boundingRect(cnt)

        # Cropping
        tol = 15
        char = img[y-tol:y+h+tol, x-tol:x+w+tol]
        
        cv2.rectangle(orig,(x-tol,y-tol),(x+w+tol,y+h+tol),(255,255,0),2)

        im_resize = cv2.resize(char, (28,28))

        # save the segmented characters
        cv2.imwrite("Image_Segmentation/segmented/char_" + str(i) + ".jpg",im_resize)

    # cv2.imshow('Image', orig)
    # cv2.waitKey(0)

def rm_files_and_segment(image):
    remove_files('Image_Segmentation/segmented')
    image_segmentation(image)


# def main():
#     remove_files('segmented')
#     image_segmentation('test_3.jpg')


# if __name__=='__main__':
#     main()
