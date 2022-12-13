# Description

This repository includes 3 main files
1. **train.ipynb** -- This file uses to train and validate to find the best model for recognizing 10 handwriting letters where the label of each letter as shown in the table below.

<div align="center">

| letter | label |
|:-:|:-:|
| a | 0 |
| b | 1 |
| c | 2 |
| d | 3 |
| e | 4 |
| f | 5 |
| g | 6 |
| h | 7 |
| $ | 8 |
| # | 9 | 

</div>

2. **test.ipynb** -- This file can be run to test any input data and label.
3. **Final_weights.pth** -- Weights data which was received from the training file.

# Implementation

1. Open the 'test.ipynb' file
2. At the 'Loading data' section, change the file name from 'data_train.npy' and 'labels_train.npy' to any data and labels file.
3. Hit run all cells!!


# Dependencies

- matplotlib     - 3.5.1
- numpy          - 1.21.5
- opencv         - 4.5.5.64
- scikit-learn   - 1.0.2
- torch          - 1.11.0

