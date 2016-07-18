import cv2
import numpy as np
import matplotlib.pyplot as plt

def Get_wall_coordinates(source, dest):

    x = source;
    y = dest;

# *******************************Image Processing for identifying corners in the image**********************************
    image = cv2.imread(x)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, 2, 3, 0.04)
    image[dst > 0.01 * dst.max()] = [0, 0, 255]

    cv2.imwrite('coordinateImage.jpg', image)

# *******************************Getting the pixel values of the detected corners***************************************
    getCoord = np.where(np.all(image == (0, 0, 255), axis=-1))
    coordinates = zip(getCoord[0], getCoord[1])
    x = np.array(coordinates, dtype="int")
    print ("Coordinates : ")
    print (x)

# ******************************* Generating the text file *************************************************************
    filename1 = open(y, "w")
    filename1.write(str(coordinates))
    filename1.close()

    #plt.scatter(getCoord[0], getCoord[1])
    #plt.show()