import cv2
import numpy as np
  
image = cv2.imread("panorama23.jpg")
image = cv2.resize(image, (640,480), interpolation = cv2.INTER_AREA)  
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
  
edges = cv2.Canny(gray,50,150,apertureSize=3)
  
lines_list =[]
lines = cv2.HoughLinesP(
            edges, # Input image
            1, # Distance resolution in pixels
            np.pi/180, # Angle resolution in radians
            threshold=100, # Min number of votes for valid line
            minLineLength=5, # Min allowed length of line
            maxLineGap=10 # Max allowed gap between line for joining them
            )
  
# Iterate over points
for points in lines:
    x1,y1,x2,y2=points[0]
    cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)
    lines_list.append([(x1,y1),(x2,y2)])

    cv2.imshow("Detected Lines - Probabilistic Line Transform", image)
    cv2.waitKey(0)

cv2.imwrite('detectedLines.png',image)

cv2.release()
cv2.destroyAllWindows()
