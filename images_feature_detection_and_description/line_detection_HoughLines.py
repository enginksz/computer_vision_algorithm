import cv2
import numpy as np


img = cv2.imread("panorama23.jpg")
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
cv2.imshow('image_path', img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
edges = cv2.resize(edges, (0, 0), fx=0.5, fy=0.5)
cv2.imshow('Edges', edges)

cv2.waitKey(0)

lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

for line in lines:

    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)

    x0 = a * rho
    y0 = b * rho

    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))

    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow('Image with detected lines', img)
cv2.waitKey(0)
cv2.imwrite('lines_detected.jpg', img)

cv2.destroyAllWindows()


