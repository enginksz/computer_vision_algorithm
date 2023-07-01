import cv2

PATH = "../../videos/ocean.mp4"
class ORBMatcher:
    def __init__(self):
        self.orb = cv2.ORB_create()
        self.bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        self.prev_frame = None
        self.prev_gray = None
        self.prev_kp = None
        self.prev_des = None
        self.match_count = 0

    def calculate_matches(self, prev_frame, frame):
        gray1 = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
        kp1, des1 = self.orb.detectAndCompute(gray1, None)

        gray2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        kp2, des2 = self.orb.detectAndCompute(gray2, None)

        matches = self.bf.match(des1, des2)

        return len(matches)


    def process_frame(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        kp, des = self.orb.detectAndCompute(gray, None)

        if self.prev_frame is not None:
            matches = self.bf.match(self.prev_des, des)
            matches = sorted(matches, key=lambda x: x.distance)
            self.match_count = matcher.calculate_matches(self.prev_frame, frame)

            
            result = cv2.drawMatches(self.prev_frame, self.prev_kp, frame, kp, matches[:10], None, flags=2)
            cv2.imshow("ORB Matches", result)
            if cv2.waitKey(1) == ord('q'):
                return False

        self.prev_frame = frame
        self.prev_gray = gray
        self.prev_kp = kp
        self.prev_des = des

        return True

    def process_video(self, video_path):
        cap = cv2.VideoCapture(video_path)
        
        if not cap.isOpened():
            print("Video dosyası yüklenemedi.")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            if not self.process_frame(frame):
                break
        print("Toplam eşleşen nokta sayısı:", self.match_count)       
        cap.release()
        cv2.destroyAllWindows()

        

# Kullanım örneği
matcher = ORBMatcher()
matcher.process_video(PATH)