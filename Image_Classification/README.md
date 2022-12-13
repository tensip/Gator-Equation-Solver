# Image_Classification

The image classification folder was created for training convolutional neural network needed to be used for classifying the images. After finishing training the model, we also need to test the performance of the model. The training and testing model performance continued until we found the model that has the most accuracy (the best model).

**All files and folders in this part are not necessary for the GUI. You don't need to run anything here. The purpose of this `Image_Classification` folder is to illustrate what we have done so far before getting the best weight file for model**

### About the image classification

1. `data.7z` -- This file includes the handwriting images which are used for training the neural networks. The file need to be extracted before using it.
    
2. `Data_extracting.py` -- Download images from `data` folder which is extracted from `data.7z`, preprocess images, assign the label to the images, and save it as `data_for_train.npy` file

3. `data_for_training.zip` -- This zip file includes `data_for_training.npy`, which is the data set for training the Convolutional Neural Networks. This file is going to be generated after running `Data_extracting.py` file. You can either download this file directly or run the `Data_extracting.py` file

4. `train_CNN.ipynb` -- This file uses to train and validate to find the best model for handwriting math solver.

5. `test_CNN.ipynb` -- This file can be run to test any input data.

6. `modelX.pth` -- The best model that is generated from the `train_CNN.ipynb` file. There are 2 model which are `model1.pth` and `model4.pth`. The default model that is used in this project is `model1.pth`.

