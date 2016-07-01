import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # b, r, g = cv2.split(frame)
    # frame = cv2.merge([r, b, g])
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGRA)
    if ret:
        print('imshow next')
        cv2.imshow('frame', frame)
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
