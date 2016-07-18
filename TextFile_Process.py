import re
import os
import csv

###################################################################################
############################ SIHINA KADALLA #######################################
###################################################################################
#####   D. M. Abheetha Ishan Rangana    /   IT 13129118     /   CDAP 2016    ######
###################################################################################

# Define Function
def ProcessFile(file):

    f = file

    with open(f+'.txt','r')as fr:
        with open(f+'_I.txt','w') as fw:

            print('Files opened....')
            string = fr.read()
            new_str = re.sub('[^a-zA-Z0-9\n\.\t]', ' ', string)
            fw.write(new_str)

    with open(f+'_I.txt','r') as fr:
        x,y = [], []
        for l in fr:
            row = l.split()
            x.append(row[0])
            y.append(row[1])

    with open('final_'+f+'.txt','w') as f1:
        # adding two x values
        #for i in range(0,len(x)):
        i = 0
        while(i <= len(x)-1):
            avg_x = (int(x[i]) + int(x[i+1]))/2
            #print(avg_x)

            avg_y = (int(y[i+1]) + int(y[i+2]))/2
            #print(avg_y)

            f1.write('Object/')
            f1.write('(')
            f1.write(str(avg_x))
            f1.write(',')
            f1.write(str(avg_y))
            f1.write(')')
            f1.write('\n')
            i=i+4

# Call Function
#ProcessFile('Door_coordinates')
#ProcessFile('Window_coordinates')