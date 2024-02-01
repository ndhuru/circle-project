import cv2
import time

# Load the video
cap = cv2.VideoCapture('IMG_3470.MOV')

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # gaussian blur
        blurred = cv2.GaussianBlur(gray, (9, 9), 2)
        # canny edge to line detect
        edges = cv2.Canny(blurred, 30, 150)
        # contour for circle detection get detected here
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # sort the contours
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        largest_contour = contours[0]

        # fit to the largest contour
        center, radius = cv2.minEnclosingCircle(largest_contour)
        center = tuple(map(int, center))

        # this line actually is the one that draws the circle
        cv2.circle(frame, center, int(radius), (0, 255, 0), 2)

        # center dot detection
        cv2.circle(frame, center, 5, (0, 0, 255), -1)

        # the display goes here
        cv2.imshow('Circumference Detection', frame)

        # Break the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
