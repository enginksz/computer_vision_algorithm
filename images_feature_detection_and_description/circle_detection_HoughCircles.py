import cv2
import numpy as np
  
img = cv2.imread("panorama23.jpg")
img = cv2.resize(img, (640,480))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
gray_blurred = cv2.blur(gray, (3, 3))
  
# Apply Hough transform on the blurred image.
detected_circles = cv2.HoughCircles(gray_blurred, 
                   cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
               param2 = 30, minRadius = 1, maxRadius = 40)
  
if detected_circles is not None:
  
    detected_circles = np.uint16(np.around(detected_circles))
  
    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        print("r: ", r)
        cv2.circle(img, (a, b), r, (0, 255, 0), 2)
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
        cv2.imshow("Detected Circle", img)
        cv2.imwrite('detectedCircle.png',img)
        cv2.waitKey(0)
else:
    print("No circle detected")

cv2.release()
cv2.destroyAllWindows()
