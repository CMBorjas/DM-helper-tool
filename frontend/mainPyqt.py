import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap

class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dungeon Master Map")
        self.setGeometry(100, 100, 800, 600)

        # Label to display the map
        self.map_label = QLabel(self)
        self.map_label.setGeometry(100, 50, 600, 400)

        # Button to load map
        self.load_map()

    def load_map(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Map", "", "Image Files (*.png *.jpg)")
        if file_path:
            pixmap = QPixmap(file_path)
            pixmap = pixmap.scaled(600, 400)
            self.map_label.setPixmap(pixmap)

# Initialize the application
app = QApplication(sys.argv)
window = MapWindow()
window.show()
sys.exit(app.exec_())
