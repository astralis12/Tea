import sys
import cv2 as cv
import threading
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QFileDialog

class CameraApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Camera App')
        self.setGeometry(100, 100, 640, 480)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

        self.start_button = QPushButton('Start Camera', self)
        self.start_button.clicked.connect(self.startCamera)
        self.layout.addWidget(self.start_button)

        self.capture_button = QPushButton('Capture Image', self)
        self.capture_button.clicked.connect(self.captureImage)
        self.layout.addWidget(self.capture_button)

        self.central_widget.setLayout(self.layout)

        self.capture = cv.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateFrame)

    def startCamera(self):
        if not self.timer.isActive():
            self.capture.open(0)
            self.timer.start(20)  # Update the frame every 20 milliseconds

    def captureImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save Image', '', 'Image Files (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)', options=options)

        if file_name:
            _, frame = self.capture.read()
            cv.imwrite(file_name, frame)
            print(f"Image {file_name} has been created")

    def updateFrame(self):
        ret, frame = self.capture.read()
        if ret:
            # Convert the frame to RGB format for PyQt
            rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            h, w, ch = rgb_frame.shape
            bytes_per_line = ch * w
            image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            self.image_label.setPixmap(pixmap)

    def closeEvent(self, event):
        if self.capture.isOpened():
            self.capture.release()
        self.timer.stop()
        super().closeEvent(event)

def main():
    app = QApplication(sys.argv)
    window = CameraApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
