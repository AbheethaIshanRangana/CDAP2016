import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

###################################################################################
############################ SIHINA KADALLA #######################################
###################################################################################
#####   D. M. Abheetha Ishan Rangana    /   IT 13129118     /   CDAP 2016    ######
###################################################################################

def w_matching(source, temp, destination):      # Window Matching Function

    x = source
    y = temp
    z = destination

    img_rgb = cv2.imread(x)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    template = cv2.imread(y,0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (255,0,0), 1)

    cv2.imwrite(z,img_rgb)

###################################################################################

def d_matching(source, temp, destination):      # Door Matching Function

    x = source
    y = temp
    z = destination

    img_rgb = cv2.imread(x)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    template = cv2.imread(y,0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 1)

    cv2.imwrite(z,img_rgb)

###################################################################################