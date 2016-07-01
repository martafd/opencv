import cv2

img = cv2.imread('im1.jpg')
cv2.imshow('imageee', img)
e1 = cv2.getTickCount()
for i in range(5, 50, 2):
    img = cv2.medianBlur(img, i)
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
cv2.imshow('medianBlur', img)
print(time)

cv2.waitKey(0)
cv2.destroyAllWindows()