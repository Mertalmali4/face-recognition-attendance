
from retinaface import RetinaFace
import face_recognition
import cv2
import numpy as np
import os
import pickle
import xlsxwriter
import datetime



video_capture = cv2.VideoCapture(0)

x = datetime.datetime.now()

xl_name=(str(x.day)+"_"+str(x.month)+"_"+str(x.year))





file=open("data/EncodeFile.p",'rb')
encode_list_with_id=pickle.load(file)
file.close()
known_face_encodings,known_face_names=encode_list_with_id
#known_face_encodings.append(encode_list_known)

#encodings=Id_list_known[0]
#known_face_encodings = known_face_encodings.append(encode_list_known[0])

 





# Create arrays of known face encodings and their names



# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
face_known_names=[]

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    #frame=face_recognition.load_image_file("dataset/23000.jpg")

    # Only process every other frame of video to save time
    if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        
        resp = RetinaFace.detect_faces(frame, threshold = 0.3)
        facial_area_location=[]
        
        if 1==len(resp):
            for key in resp:
                identity = resp[key]
                facial_area=identity["facial_area"]
                facial_area_location.append((facial_area[3],facial_area[0], facial_area[1],facial_area[2]))
                #3012
                crop_img = frame[facial_area[1]: facial_area[3], facial_area[0]: facial_area[2]]

        else:
            crop_img=frame    

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        
        
        
        # Find all the faces and face encodings in the current frame of video
        #, facial_area_location
        face_encodings = face_recognition.face_encodings(crop_img)
        
        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            
            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                if name not in face_known_names:
                    face_known_names.append(name)

                
                

            face_names.append(name)
            
    process_this_frame = not process_this_frame

    text="Press q For Exit"
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(frame,text,(500, 470), font, 0.5, (255, 255, 255), 1)
    # Display the results
    for (top, right, bottom, left), name in zip(facial_area_location, face_names):
        '''
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        '''
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        #font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left-180, bottom-8), font, 1.0, (255, 255, 255), 1)
        
    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
i=1
workbook = xlsxwriter.Workbook(("ExcelData/"+xl_name+'.xlsx'))
worksheet = workbook.add_worksheet()

for id in face_known_names:
    row_name=('A'+str(i))
    worksheet.write(row_name,id)
    i+=1
    

workbook.close()















