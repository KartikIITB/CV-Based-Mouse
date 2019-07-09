import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

cam = cv.VideoCapture(0)

lower_orange = np.array([10,130,150])
upper_orange = np.array([50,255,255])

while(True):
    ret, frame =cam.read()
    frame = cv.flip(frame, 1)

    w = frame.shape[1]
    h = frame.shape[0]
    
    img_smooth = cv.GaussianBlur(frame, (7,7), 0)

    #Define a region of interest
    mask = np.zeros_like(frame)

    mask[50:350, 50:350] = [255, 255, 255]

    img_roi = cv.bitwise_and(img_smooth, mask)
    cv.rectangle(frame, (50,50), (350,350), (0,0,255), 2)
    cv.line(frame, (150,50), (150,350), (0,0,255), 2)
    cv.line(frame, (250,50), (250,350), (0,0,255), 1)
    cv.line(frame, (50,150), (350,150), (0,0,255), 1)
    cv.line(frame, (50,250), (350,250), (0,0,255), 1)
    

    #Threshold the image for orange
    img_hsv = cv.cvtColor(img_roi, cv.COLOR_BGR2HSV)
    img_threshold = cv.inRange(img_hsv, lower_orange, upper_orange)

    contours, hierarchy = cv.findContours(img_threshold, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    
    if(len(contours) != 0):
        areas = [cv.contourArea(c) for c in contours]
        max_index = np.argmax(areas)
        cnt = contours[max_index]
##        x_bound, y_bound, w_bound, h_bound = cv.boundingRect(cnt)
##        cv.rectangle(frame, (x_bound, y_bound), (x_bound + w_bound, y_bound + h_bound), (255, 0, 0), 2)

        M = cv.moments(cnt)
        if(M['m00']) != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv.circle(frame, (cx,cy), 4, (0,255,0), -1)

            if cx is range(150, 250):
                if cy < 150:
                    print('Upper Middle')
                elif cy > 250:
                    print('Lower Middle')
                else:
                    print('Centre')

            if cy is range(150, 250):
                if cx < 150:
                     print('Left Middle')
                elif cx > 250:
                    print('Right Middle')
                else:
                    print('Centre')

            
    
    if ret == True:
        cv.imshow('Frame', frame)
    else:
        break
    key = cv.waitKey(100)
    if key == 27:
        break

##img_RGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
##plt.imshow(img_RGB)
##plt.show()

cam.release()
cv.destroyAllWindows()
