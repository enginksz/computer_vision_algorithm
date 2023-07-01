import cv2
import numpy as np

image = cv2.imread("panorama23.jpg")
image = cv2.resize(image, (640,480))  

  
operatedImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
operatedImage = np.float32(operatedImage)       # convert the grayscale image to float32
  
dest = cv2.cornerHarris(operatedImage, 2, 5, 0.07)
dest = cv2.dilate(dest, None)
image[dest > 0.01 * dest.max()]=[0, 0, 255]
cv2.imshow('Image with Borders', image)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

cv2.imwrite('detectedCorners.png',image)


    

