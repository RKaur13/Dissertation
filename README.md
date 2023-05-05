# Dissertation
This repository contains the code that was used to test the smart wearable designed for object detection.

The repository contains the following files both object detection using sensors and object detection using computer vision techniques:

Object detection using sensors:

ultrasonic_sensor.ino : contains the code that was used to measure the distance using the ultrasonic sensor and communicate these distances to the user through the use of four vibration motors

Object detection using computer vision technqiues:

Whilst Google Colab was used to train the machine learning model, the following files were used to deploy the machine learning model onto the Raspberry Pi 4:

requirements.txt: Contains all the necessary libraries detect.py: Main script that enables the initialisation and continous running of the model utils.py: Enables bounding boxes to be shown, counts the number of identified objects and enables text-to-speech formatting using the gtts library

model_edgetpu.tflite: Trained machine learning tflite model file
