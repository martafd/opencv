import numpy as np
import cv2

x = np.uint8([233])
y = np.uint8([30])

print(cv2.add(x, y))    # 233+30= 263 => 255
print(x+y)      # 233+30= 263 % 256  =>7

#--------------------------------------------
img1 = cv2.imread('im1.jpg')
img2 = cv2.imread('im2.jpg')
dst = cv2.addWeighted(img1, 0.6, img2, 0.5, 0)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

#--------------------------------------------
img1 = cv2.imread('img.jpg')
img2 = cv2.imread('heart.jpg')

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]  # region of image

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#cv2.imshow('im', img2gray)
ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY_INV)
#cv2.imshow('mask', mask)
mask_inv = cv2.bitwise_not(mask)
#cv2.imshow('mask_inv', mask_inv)

# Now white-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
#cv2.imshow('img1_bg', img1_bg)
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2, img2, mask= mask)
#cv2.imshow('img2_fg', img2_fg)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('image', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()