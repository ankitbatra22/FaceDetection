import cv2

img = cv2.imread("Resources/IMG_3019.jpg")

originalDimensions = img.shape
print('Original Dimensions : ', originalDimensions)

if img.shape[0] >= 4000:
    scale_percent = 10
elif img.shape[0] >= 3000:
    scale_percent = 20
elif img.shape[0] >= 1000:
    scale_percent = 60
else:
    scale_percent = 100

width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)

dim = (width, height)

resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = resized

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)


cv2.imshow('Detected Face: ', resized)
print('Resized Dimensions : ', img.shape)

cv2.waitKey()
cv2.destroyAllWindows()








