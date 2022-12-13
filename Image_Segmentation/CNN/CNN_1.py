"""
Author @Sippapas Sukpholtham
Master's Student in Mechanical and Aerospace Engineering
University of Florida
Dec, 2022

"""

import torch.nn as nn

# CNN for model1.pth

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Sequential(         # input shape (1, 28, 28)
            nn.Conv2d(
                in_channels=1,              # input height
                out_channels=32,            # n_filters
                kernel_size=3,              # filter size
                stride=1,                   # filter movement/step
                padding=2,                  # padding
            ),                              
            nn.BatchNorm2d(32),             # normalization the data
            nn.ReLU(),                      # activation function
            nn.MaxPool2d(kernel_size=2),    # choose max value in 2x2 area
            nn.Dropout2d(p=0.3)             # drop out 10% of data
        )
        self.conv2 = nn.Sequential(         
            nn.Conv2d(32, 64, 3, 1, 2),     
            nn.BatchNorm2d(64),
            nn.ReLU(),                      
            nn.MaxPool2d(2),                
            nn.Dropout2d(p=0.3)
        )
        self.conv3 = nn.Sequential(         
            nn.Conv2d(64, 128, 3, 1, 2),    
            nn.BatchNorm2d(128),
            nn.ReLU(),                      
            nn.MaxPool2d(2),
            nn.Dropout2d(p=0.3)
        )
        self.conv4 = nn.Sequential(         
            nn.Conv2d(128, 128, 3, 1, 2),     
            nn.BatchNorm2d(128),
            nn.ReLU(),                      
            nn.MaxPool2d(2),                
            nn.Dropout2d(p=0.3)
        )
        # self.conv5 = nn.Sequential(         
        #     nn.Conv2d(64, 64, 3, 1, 2),     
        #     nn.BatchNorm2d(64),
        #     nn.ReLU(),                      
        #     nn.MaxPool2d(2),                
        #     nn.Dropout2d(p=0.1),
        # )

        self.out1 = nn.Sequential(nn.Linear(1152, 1000), 
                                 nn.ReLU(),
                                 nn.Dropout(p=0.3))
        self.out2 = nn.Sequential(nn.Linear(1000 , 500),  
                                 nn.ReLU(),
                                 nn.Dropout(p=0.3))
        self.out3 = nn.Sequential(nn.Linear(500 , 17))  # last fully connected layer,  output 17 classes

    def forward(self, x):
        # Convolutional layers
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        # x = self.conv5(x)
        x = x.view(x.size(0), -1)  # flatten the output of conv2 to (BATCH_SIZE, 64 * 3 * 3)
        # Linear layers          
        output = self.out1(x)
        output = self.out2(output)
        output = self.out3(output)
        return output, x