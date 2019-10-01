import cv2

capture cv2.VideoCapture('data.avi')

while True:
    has_frame, frame = capture.read()
    if not has_frame:
        print('Fim')
        break

    cv2.imshow('frame', frame)
    key = cv2.waitKey(50)
    if key == 27:
        print('Esc')
        break

cv2.destroyAllWindows()
