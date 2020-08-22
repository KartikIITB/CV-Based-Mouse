# CV-Based-Mouse
In this project, we use the openCV and pyautogui libraries in python to create a mouse that works based on colour markers (Yellow for movement of the cursor and Green for left click).

The pipeline for the above project is as follows:

1) Image Acqusition: Video is taken frame by frame using a webcam.
2) Image Processing: We apply Gaussian Blur to the frames of the video, identify a region of interest and create ROI grid which we shall use to track the marker.
3) Colour Recognition: We convert the standard BRG image in openCV to a HSV image for improved detection -> We threshold the frame based on the marker colour.
4) Marker Identification: We first find contours of the object we are using as a marker by taking the max area contour -> We then use contour features to locate the centroid of the marker.
5) Marker Motion Tracking: We use the relative loction of the centroid of the marker w.r.t. the ROI grid.
6) Cursor Control: We move the cursor based on the above marker motion tracking and left click based on marker colour.

