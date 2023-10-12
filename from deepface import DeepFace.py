from deepface import DeepFace
import cv2 

#DeepFace.stream(db_path="C:/Users/merta/Desktop/erdogan",source=0,model_name='Facenet512')
#,model_name='VGG-Face'
#DeepFace.analyze(img_path="C:/Users/merta/Desktop/erdogan/erdogan.jpg")
i=0




while True:


    vid_cam = cv2.VideoCapture(0)
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


    results,image_frame = vid_cam.read()
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

            # Crop the image frame into rectangle
            cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
            


            image_frame=image_frame[y:y+h,x:x+w]
            # Increment sample face image
            

            # Save the captured image into the datasets folder
        

            # Display the video frame, with bounded rectangle on the person's face
            cv2.imshow('frame', image_frame)
            cv2.waitKey(3000)
            

            cv2.destroyAllWindows
        
        



    result = DeepFace.verify(img1_path = "C:/Users/merta/Desktop/erdogan/mert1.jpg", 
            img2_path = image_frame, 
            model_name = "VGG-Face",
            enforce_detection=False
            
            
        )
    print (result['verified'])
    
    


    if 0xFF == ord('q'):
        break