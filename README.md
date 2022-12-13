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
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#authors">Authors</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This report is part of the final project in the

<!-- GETTING STARTED -->
## Getting Started

In this section all libraries, packages and other dependencies that need to be installed are listed along with the instruction on how to recreate the project locally. 

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/tensip/OCR_equation_solver.git
   ```
   
2. Setup (and activate) your environment
   ```sh
   conda env create -f environment.yml
   ```

### Usage

Follow the instructions to run the project:

1) Open the gatorCodeSolverGUI.py file in an editor.

2) Run the code. A separate GUI window will open.

3) In the GUI window, click the "Upload Image" button. This will open the file manager. Go to the "OCR_equation_solver\Test Images" folder.

4) Open an image file between "test_1" and "test_2". This will provide a small preview of the image in the GUI.

5) In the GUI window, click the "Get Equation" button. This will return and show the string format of the equation in the image.

6) Since we are working only on "Two variables linear equations", we need to provide values for one of the variables. Provide the values for the variable using "space separation". Also, **this program only recognizes variables "a" and "b"**.
   Example - put "1 2 3 4 5 45 67" for the values "1, 2, 3, 4, 5, 45, 67" etc.
   
7) In the GUI window, click the "Get Result" button. This will return the values for the other variable and will also plot a graph of the two variable values. You can zoom in, zoom out and pan the plot for your convenience.

8) Once done or during any step in the process, you can go back and select another equation.

9) Close the GUI window to stop the program.

10) You can also upload your own equation image and get the results.

### Authors

Sippapas Sukpholtham - s.sukpholtham@ufl.edu

Ninad Bhagwat - n.bhagwat@ufl.edu

Soham Bombale - s.bombale@ufl.edu

### Thank you
