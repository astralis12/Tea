import sys
import cv2 as cv
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget ,QApplication, QInputDialog, QLineEdit,QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
import threading 
import time
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap
import sys
import cv2 as cv
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QDialog, QPushButton, QVBoxLayout, QLabel, QWidget, QFileDialog
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets

def resolutionSetting(cap): # resolution setting function
    height = int(input("frame height: "))
    width = int(input("frame width: "))
    
    cap.set(cv.CAP_PROP_FRAME_HEIGHT,height)
    cap.set(cv.CAP_PROP_FRAME_WIDTH,width)

    

class Screen0(QDialog):
    def __init__(self):
        super(Screen0, self).__init__()
        loadUi("mode.ui", self)
       # self.pushButton1.clicked.connect(self.gotoScreen1)
       # self.pushButton2.clicked.connect(self.gotoScreen2)
        #self.pushButton3.clicked.connect(self.gotoScreen3)

    #def gotoScreen1(self):
        screen1 = Screen1()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    #def gotoScreen2(self):
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() + 2)

    #def gotoScreen3(self):
        screen3 = Screen3()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex() + 3)



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



