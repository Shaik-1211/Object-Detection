#Detecting face and measuring the distance between the face and camera using cvzone
import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector


cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)
    
    if faces : 
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]
        # print(pointLeft, pointRight)

        w, _ = detector.findDistance(pointLeft, pointRight)
        W = 6.3
        f = 840
        d = (W*f)/w
        cvzone.putTextRect(img, f'Depth: {int(d)}cm', 
                           (face[10][0] - 100, face[10][1] - 50),
                           scale = 2)
        cv2.rectangle(img, (face[0][0],face[0][1]), (face[2][0], face[12][1]),(0,255,0),2)
        cv2.imshow("Image", img)
        cv2.waitKey(1)