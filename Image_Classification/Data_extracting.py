"""
Author @Sippapas Sukpholtham
Master's Student in Mechanical and Aerospace Engineering
University of Florida
Dec, 2022

"""
import numpy as np
import cv2
import os

# loading images and preprocessing
def load_images_from_folder(folder):
    '''Download the raw images and preprocess it
    
    Parameter:
        folder (str): the directory of the folder
    Return: 
        train_data (list): a list contains a number of RGB values for each pixel. The dimension is (28*28,1)
        
    '''
    # Create empty list
    train_data = []

    kernel = np.ones((3,3), np.uint8)
    # width 
    w = 28
    # height
    h = w
    
    # loop in the folder
    for i, filename in enumerate(os.listdir(folder)):
        img = cv2.imread(os.path.join(folder,filename),cv2.IMREAD_GRAYSCALE)
        img = ~img
        if img is not None and i < 800:
            # _ , thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
            im = cv2.dilate(img, kernel, iterations=1)
            im = cv2.morphologyEx(im, cv2.MORPH_OPEN, kernel)
            im = cv2.morphologyEx(im, cv2.MORPH_CLOSE, kernel)
            
            im_resize = cv2.resize(im,(w,h))
            im_reshape = np.reshape(im_resize,(w*h,1))
            train_data.append(im_reshape)
        else:
            break
    return train_data

# empty list for collecting data
data = []

# assign '0' = 0
data = load_images_from_folder('data/0')

for i, each in enumerate(data):
    data[i] = np.append(each, ['0'])

# assign '1' = 1
data1 = load_images_from_folder('data/1')

for i, each in enumerate(data1):
    data1[i] = np.append(each, ['1'])

data = np.concatenate((data,data1))

# assign '2' = 2
data2 = load_images_from_folder('data/2')

for i, each in enumerate(data2):
    data2[i] = np.append(each, ['2'])

data = np.concatenate((data,data2))

# assign '3' = 3
data3 = load_images_from_folder('data/3')

for i, each in enumerate(data3):
    data3[i] = np.append(each, ['3'])

data = np.concatenate((data,data3))

# assign '4' = 4
data4 = load_images_from_folder('data/4')

for i, each in enumerate(data4):
    data4[i] = np.append(each, ['4'])

data = np.concatenate((data,data4))

# assign '5' = 5
data5 = load_images_from_folder('data/5')

for i, each in enumerate(data5):
    data5[i] = np.append(each, ['5'])

data = np.concatenate((data,data5))

# assign '6' = 6
data6 = load_images_from_folder('data/6')

for i, each in enumerate(data6):
    data6[i] = np.append(each, ['6'])

data = np.concatenate((data,data6))

# assign '7' = 7
data7=load_images_from_folder('data/7')

for i, each in enumerate(data7):
    data7[i] = np.append(each, ['7'])

data = np.concatenate((data,data7))

# assign '8' = 8
data8=load_images_from_folder('data/8')

for i, each in enumerate(data8):
    data8[i] = np.append(each, ['8'])

data = np.concatenate((data,data8))

# assign '9' = 9
data9 = load_images_from_folder('data/9')

for i, each in enumerate(data9):
    data9[i] = np.append(each, ['9'])

data = np.concatenate((data,data9))

# assign '-' = 10
data10 = load_images_from_folder('data/-')

for i, each in enumerate(data10):
    data10[i] = np.append(each, ['10'])

data = np.concatenate((data,data10))

# assign '+' = 11
data11 = load_images_from_folder('data/+')

for i, each in enumerate(data11):
    data11[i] = np.append(each, ['11'])

data = np.concatenate((data,data11))

# assign '*' = 12
data12 = load_images_from_folder('data/times')

for i, each in enumerate(data12):
    data12[i] = np.append(each, ['12'])

data = np.concatenate((data,data12))

# assign 'a' = 13
data13 = load_images_from_folder('data/A')

for i, each in enumerate(data13):
    data13[i] = np.append(each, ['13'])

data = np.concatenate((data,data13))

# assign 'b' = 14
data14 = load_images_from_folder('data/b')

for i, each in enumerate(data14):
    data14[i] = np.append(each, ['14'])
    
data = np.concatenate((data,data14))

# assign '/' = 15
data15 = load_images_from_folder('data/div')

for i, each in enumerate(data15):
    data15[i] = np.append(each, ['15'])

data = np.concatenate((data,data15))

# assign '=' = 16
data16 = load_images_from_folder('data/=')

for i, each in enumerate(data16):
    data16[i] = np.append(each, ['16'])

data = np.concatenate((data,data16))

# save data as .npy file
np.save('data_for_training', data)