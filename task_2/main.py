#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 10:07:04 2022

@author: rahul
"""

import cv2 
import os
import pandas as pd 


def label_img(folder_name, csv_file):
    
    
    labels = csv_file
    
    #extracting coordinates and image file name from the csv file
    minx = labels["xmin"].tolist()
    miny = labels["ymin"].tolist()
    maxx = labels["xmax"].tolist()
    maxy = labels["ymax"].tolist()
    img_name = labels["name"].tolist()
    
    
    
    #extracting each image path and reading each image
    img_path = []
    image = []
    for img in img_name:
      img_path.append(os.path.join(folder_name,str(img)))

    for i in range(0,len(img_path)):
        if i == 0:
            image.append(None)
        else:  
            image.append(cv2.imread(img_path[i]))
            

            
    #bounding rectangles in the image using the co=ordinates given and labelling them        
    bounding_img = []
    labelled_img = []

    for i in range(len(image)):
        if i == 0:
            bounding_img.append(None)
            labelled_img.append(None)
        else:
            bounding_img.append(cv2.rectangle(image[i], (int(minx[i]),int(miny[i])), (int(maxx[i]),int(maxy[i])), color = (255,255,255), thickness =2))
            labelled_img.append(cv2.putText(bounding_img[i], "Cat",(int(minx[i]-50), int(miny[i]+50)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0),2))



    # #creating a new folder to store all labelled images
    # os.mkdir("output_images") 
    # for i in range(1,len(image)):
    #   cv2.imwrite(f"output_images/{i}.png", labelled_img[i])
    
    return None
    

      

if __name__ == '__main__':
      
    file_name = "cat/"
    
    csv_file = pd.read_csv("data_labels.csv")
    
    label_img(file_name, csv_file)
    