#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 22:40:20 2022

@author: rahul
"""

import cv2
import os 
import glob

def task(file_path):
    
    img_file = []
    for path in file_path:
        img_file.append(path)
    
    split_text = []
    for text in img_file :
        
        split_text.append(os.path.splitext(text))   #splits the text into file_name and file_extension seperately
        
    gray_images = []
    image_format = []
    images = []
    
    for i in range(len(img_file)):
        if(split_text[i][1] != ".xml"):  #here excluding the .xml file
         gray_images.append(cv2.cvtColor(cv2.imread(img_file[i]), cv2.COLOR_BGR2GRAY))
         images.append(img_file[i])
        
         
    for i in range(len(gray_images)):
        image_format.append(type(gray_images[i]))
        
    
         
    
    #creating a new folder for gray_scale images
    folder_name = 'grayScale_images'
    folder = os.path.join(os.getcwd(), folder_name)    
    
    
   #creating a new folder to store all grayscale images
    os.mkdir(folder_name) 
    for i in range(len(gray_images)):
     cv2.imwrite(f"{folder}/{i}.png", gray_images[i])
    
    
   
    
    cv2.imshow("original_image", cv2.imread(images[1]))
    cv2.imshow("output = grayscale_image", gray_images[1])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
    return len(img_file), image_format
    



if __name__ == '__main__':
      
    file_path = glob.glob("image_dataset/*")
        
    image_count, image_format =  task(file_path)
    
    print(f"There are total {image_count} images \nThe variable type of grayscale image is : {image_format[1]}")
    
    
    