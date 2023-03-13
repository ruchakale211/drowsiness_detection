# drowsiness_detection

The goal of this project is to create a simulation of a system for sleepiness detection. The project's main goal is to create a system that can recognise tiredness in a driver by observing their closed eyes. In order to prevent car accidents, it is thought that by keeping an eye on the condition of the eyes, one might identify the first signs of drowsiness in a driver. The procedure of identifying tiredness in drivers involves observing their eye movements, both open and closed.

MODULAR DIVISION: 

Face Detection:
This module uses video input from the camera to try to identify faces. Face detection is accomplished mostly using the Frontal face cascade classifier of the Haar classifiers. The face is recognised as a rectangle and then transformed to a grayscale image, which is then saved in memory and used to train the model.


Eye Detection:
We must concentrate on the eyes to detect drowsiness since the model builds a drowsiness detection system. The Haar Cascade Eye Classifier, a haar classifier, is used to identify the eyeballs from the video input. Rectangular formats are used to detect eyeballs.


Face Tracking:
In order to detect faces, this module uses visual input from the camera. Most often, the Frontal face cascade classifier of the Haar classifiers is used for face detection. The face is identified as a rectangle, converted to grayscale, and saved in memory before being used to train the model.

Eye Tracking:
We must concentrate on the eyes to detect drowsiness since the model builds a drowsiness detection system. The Haar Cascade Eye Classifier, a haar classifier, is used to identify the eyeballs from the video input. Rectangular formats are used to detect eyeballs.


Drowsiness detection: 
The frequency is calculated in the module before, and if it remains at 0 for a long period, the system warns the driver of the danger of drowsiness. detection of distractions The face tracking module continuously monitors the driver's face for any repetitive movements or extended periods of unbroken eye contact that could be perceived as a lack of driver focus and set off a distraction alarm by the system.

