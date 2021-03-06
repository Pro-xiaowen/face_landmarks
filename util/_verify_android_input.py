'''Simple test code to check the integrity of the input buffer of Android app.
Data in input buffer is dumped from the Android app and reconstructed as image for integrity check.

>> problem solved! no need to use this code
'''

import cv2
import numpy as np

FILE = '/Users/gglee/Develop/tensorflow/tensorflow/lite/examples/android/buff_00.txt'

with open(FILE, 'r') as rf:
    for l in rf.readlines():
        data = map(lambda x: int(float(x)*128.0+128.0), l.split())

        reshaped = np.asarray(data, dtype=np.uint8).reshape((56, 56, 3))
        print(reshaped)
        cv2.imshow('reshaped', reshaped)

        cv2.waitKey(-1)