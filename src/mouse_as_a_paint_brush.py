import cv2
import numpy as np

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

#-----------------------------------
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (90,50), 40, (300, 0, 0), 2)

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while (1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()

#----------------------------------
drawing = False # true, if mouse is pressed
mode = True # if True, draw rectangle. press 'm' to toogle a curve
ix, iy = -1, -1

img = np.zeros((512, 512, 3), np.uint8)

def draw_circle(event, x, y, flags, param):
    global drawing, mode, ix, iy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)
            else:
                cv2.circle(img, (ix, iy), 40, (255, 0, 0), 1)
    elif event == cv2.EVENT_MBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)
        else:
            cv2.circle(img, (ix, iy), 40, (255, 0, 0), 1)

cv2.namedWindow('image1')
cv2.setMouseCallback('image1', draw_circle)

while True:
    cv2.imshow('image1', img)
    k = cv2.waitKey(0) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k ==27:
        break

cv2.destroyAllWindows()
