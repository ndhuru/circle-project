import time

import cv2

# Load the image
image = cv2.imread('Screenshot 2024-01-25 at 8.16.11 AM.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# gaussian blur
blurred = cv2.GaussianBlur(gray, (9, 9), 2)
# canny edge to line detect
edges = cv2.Canny(blurred, 30, 150)
# contour for circle detection get detected here
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# usually onscreen if we have a topdown image of a sodacan I had set it
# so that it would display the largest contour, that way I can just
# only display the soda can image
# reminder: in a topdown image of a soda can,
# the rim of the soda can is usually the circle with the largest contour
contours = sorted(contours, key=cv2.contourArea, reverse=True)
largest_contour = contours[0]

# fit to the largest contour
center, radius = cv2.minEnclosingCircle(largest_contour)
center = tuple(map(int, center))

# this line actually is the one that draws the circle
cv2.circle(image, center, int(radius), (0, 255, 0), 2)

# center dot detection
cv2.circle(image, center, 5, (0, 0, 255), -1)

# the display goes here
cv2.imshow('Circumference Detection', image)
cv2.waitKey(0)
time.sleep(10)
cv2.destroyAllWindows()
