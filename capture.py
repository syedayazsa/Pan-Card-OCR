# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 13:38:05 2020

@author: Ayaz
"""
import cv2
import time

def countdown(t):
    while t>0:
        print(t)
        t=t-1
        time.sleep(1)
    print('Clicking!')
    
countdown(2)

video_capture = cv2.VideoCapture(0)
# Check success
if not video_capture.isOpened():
    raise Exception("Could not open video device")
# Read picture. ret === True on success
ret, frame = video_capture.read()
# Close device
video_capture.release()

import sys
from matplotlib import pyplot as plt

frameRGB = frame[:,:,::-1] # BGR => RGB
plt.imshow(frameRGB)

#Save the captured image
from PIL import Image
import numpy as np
im = Image.fromarray(frameRGB)
im.save('./pancard_pics/test.jpg')


import ocr_capture