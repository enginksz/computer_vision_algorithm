import cv2
import numpy as np
import time

def find_matching_points(image1, image2):
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    global keypoints1, keypoints2, good_matches, match_time

    sift = cv2.SIFT_create()
    keypoints1, descriptors1 = sift.detectAndCompute(gray1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(gray2, None)

    bf = cv2.BFMatcher()
    start_time  = time.time()

    matches = bf.knnMatch(descriptors1, descriptors2, k=2)

    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    match_time = time.time() - start_time

    points1 = np.float32([keypoints1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    points2 = np.float32([keypoints2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    return points1, points2, len(good_matches)

satellite_image = cv2.imread('image1.png')
satellite_image = cv2.resize(satellite_image, (640, 480))
satellite_image_with_text = satellite_image.copy()

drone_image = cv2.imread('image1.png')
drone_image = cv2.resize(drone_image, (640, 480))

points1, points2, num_matches = find_matching_points(satellite_image, drone_image)

result = cv2.drawMatches(satellite_image, keypoints1, drone_image, keypoints2, good_matches, None)

# SIFT yazısını görüntüler üzerinde göstermek için koordinatları hesaplama
x = 10
y = 30

# Görüntülerin üzerine SIFT yazısı
satellite_image_with_text = cv2.putText(satellite_image_with_text, "SIFT", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
result_with_text = cv2.putText(result, "SIFT", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

print("Toplam eşleşen nokta sayısı:", num_matches)
print("Eşleşme süresi:", match_time)

cv2.imshow('Satellite Image with SIFT', satellite_image_with_text)
cv2.imshow('Image Matching', result_with_text)
cv2.imwrite('result_sift.png', result_with_text)
cv2.waitKey(0)
cv2.destroyAllWindows()
