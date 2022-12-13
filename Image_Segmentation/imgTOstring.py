"""
Author @Sippapas Sukpholtham
Master's Student in Mechanical and Aerospace Engineering
University of Florida
Dec, 2022

"""

from Image_Segmentation.CNN.CNN_1 import CNN

import numpy as np
import torch
import cv2
import os

# Activate the model
cnn = CNN()

# Load the weights of the trained model
cnn.load_state_dict(torch.load(
    'Image_Segmentation/CNN/model1.pth', map_location=torch.device('cpu')), strict=True)


def img2label(image):
    '''Interpreting the input image to label 

    Parameter:
        image (str): the path of the image that user want to input, the dimension of the image need to be (28,28)
    Return:
        predicted_label (int): the predicted label from Convolutional Neural Networks

    '''
    # read an image
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

    # change type of data from numpy to tensor before inputting into neural networks
    img = torch.from_numpy(img)

    # change the type of data to float
    img = img.type(torch.FloatTensor)/255

    # reshape an image
    img = img.reshape(1, 1, 28, 28)

    cnn.eval()
    output = cnn(img)[0]
    _, prediction = torch.max(output, 1)

    # the predicted label
    predicted_label = np.array(prediction[0])

    return predicted_label


def label2string(label):
    '''Interpreting the label (output) received from CNN to a readable equation string

    Parameter:
        label (int): the predicted output from CNN
    Return:
        character (str): string of the input label

    '''

    if label == 0:
        character = "0"
    elif label == 1:
        character = "1"
    elif label == 2:
        character = "2"
    elif label == 3:
        character = "3"
    elif label == 4:
        character = "4"
    elif label == 5:
        character = "5"
    elif label == 6:
        character = "6"
    elif label == 7:
        character = "7"
    elif label == 8:
        character = "8"
    elif label == 9:
        character = "9"
    elif label == 10:
        character = "-"
    elif label == 11:
        character = "+"
    elif label == 12:
        character = "*"
    elif label == 13:
        character = "a"
    elif label == 14:
        character = "b"
    elif label == 15:
        character = "/"
    elif label == 16:
        character = "="

    return character


def img2string(folder):
    '''Reading images which were segmented in the folder

    Parameter:
        folder (str): the path of the folder containing segmented images
    Return:
        str_equation (str): the equation which was interpreted from the folder

    '''
    str_equation = ""
    for file in os.listdir(folder):
        predicted_label = img2label(os.path.join(folder, file))
        character = label2string(predicted_label)

        # append each string
        str_equation = str_equation + character

    return str_equation
