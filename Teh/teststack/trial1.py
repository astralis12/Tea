import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap

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

    #def open_image(self):
     #   options = QFileDialog.Options()
      #  file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.bmp *.gif);;All Files (*)", options=options)
    
  #  def open_image(self):
   #     options = QFileDialog.Options()
    #    file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "", options=options)


     #   if file_name:
      #      pixmap = QPixmap(file_name)
       #     self.label.setPixmap(pixmap)

    #def save_image(self):
     #   options = QFileDialog.Options()
      #  file_name, _ = QFileDialog.getSaveFileName(self, "Save Image File", "", "Images (*.png *.jpg *.bmp *.gif);;All Files (*)", options=options)
      
    def openImage(self):
    options = QFileDialog.Options()
    options |= QFileDialog.ReadOnly
    file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.bmp);;All Files (*)", options=options)
    if file_name:
        #image = cv2.imread(file_name)
        pixmap = QPixmap(file_name)
        self.label.setPixmap(pixmap)
        # Resize image if necessary
        # Display the image on QLabel

def save_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image File", "","" ,options=options)
    

        if file_name:
            pixmap = self.label.pixmap()
            if pixmap:
                pixmap.save(file_name)

app = QApplication(sys.argv)
example = openImage()
example.setWindowTitle("Image File Dialog Example")
example.setGeometry(100, 100, 600, 400)
example.show()
sys.exit(app.exec_())
