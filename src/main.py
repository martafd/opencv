import numpy as np
import cv2
import matplotlib.pyplot as plt

#-------------------------------first lesson
# img = cv2.imread('img.jpg', 0)
#
# #imread_color = 1
# #imread_greyscale = 0
# #imread_unchanged = -1
#
# cv2.imshow('image', img)
# k = cv2.waitKey(0) & 0xFF
# if k == 27:   #wait for ESC key to exit
#     cv2.destroyAllWindows()
# elif k == ord('s'):     #wait for "s" key to save and exit
#     cv2.imwrite('graycat.png',img)
#     cv2.destroyAllWindows()
#
#
# imag = cv2.imread('car.jpg', 0)
# cv2.namedWindow('imag', cv2.WINDOW_NORMAL)
# cv2.imshow('imag', imag)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# plt.imshow(img, interpolation='bicubic')
# plt.xticks([]), plt.yticks([])      #hiding the scale of x and y values
# plt.plot([60,69], [50,70], 'r', linewidth=5)
# plt.show()
#
# #-----------------comparing maatplotlib and opencv-----------------------
# img = cv2.imread('img.jpg', 1)
# b,g,r = cv2.split(img)
# img2 = cv2.merge([r,g,b])
#
# # ok for matplotlib, but wrong for opencv
# plt.subplot(121); plt.imshow(img) # expects distorted color
# plt.subplot(122); plt.imshow(img2) # expect true color
# plt.show()
#
# # ok for opencv, but wrong formatplotlib
# cv2.imshow('bgr image',img) # expects true color
# cv2.imshow('rgb image',img2) # expects distorted color
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# # -------------------------------third lesson
# # drawing functions
# img = np.zeros((512, 512, 3), np.uint8)
# cv2.line(img, (0, 0), (50, 50), (255, 0, 0), 5)
# cv2.rectangle(img, (300, 0), (500, 500), (22, 220, 0), 3)
# cv2.circle(img, (89, 89), 20, (0, 0, 255), -1)
# cv2.ellipse(img, (256, 256), (100, 50), 0, 0 , 270, 255, -1)
# pts = np.array([[30, 350], [80, 130], [120, 320], [350, 310]], np.int32)
# pts.reshape((-1, 1, 2))
# cv2.polylines(img, [pts], True, (50, 50, 50), 2)
# font = cv2.FONT_HERSHEY_COMPLEX
# cv2.putText(img, 'MartaLovesDima', (10, 500), font, 1, (200, 200, 0), 2, cv2.LINE_AA)
# cv2.imshow('ff', img)
# cv2.waitKey(0)
