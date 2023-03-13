import face_recognition
import cv2
import time
from scipy.spatial import distance as dist
from threading import Thread
import numpy as np


MIN_AER = 0.30  
EYE_AR_CONSEC_FRAMES = 10   
COUNTER = 0 


def eye_aspect_ratio(eye):
 # compute the euclidean distances between the two sets of
 # vertical eye landmarks (x, y)-coordinates
 A = dist.euclidean(eye[1], eye[5])
 B = dist.euclidean(eye[2], eye[4])

 # compute the euclidean distance between the horizontal
 # eye landmark (x, y)-coordinates
 C = dist.euclidean(eye[0], eye[3])

 # compute the eye aspect ratio
 ear = (A + B) / (2.0 * C)

 # return the eye aspect ratio
 return ear


 
def main():
    global COUNTER
    video_capture = cv2.VideoCapture(0)
    while True:       
        ret, frame = video_capture.read(0)   


        # get the correct face landmarks
        
        face_landmarks_list = face_recognition.face_landmarks(frame) #face recognition module to get face landmarks like eyes,nose,etc..

            # get eyes
        for face_landmark in face_landmarks_list:
                        leftEye = face_landmark['left_eye']
                        rightEye = face_landmark['right_eye']
                        #eye aspect ratio for left and right eyes
                        leftEAR = eye_aspect_ratio(leftEye)
                        rightEAR = eye_aspect_ratio(rightEye)
                        # average the eye aspect ratio together for both eyes
                        ear = (leftEAR + rightEAR) / 2
                        #========================converting left and right eye values in numpy arrays
                        lpts = np.array(leftEye)
                        rpts = np.array(rightEye)
                        #==================showing line from left of left eye and right of right eye
                        cv2.polylines(frame, [lpts],True ,(255,255,0), 1)
                        cv2.polylines(frame, [rpts],True ,(255,255,0), 1)
                        
                        # check to see if the eye aspect ratio is below the blink
                        # threshold, and if so, increment the blink frame counter
                        if ear < MIN_AER:
                                COUNTER+= 1

                        
                                if COUNTER >= EYE_AR_CONSEC_FRAMES:
                                        
                                         # draw an alarm on the frame
                                        cv2.putText(frame, "ALERT! You are feeling asleep!", (10, 30),
                                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                        
                        else:
                                COUNTER = 0
                                

                        # draw the computed eye aspect ratio on the frame to help
                        # with debugging and setting the correct eye aspect ratio
                        # thresholds and frame counters
                        cv2.putText(frame, "EAR: {:.2f}".format(ear), (500, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
 
                        # show the frame
                        cv2.imshow("Sleep detection program.", frame)

        # if the `q` key was pressed, break from the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    # do a bit of cleanup
    video_capture.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()
        