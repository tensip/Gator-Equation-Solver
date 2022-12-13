# Gator-Equation-Solver

This resporitory includes *three* main folders

### Image_Classification 
The image classification folder was created for training convolutional neural network needed to be used for classifying the images. After finishing training the model, we also need to test the performance of the model. The training and testing model performance continued until we found the model that has the most accuracy (the best model).

1. `data` -- This folder includes the handwriting images which are used for training the neural networks
    
2. `Data_extracting.py` -- Download images from `data`, preprocess the training images, assign the label to the images, and save it as `data_for_train.npy` file

3. `train_CNN.ipynb` -- This file uses to train and validate to find the best model for handwriting math solver.

4. `model.pth` -- The best model that is generated from the `train_CNN.ipynb` file. 

5. `test_CNN.ipynb` -- This file can be run to test any input data.

### Image_Segmentation
The input for the hand-writing equation solver is the *whole* equation including numbers and math signs. Therfore, the image need to be segmented before classifying characters.

### GUI