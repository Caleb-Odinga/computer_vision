import cv2 
#load the cascade
eye_cascade =cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')
#Read the input image 
path=r'/home/caleb/Desktop/cale backup/shakii/mn.jpg'
img=cv2.imread(path)
#convert into grayscale 
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#detect faces
eyes=eye_cascade.detectMultiScale(img,scaleFactor =2, minNeighbors=4)
print("found {0} eyes".format(len(eyes)))
#Draw rectangle around the face 
for(x,y,w,h) in eyes:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)
#Display the image
cv2.imshow('HERE ARE EYES',img)
cv2.waitKey(0)