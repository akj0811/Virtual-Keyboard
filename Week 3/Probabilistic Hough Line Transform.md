
# Probabilistic Hough Line Transform

## Goal

The aim of this code is to demonstrate the usage of the Probabilistic Hough Line Transform function of the opencv library. The function identifies the lines based on certain parametric thresholds set by the user. The code results in the display of the finite length lines obtained by applying the Probabilistic Hough Line function to the given image.

## Requisites

#### Concepts - 
* [Hough Transform Theory](https://github.com/akj0811/Virtual-Keyboard/blob/master/Week%203/Hough%20Line%20Transform%20Theory.md) (refer to the given link)

#### Functions - 
* [Probabilistic Hough Line Transform](https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/hough_lines/hough_lines.html) - `cv2.HoughLinesP(edges, resolution_of_r, resolution_of_theta, min_votes, min_length, max_gap)`

  | Argument              |    Function     |
  | -------------         | --------------- |
  | edges                 | The edges detected using Canny Edge Detector or any other techniques|
  | resolution_of_r       | The resolution of the *r* parameter of the line                     |
  | resolution_of_&theta; | The resolution of the *&theta;* parameter of the line               |
  | min_votes             | The minimum threshold on the number of votes of line to be detected |
  | min_length            | Lines shorter than this length are rejected                         |
  | max_gap               | Allowed distance between two points on a line is max_gap to link them|
  
* [Line](https://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html) (refer to the given link)
* [Trackbar](https://docs.opencv.org/3.4/da/d6a/tutorial_trackbar.html) (refer to the given link)

## Code Insights

* The image is read in the same format as the image and is then converted to Gray scale mode so that the Canny Edge Detection can applied to the image.
* Two trackbars are made to fine tune the parameteres of min_length and max_gap, so that the desired representation can be obtained.
* The image is passed to the Probabilistic Hough Line Function and the detected lines are displayed on the image itself.
* The image is then read and displayed continuously to reflect any changes that happen to the image.
* The lines are then drawn using the line function of the opencv library.

## Special Note

If carefully observed, the only difference between the codes of Hough Line Transform and Probabilistic Hough Line Transform is that of the function, the rest of the code is exactly the same. The thing is, the standard function draws the lines of inifinte length, whereas the probabilistic model draws lines of finite length. It somehow manages to draw the probable lines present on the image in terms of the terminal points of the line unlike the only *(r, &theta;)* values obtained in the standard model. So, there lies a big difference between the two models.

## Code

```python 
import cv2 as cv               
import numpy as np 

def nothing(x):				                # Dummy callback function for the Trckbar position change
	pass					        # Do nothing inside the function
img = cv.imread('sudoku.png')		                # Read the image 'sudoku.png' from the directory
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)		# Convert the image to grayscale mode.
edges = cv.Canny(gray, 50, 150, apertureSize = 3)	# Apply the Canny Edge Detection
cv.imshow('edges', edges)				# Displays the image on the 'edge' window

cv.namedWindow('image')				        # Create a named window with name 'image'

cv.createTrackbar('min', 'image', 100, 100, nothing)	# Create a trackbar with 'min' label
cv.createTrackbar('max', 'image', 10, 100, nothing)	# Create a trackbar with 'max' label

while(1):						# To display the image consistently
	cv.imshow('image', img)			        # Displays the image on the 'image' window
	k = cv.waitKey(1)				# Waits for the user to press some key
	if k == 27:					# If 'escape' key is pressed, the loop is terminated
		break
	img = cv.imread('sudoku.png')	                # The image is read into the 'img' variable

	m1 = cv.getTrackbarPos('min', 'image')		# The trackbar position of the 'min' label is obtained
	m2 = cv.getTrackbarPos('max', 'image')		# The trackbar position of the 'max' label is obtained
	lines = cv.HoughLinesP(edges, 1, np.pi/180, 100,minLineLength  = m1, maxLineGap = m2)	# The probabilistic Hough Lines Function is used.

	for line in lines:				# Iterating over the lines
		x1,y1,x2,y2 = line[0]			# The extreme co-ordinates of the line are obtained
		cv.line(img, (x1,y1), (x2,y2), (0,255,0), 2)	# The line is drawn on the image itself

cv.destroyAllWindows()				        # All the windows are destroyed and the program is terminated.
```

## References 

* [Youtube Video](https://www.youtube.com/watch?v=rVBVqVmHtfc&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=34)
* [OpenCV Doc](https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html)
