import sys
import cv2 as cv
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QDialog, QPushButton, QVBoxLayout, QLabel, QWidget, QFileDialog
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets

# Define separate classes for each screen/dialog
class Screen0(QDialog):
    def __init__(self):
        super(Screen0, self).__init__()
        loadUi("screen0.ui", self)
        self.pushButton1.clicked.connect(self.gotoScreen1)
        self.pushButton2.clicked.connect(self.gotoScreen2)
        self.pushButton3.clicked.connect(self.gotoScreen3)

    def gotoScreen1(self):
        screen1 = Screen1()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoScreen2(self):
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() + 2)

    def gotoScreen3(self):
        screen3 = Screen3()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex() + 3)

class Screen1(QDialog):
    def __init__(self):
        super(Screen1, self).__init__()
        loadUi("screen1_fix.ui", self)
        self.pushButton1.clicked.connect(self.gotoScreen2)
        self.pushButton2.clicked.connect(self.gotoScreen3)

    def gotoScreen2(self):
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoScreen3(self):
        screen3 = Screen3()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex() + 2)

class Screen2(QDialog):
    def __init__(self):
        super(Screen2, self).__init__()
        loadUi("screen2.ui", self)
        self.pushButton1.clicked.connect(self.gotoScreen3)
        self.pushButton2.clicked.connect(self.gotoScreen1)

    def gotoScreen1(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def gotoScreen3(self):
        screen3 = Screen3()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Screen3(QDialog):
    def __init__(self):
        super(Screen3, self).__init__()
        loadUi("screen3.ui", self)
        self.pushButton1.clicked.connect(self.gotoScreen1)
        self.pushButton2.clicked.connect(self.gotoScreen2)

    def gotoScreen1(self):
        widget.setCurrentIndex(widget.currentIndex() - 2)

    def gotoScreen2(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

class ImageFileDialogExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel(self)
        layout.addWidget(self.label)

        open_button = QPushButton('Open Image', self)
        open_button.clicked.connect(self.open_image)
        layout.addWidget(open_button)

        save_button = QPushButton('Save Image', self)
        save_button.clicked.connect(self.save_image)
        layout.addWidget(save_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open Image File", "", "Images (*.png *.jpg *.bmp *.gif);;All Files (*)", options=options
        )

        if file_name:
            pixmap = QPixmap(file_name)
            self.label.setPixmap(pixmap)

    def save_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save Image File", "", "Images (*.png *.jpg *.bmp *.gif);;All Files (*)", options=options
        )

        if file_name:
            pixmap = self.label.pixmap()
            if pixmap:
                pixmap.save(file_name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    mainwindow = Screen0()
    widget.addWidget(mainwindow)
    widget.setFixedHeight(720)
    widget.setFixedWidth(720)
    widget.show()

    try:
        sys.exit(app.exec_())
    except:
        print("Exit")
