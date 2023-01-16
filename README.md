### Introduction
This is an application to solve sudoku using OCR.

### Architecture
The application is divided into 4 parts:
* Web API
* Mobile Application 
* OCR
* Sudoku Solver

#### Web API
The web API is a Flask application that provides a RESTful API to solve sudoku. It uses Flask-RESTful to provide the API.

#### OCR
The OCR is a Python application that uses OpenCV to extract the sudoku grid from an image. It uses Tesseract to recognize the digits in the grid.

#### Sudoku Solver
The Sudoku Solver is a Python application that uses a backtracking algorithm to solve the sudoku grid.

#### Mobile Application
The Mobile Application is an Android application that uses the OCR and the Web API to solve the sudoku, using the camera to take a picture of the sudoku grid.
