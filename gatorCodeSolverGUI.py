"""
Author @Ninad Bhagwat
Master's Student in Mechanical and Aerospace Engineering
University of Florida
Dec, 2022

"""

# Import Packages

from PyQt5.QtWidgets import *
import sys
import os
from sympy import symbols, Eq, solve, sympify
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pyqtgraph as pg
from Image_Segmentation.data_segmentation import clear_and_segment
from Image_Segmentation.imgTOstring import img2string


class Window(QWidget):
    '''
    The Window class inherits from the QWidget class.
    The __init__ method is a constructor method
    The super method returns the parent object of the Window class and we call 
    its constructor.

    The Window Class has following methods - 
    1) InitWindow: To display a GUI window
    2) getImage: It opens the file manager to find the image file
    3) getEquation: This method sends the selected image to the OpenCV, CNN and 
                    OCR code to get the string output.
    4) getResult: This methods calculates result from the provided string and 
                  plots the graph                 
    '''

    def __init__(self):
        super().__init__()

        self.title = "Gator Equation Solver"
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        self.InitWindow()

        self.fname = ''

    def InitWindow(self):
        self.setWindowTitle(self.title)

        vbox = QVBoxLayout()

        # Setting up the Gator Solver Icon

        self.gatorLabel = QLabel("")
        self.gatorLabel.setAlignment(Qt.AlignCenter)
        pixmapg = QPixmap(os.path.join(
            os.getcwd(), "Florida_Gators_gator_logo.svg.png")).scaledToHeight(75)
        self.gatorLabel.setPixmap(QPixmap(pixmapg))
        vbox.addWidget(self.gatorLabel)

        # Printing out the Greeting

        self.greeting = QLabel("Welcome to Gator Solver")
        self.greeting.setFont(QFont('Times', 15))
        self.greeting.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.greeting)

        # Creating 'Upload Image' Button

        self.uploadButton = QPushButton("Upload Image")
        self.uploadButton.setFont(QFont('Times', 10))
        self.uploadButton.setStyleSheet("background-color: orange")
        self.uploadButton.clicked.connect(self.getImage)
        vbox.addWidget(self.uploadButton)

        # Alignment for the image display

        self.imageLabel = QLabel("")
        self.imageLabel.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.imageLabel)

        # Creating 'Get Equation' Button

        self.equationButton = QPushButton("Get Equation")
        self.equationButton.setFont(QFont('Times', 10))
        self.equationButton.setStyleSheet("background-color: cyan")
        self.equationButton.clicked.connect(self.getEquation)
        vbox.addWidget(self.equationButton)

        # alignment for the equation display

        self.equationLabel = QLabel("")
        self.equationLabel.setFont(QFont('Times', 10))
        self.equationLabel.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.equationLabel)

        # User input for 'a' values

        self.aValueLabel = QLabel("Enter the space separated values for a:")
        self.aValueLabel.setFont(QFont('Times', 10))
        vbox.addWidget(self.aValueLabel)

        vbox.addWidget(self.aValueLabel)
        self.aLabel = QLineEdit("")
        self.aLabel.setFont(QFont('Times', 10))
        self.aLabel.setText('')
        vbox.addWidget(self.aLabel)

        # Creating 'Get Result' Button

        self.resultButton = QPushButton("Get Result")
        self.resultButton.setFont(QFont('Times', 10))
        self.resultButton.setStyleSheet("background-color: green")
        self.resultButton.clicked.connect(self.getResult)
        vbox.addWidget(self.resultButton)

        self.resultLabel = QLabel("")
        self.resultLabel.setFont(QFont('Times', 10))
        self.resultLabel.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.resultLabel)

        # Creating the Plot

        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.graphWidget)

        self.setLayout(vbox)
        self.showMaximized()

    # Image selection dialogue box

    def getImage(self):
        self.fname = QFileDialog.getOpenFileName(
            self, "Open File", "/home", "Images (*.png *.xpm *.jpg)")
        imagePath = self.fname[0]
        pixmap = QPixmap(imagePath).scaledToHeight(75)
        self.imageLabel.setPixmap(QPixmap(pixmap))

    # Equation from OCR

    def getEquation(self):

        # clear the old segmented images from the 'segmented' folder

        clear_and_segment(self.fname[0])
        ocrResult = img2string('Image_Segmentation/segmented')
        self.equationLabel.setText("Equation :" + f"{ocrResult}")

    # Calculation and plotting graphs

    def getResult(self):

        # clear the old segmented images from the folder and add the new ones

        clear_and_segment(self.fname[0])
        ocrResult = img2string('Image_Segmentation/segmented')

        # Equation Solver

        aValues = self.aLabel.text()
        print(aValues)
        a, b = symbols("a b")
        arrayString = aValues.split(" ")
        array = []
        for strA in arrayString:
            array.append(float(strA))

        splitList = ocrResult.split('=')
        lhs = (sympify(splitList[0], evaluate=False))
        rhs = (sympify(splitList[1], evaluate=False))
        expr = Eq(lhs, rhs)
        sol = solve(expr, b)
        resultList = []
        for value in array:
            result = sol[0].subs(a, value)
            resultList.append(round(float(result), 2))
        print(resultList)
        self.resultLabel.setText("b values =" + f"{resultList}")

        # Creating and Stylizing the plot

        self.graphWidget.setTitle(
            "<span style=\"color:blue;font-size:20pt\">Gator Solver Plot</span>")
        self.graphWidget.setLabel(
            'left', "<span style=\"color:red;font-size:20px\">b Values</span>")
        self.graphWidget.setLabel(
            'bottom', "<span style=\"color:red;font-size:20px\">a Values</span>")
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.plot(array, resultList, pen=pg.mkPen(
            color=(0, 0, 254), width=5), symbol='o', symbolBrush=('r'), symbolSize=20)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
