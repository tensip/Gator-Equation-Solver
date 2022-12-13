# Image_Segmentation

The image segmentation folder was created for segmenting the hand-writing equation into characters before putting it into the convolutional neural network.

### About the image segmentation

1. `CNN` -- This folder includes the designed convolutional neural networks and the weight of model which we got by training and testing from Image_Classification part
    - `CNN_1.py` -- The first designed convolutional neural networks and the one that is used for this project
    - `CNN_2.py` -- The second designed convolutional neural networks.
    - `model1.pth` -- The copied weight model from `Image_Classification` folder
    - `model4.pth` -- The copied weight model from `Image_Classification` folder

2. `segmented` -- This folder contains segmented characters from the equation

3. `data_segmentation.py` -- The algorithm for segmentating a hand-writing math equation. The segmented images will be saved in `segmented` folder

4. `imgTOstring.py` -- The algorithm for performing an optical character recognition (OCR).