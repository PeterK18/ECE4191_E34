#camera calibration

import numpy as np
import cv2

def calculate_distance(imageball)
    fx=800
    fy=800 #will be found through camera calibration
    cx=320
    cy=240
    realball=0.067 #diameter in real tennis ball in meters

    imageball=800 #diameter of image of tennis ball in pixels

    intrinsic_camera=np.array([[fx, 0, cx],[0, fy, cy], [0, 0, 1]])

    K=intrinsic_camera[0,0] #assumes square pixels, may be further transformations

    distance = (K * realball) / imageball
return distance
