# Live-Contour-Detection

This project utilizes OpenCV to detect contours of objects with a specific color in real-time video streams from your webcam. It identifies contours within a specified color range and draws them on the video feed.

## Installation
Ensure you have Python installed on your system along with the OpenCV library. You can install OpenCV using pip:

## Running
Your webcam will activate, and contours of objects with the specified color range will be detected and highlighted in real-time.

## Code Explanation
The script contour_detection.py performs the following steps:

-Initializes the webcam capture. <br>
-Reads each frame from the webcam feed and applies Gaussian blur to reduce noise. <br>
-Converts the blurred frame to the HSV color space. <br>
-Defines the lower and upper bounds of the color range to detect contours. <br>
-Creates a mask based on the specified color range. <br>
-Finds contours within the mask. <br>
-Draws contours on the original frame. <br>
-Displays the modified frame with detected contours and a mask showing the specified color range. <br>
