### Task 3 consists: 

    Aim: To create a neural network model of the highest accuracy, with the least number of parameters
    
    
    process: 
             -Load the dataset from a given folder 
             -Create all the image pre-processing steps 
             -Create a Neural network model using Keras and train the model on the training dataset
             -Test the model on the test dataset
             
             
### Library used: 

    1. Keras 
    2. Tensorboard 
    3. Numpy 
    4. OpenCv
    5. Pandas
    4. Matplotlib 
    5. Os 
    
    
### Output: 
    
    1. Trained the model with:

        -3 Convolution layers
        -3 Maxpooling layers
        -1 Flatten layer
        -1 Hidden layer 
        -1 Output layer
            
  ![Screenshot 2022-02-26 at 3 13 54 AM](https://user-images.githubusercontent.com/63935255/155831889-6f0a64f2-9bda-4f2e-bb5b-ae17458086ba.png)

    With Total 108,802 parameters and 5 epochs : 
              
        - Accuracy = 76.38%
        - Val_Accuracy = 73.25%
        
        
        
![Screenshot 2022-02-26 at 3 13 43 AM](https://user-images.githubusercontent.com/63935255/155832023-74f09cd7-056c-477f-bc9b-e6db93518d15.png)
![Screenshot 2022-02-26 at 3 24 19 AM](https://user-images.githubusercontent.com/63935255/155832070-3dbcd881-ba9b-4e11-8e2a-b267dcffedd9.png)


        2. Trained same model with:

        -3 Convolution layers
        -3 Maxpooling layers 
        -1 Flatten layer
        -2 Hidden layers.    -added one extra hidden layer-
        -1 Output layer
        
![Screenshot 2022-02-26 at 2 58 41 AM](https://user-images.githubusercontent.com/63935255/155832240-0200114c-c243-4c2c-875f-a8238978436d.png)

    With Total 125,314 parameters and 5 epochs : 
              
        - Accuracy = 75.39%
        - Val_Accuracy = 72.25
![Screenshot 2022-02-26 at 2 58 29 AM](https://user-images.githubusercontent.com/63935255/155832277-ed5c23c4-6b4c-49f5-81f6-04cdc16914f2.png)
![Screenshot 2022-02-26 at 3 08 49 AM](https://user-images.githubusercontent.com/63935255/155832287-e8918a49-772e-4cae-a54c-8b084a50e5c2.png)


## Summary 

    a. The Model that trained with 108,802 parameters achieved 76.38% Accuracy
    
    b. The same Model trained with 125,314 parameters achieved 75.39% Accuracy




                                      

