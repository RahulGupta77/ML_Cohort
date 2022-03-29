## Custom Object detection 
##
 #### Aim : 
     To train a custom object detection model using Tensorflow object detection API.
##
     
     
#### Dataset : 
  [Drive link](https://drive.google.com/drive/folders/1TiN2qCCmbhxrbV4JPNGGkzP0TA_850tb)
  
  
 ##   

#### Process : 
    1. Data annotation and cleaning : 
            a. Split the datasets into train and test data.
            b. Using LabelImg library, I individually annotated the data. The annotated data was saved in .xml file which consists the co-ordinates of region of intrests. 
            c. The .xml files in both train and test dataset was further converted into .csv files. 
            d. Generated .tfrecords files using .csv files for each image in  train and test datasets. 

    2. Pre-trained model selection : 
            a. ssd_mobilenet_v1_coco model was used due to it's good accuracy compared to other models. 

    3. Configuring .pbtxt and .config file : 
            a. Generated a .pbtxt file which consists types of classes. In this case "scratch", "dent" and "replacement" was used. 
            b. Configured .config file. path to training data, evaluation data, number of classes, batch size, number of steps were configured to initiate the training process.

    4. Training the model : 
           a. Trained the model using : 
                                a. batch size = 24
                                b. num_step = 25k
                                c. number of hrs trained = 2:30 hrs 
                                d. loss of saved model = 1.3% 
                                e. The model was trained on Google Colab for accessing the better resource like GPU. 
                                

##

#### Libraries used : 
        1. Tensorflow 
        2. LabelImg 
        3. Numpy 
        4. OS
        5. Matplotlib
        6. Tensorboard 
        
##

#### Model Used :
     ssd_mobilenet_v1_coco model
     
##

     
#### Trained model checkpoints :
[Drive link](https://drive.google.com/drive/folders/1MxEWFkkWBDDOnzLF9MNhqcu468yAx5hW?usp=sharing)


## 

#### Output: 

      1. Loss evaluation on Tensorboard : 
      
![Screenshot 2022-03-28 at 11 31 03 PM](https://user-images.githubusercontent.com/63935255/160678820-28555d32-4309-458a-b038-359c6dad820f.png)

      2. Testing images : 
![image1](https://user-images.githubusercontent.com/63935255/160679738-039e8662-e8ac-49d9-8ead-0c7ea993058f.jpg)
![image2](https://user-images.githubusercontent.com/63935255/160679744-69218b8e-914f-4397-a71d-a60424e7bb85.jpg)
![image3](https://user-images.githubusercontent.com/63935255/160679749-6f3a499f-effb-4428-9613-31a6d1fe6023.jpg)
![image4](https://user-images.githubusercontent.com/63935255/160679751-e2c96b04-4dbf-4b5c-93fd-f7d7b753ff49.jpg)


      3. Preditions made by the model : 
![detection_output0](https://user-images.githubusercontent.com/63935255/160679470-4c0de306-1726-43ae-8977-235bba199e2e.png)
![detection_output1](https://user-images.githubusercontent.com/63935255/160679488-9ef160b6-eead-4cbb-aba2-7b3d303642ce.png)
![detection_output2](https://user-images.githubusercontent.com/63935255/160679500-6848ba24-0a73-4f82-8a21-2bc88c7f18db.png)
![detection_output3](https://user-images.githubusercontent.com/63935255/160679513-96709135-d349-46f4-ba09-b261df37cb87.png)


## 

### Summary : 
      Successfully trained a custom object detection model which is working with a high confidence on a given image 






