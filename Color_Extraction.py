import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

def color_filter_door(source, dest):

    x = source
    y = dest

    # Extract doors
    image = cv2.imread(x)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    weaker = np.array([50,100,100])
    stronger = np.array([70,255,255])

    mask = cv2.inRange(hsv, weaker, stronger)

    cv2.imwrite(y, mask)


def color_filter_window(source, dest):

    x = source
    y = dest

    # Extract doors
    image = cv2.imread(x)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    weaker = np.array([100,0,0])
    stronger = np.array([255,255,255])

    mask = cv2.inRange(hsv, weaker, stronger)

    cv2.imwrite(y, mask)