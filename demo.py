import cv2
import mysql.connector
import numpy as np
video=cv2.VideoCapture(0)
facedetect=cv2.CascadeClassifier('c:/Users/HP/Downloads/haarcascade_frontalface_default.xml')

faces_data=[]
  
i=0      

name=input("Enter Your Name: ")

while True:
    ret,frame=video.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=facedetect.detectMultiScale(gray, 1.3 ,5)
    for (x,y,w,h) in faces:
        crop_img=frame[y:y+h, x:x+w, :]
        resized_img=cv2.resize(crop_img, (50,50))
        if len(faces_data)<=100 and i%10==0:
            faces_data.append(resized_img)
        i=i+1
        cv2.putText(frame, str(len(faces_data)), (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255), 1)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (50,50,255), 1)
    cv2.imshow("Frame",frame)
    k=cv2.waitKey(1)
    if k==ord('q') or len(faces_data)==100:
        break
video.release()
cv2.destroyAllWindows()
# save face to pickle file  
def insertOrupdate(id, name, age):
    conn= mysql.connector.connect(
          host="localhost",
          user ="root",
          password="Ajay123@ ",
          database="college"

    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM STUDENT WHERE ID= %s", (id))
    isRecordExist=cursor.fetchone()

    if isRecordExist:
        cursor.execute("UPDATE STUDENT SET NAME=%s WHERE id = %s",(name,id))
        cursor.execute("UPDATE STUDENT SET age=%s WHERE id = %s",(age,id))
    else:
        cursor.execute("INSERT INTO STUDENT (id, name, age) VALUES(%s,%s,%s)",(id,name,age))

    conn.commit()
    cursor.close()
    conn.close()
