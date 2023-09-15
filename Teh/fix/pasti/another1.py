import cv2 as cv
import threading

class CameraApp:
    def __init__(self):
        self.cap = cv.VideoCapture(0)
        self.configure_camera()

    def configure_camera(self):
        self.set_resolution()
        self.set_auto_exposure(False)
        self.set_auto_wb(False)

    def set_resolution(self):
        height = int(input("Frame height: "))
        width = int(input("Frame width: "))
        self.cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)
        self.cap.set(cv.CAP_PROP_FRAME_WIDTH, width)

    def set_auto_exposure(self, enable):
        self.cap.set(cv.CAP_PROP_AUTO_EXPOSURE, 1 if enable else 0)

    def set_auto_wb(self, enable):
        self.cap.set(cv.CAP_PROP_AUTO_WB, 1 if enable else 0)

    def capture_image(self, frame):
        img_name = input("Image name: ")
        extention = input("Extension: ")
        cv.imwrite(f"{img_name}.{extention}", frame)
        print(f"Image {img_name}.{extention} has been created")

    def run(self):
        cv.namedWindow("webcam")
        
        while self.cap.isOpened():
            grab, frame = self.cap.read()
            
            if not grab:
                print("Capture failed")
                break
            
            cv.imshow("webcam", frame)
            key = cv.waitKey(3)
            
            if key == 27:  # 27 = escape key
                print("Escape button pressed. Exiting program!")
                break
            
            elif key == 32:  # 32 = spacebar
                print("Spacebar key pressed. Entering image data collection")
                t1 = threading.Thread(target=self.capture_image, args=(frame,))
                t1.start()

        self.cap.release()
        cv.destroyAllWindows()

if __name__ == "__main__":
    app = CameraApp()
    app.run()
