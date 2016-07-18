import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
from Matching import *
from TextFile_Process import *
from  Color_Extraction import *
from  Wall_Coordinates import *

###################################################################################
############################ SIHINA KADALLA #######################################
###################################################################################
#####   D. M. Abheetha Ishan Rangana    /   IT 13129118     /   CDAP 2016    ######
###################################################################################

def Door_Window_Det(path):

    x = path

    # X side Window matching
    w_matching(x, 'Temp/X.png', 'Res/Result_X_window.png')
    # Y side Window matching
    w_matching(x, 'Temp/Y.png', 'Res/Result_Y_window.png')

    # Type 1
    d_matching(x, 'Temp/Door_X_01.png', 'Res/Result_X_D.png')
    # Type 2
    d_matching('Res/Result_X_D.png', 'Temp/Door_X_02.png', 'Res/Result_X_DD.png')
    # Type 3
    d_matching('Res/Result_X_DD.png', 'Temp/Door_X_03.png', 'Res/Result_X_DDD.png')
    # Type 4
    d_matching('Res/Result_X_DDD.png', 'Temp/Door_X_04.png', 'Res/Result_X_final.png')
    # Type 5
    d_matching(x, 'Temp/Door_Y_01.png', 'Res/Result_Y_D.png')
    # Type 6
    d_matching('Res/Result_Y_D.png', 'Temp/Door_Y_02.png', 'Res/Result_Y_DD.png')
    # Type 7
    d_matching('Res/Result_Y_DD.png', 'Temp/Door_Y_03.png', 'Res/Result_Y_DDD.png')
    # Type 8
    d_matching('Res/Result_Y_DDD.png', 'Temp/Door_Y_04.png', 'Res/Result_Y_final.png')



    # X door extraction
    color_filter_door('Res/Result_X_final.png','Res/X_doors.png')
    # Y door extraction
    color_filter_door('Res/Result_Y_final.png','Res/Y_doors.png')




    # X window extraction
    color_filter_window('Res/Result_X_window.png','Res/X_windows.png')
    # Y window extraction
    color_filter_window('Res/Result_Y_window.png','Res/Y_windows.png')


    # Write X doors coordinates to the file
    os.system('python a_order_coordinates_Door_X.py > Res/Coor_Res/X_Door_coordinates.txt')
    # Write Y doors coordinates to the file
    os.system('python a_order_coordinates_Door_Y.py > Res/Coor_Res/Y_Door_coordinates.txt')

    # Write X windows coordinates to the file
    os.system('python a_order_coordinates_Window_X.py > Res/Coor_Res/X_Window_coordinates.txt')
    # Write Y windows coordinates to the file
    os.system('python a_order_coordinates_Window_Y.py > Res/Coor_Res/Y_Window_coordinates.txt')

    # Copy all .txt file to main directory
    os.system('cp Res/Coor_Res/*.txt .')
    #os.system('cp Res/Coor_Res/Door_coordinates.txt .')

    #
    ProcessFile('X_Door_coordinates')
    ProcessFile('Y_Door_coordinates')
    #
    ProcessFile('X_Window_coordinates')
    ProcessFile('Y_Window_coordinates')

    Get_wall_coordinates('Plans/SS.png','final.txt')

###################################################################################


# Calling Door_Window_Det function
Door_Window_Det('Plans/SS.png')







