
# Hough Line Transform

## Goal

The aim of this code is to demonstrate the usage of the Hough Line Transform function of the opencv library. The function identifies the lines based on **votes** threshold set by the user. The code results in the display of the infinite length lines obtained by applying the Hough Line function to the given image.

## Requisites

#### Concepts - 
* [Hough Transform Theory](https://github.com/akj0811/Virtual-Keyboard/blob/master/Week%203/Hough%20Line%20Transform%20Theory.md) (refer to the given link)
#### Functions - 
* [Hough Line Transform](https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/hough_lines/hough_lines.html) - `cv2.HoughLines(edges, resolution_of_r, resolution_of_theta, min_votes)`

  | Argument              |    Function     |
  | -------------         | --------------- |
  | edges                 | The edges detected using Canny Edge Detector or any other technique |
  | resolution_of_r       | The resolution of the *r* parameter of the line                     |
  | resolution_of_&theta; | The resolution of the *&theta;* parameter of the line               |
  | min_votes             | The minimum threshold on the number of votes of the line to be displayed|
  
* [Line](https://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html) (refer to the given link)
* [Trackbar](https://docs.opencv.org/3.4/da/d6a/tutorial_trackbar.html) (refer to the given link)

## Code Insights

* The image is read in the same format as the image and is then converted to Gray scale mode so that the Canny Edge Detection can applied to the image.
* A trackbar is created to see the effect of the threshold on the lines detected by the Hough Line Function, so that appropriate threshold can be set. 
* The image is passed to the Hough Line Function and the detected lines are displayed on the image itself.
* The image is then read and displayed continuously to reflect any changes that happen to the image.
* To draw the line, we first have to obtain the end points of the line in *(x,y)* form from the *(r, &theta;)* form so that it can be passed an argument to the line function.
* The lines are then drawn using the line function of the opencv library.

## Code

```python 
import cv2 as cv 
import numpy as np 				

def nothing(x):                                                 # A dummy callback function for the Trackbar position change
	pass                                                    # Do nothing inside the function

img = cv.imread('sudoku.png')                                   # Reading the image and storing it in the variable 'img'
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)                      # Converting the image to grayscale mode

edges = cv.Canny(gray, 50, 150, apertureSize = 3)               # Canny Edge Detection
cv.imshow('edges', edges)                                       # Display the edges obtained using the above algorithm

cv.namedWindow('image')                                         # Creating a named window 
cv.createTrackbar('threshold', 'image', 200, 300, nothing)      # Creating a Trackbar with 'threshold' label

while(1):							# To display the image consistently
	cv.imshow('image', img)					# The generated lines are displayed on the image itself
	k = cv.waitKey(1)					# Waits for the user to press a key for 1 ms.
	if k == 27:					        # If 'escape' key is pressed, the loop is terminated
		break
	img = cv.imread('sudoku.png')				# The image is read into the img variable

	thresh = cv.getTrackbarPos('threshold', 'image')	# Obtaining the value of the Trackbar
	lines = cv.HoughLines(edges, 1, np.pi/180, thresh)	# Obtaining the lines using the HoughLines Function

	for line in lines:					# Iterating over the lines obtained
		rho, theta = line[0]			        # Obtaining the r, theta of the line
		a = np.cos(theta)				# Evaluating cos theta
		b = np.sin(theta)				# Evaluating sin theta
		x0 = a*rho					# Obtaining the perpendicular distant x co-ordinate
		y0 = b*rho					# Obtaining the perpendicular distant y co-ordinate
		x1 = int(x0 + 1000*(-b))			# Specifying x co-ordinate of one end of the line 
		y1 = int(y0 + 1000*a)				# Specifying y co-ordinate of one end of the line
		x2 = int(x0 + 1000*b)				# Specifying x co-ordinate of the other end of the line
		y2 = int(y0 + 1000*(-a))			# Specifying y co-ordinate of the other end of the line
		cv.line(img, (x1,y1), (x2,y2), (0,0,255), 2)	# Drawing the line

cv.destroyAllWindows()						# Closing all the windows and terminate the program
```
## References

* [OpenCV Docs](https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html)
* [Youtube Video](https://www.youtube.com/watch?v=gbL3XKOiBvw&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=33)
