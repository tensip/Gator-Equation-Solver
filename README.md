# Final Project

This is a **group assignment**.

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#dependencies">Dependencies</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#authors">Authors</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This report is part of the final project in the EEL5840 – Fundamental of Machine Learning course. The purpose of the project is to make a model that can learn handwritten letters. The model was built using Python programming language. All the data used in this project were created from the students in the course. Before going into the model, preprocessing methods are needed for the model to reach higher accuracy. The preprocessing methods that we used in this project include inverting the color of the grayscale image, dilating the characters, removing background noise, filling in the characters, and resizing the images. After the preprocessing, the training data was split into training and validation sets. The training set was used to learn the parameters in the convolutional neural network. Then, the validation set was used to evaluate the performance of the model. The highest accuracy score that we achieved for the validation set was 92 percent. The parameters used to achieve the highest accuracy score were used to train the entire training set. The weight coefficients and the parameters were saved for further use in predicting the characters in the test set.

<!-- GETTING STARTED -->
## Getting Started

In this section all libraries, packages and other dependencies that need to be installed are listed along with the instruction on how to recreate the project locally. 

### Dependencies

These are all libraries, packages and other dependencies that need to be installed to run the project.

* matplotlib 3.5.1
  ```sh
  conda install -c conda-forge matplotlib
  ```
* numpy 1.21.5
  ```sh
  conda install numpy
  ```
* opencv  4.5.5.64
  ```sh
  conda install -c conda-forge opencv
  ```
* scikit-learn 1.0.2
  ```sh
  conda install scikit-learn
  ```
* torch 1.11.0
  ```sh
  conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
  ```
 * CUDA 11.3
  ```sh
  https://developer.nvidia.com/cuda-11.3.0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_network
  ```
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/EEL5840-EEE4773-Spring2022/final-project-code-and-report-metaworse.git
   ```
2. Setup (and activate) your environment according to the Dependencies stated above
3. Move the file that will be used to test the model into the same folder

### Usage

The "data_train.npy" file is needed to be manually moved to the same folder as the code. This is because the file is too large to upload to Github. After moving the file, the "Final Project - Training Data.ipynb" should run perfectly to train the model. To test the model, the data that will be used to test and the label should be moved to the same folder as the code. The test data and label should be in the ".npy" format. The test data should have the dimension of 90,000 x N. After including the test and label file in the folder, the file name in the loading data section in the "Final Project - Test.ipynb" should be changed according to the test and label file. After all the steps, run all the code in "Final Project - Test.ipynb" to acquire the accuracy and confusion matrix of the model.

### Authors

Tanapol Leelertkij - leelertkij.t@ufl.edu

Sippapas Sukpholtham - s.sukpholtham@ufl.edu

### Thank you
