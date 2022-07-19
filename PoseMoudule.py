import cv2
import mediapipe as mp
import time


class PostDetector():
    def __init__(self, mode=False, model=1, sl=True,
                 eg=False, ss=True, detectionCon=0.5,
                 trackCon=0.5):

        self.mode = mode,
        self.model = model,
        self.sl = sl,
        self.eg = eg,
        self.ss = ss,
        self.detectionCon = detectionCon,
        self. trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose()  # different

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # imgRGB = img
        self.results = self.pose.process(imgRGB)
        # if draw:
        #     if results.pose_landmarks:
        #         self.mpDraw.draw_landmarks(img, results.pose_landmarks,
        #                                    self.mpPose.POSE_CONNECTIONS)
        # why use this method??
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)

        return img

    def findPosition(self, img, draw=True):
        lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, lm)
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
                # if draw:
                #     cv2.circle(img, (lmList[0][1], lmList[0][2]), 4, (0,0,255), cv2.FILLED)
                    # cv2.circle(img, (cx, cy), 1, (0,255,0), cv2.FILLED)
        return lmList

def main():
    # cap = cv2.VdieoCapture(0)
    cap = cv2.VideoCapture("video/1.mp4")
    pTime = 0
    detecor = PostDetector()

    while True:
        _, img = cap.read()
        img = detecor.findPose(img) # ,False
        lmList = detecor.findPosition(img)
        print(lmList[0])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

        cv2.imshow("video", img)
        cv2.waitKey(10)




if __name__ == "__main__":
    main()