import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QIcon
from widget import Ui_Widget


class MyApp(QWidget):
    def __init__(self):
        app.setWindowIcon(QIcon("acs.ico"))
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # Üst paneli kaldır
        self.oldPos = None  # Fare konumunu saklamak için değişken

        # Kapatma butonu (❌)
        self.close_button = QPushButton("❌", self)
        self.close_button.setGeometry(self.width() - 40, 0, 30, 30)  # Sağ üst köşe
        self.close_button.clicked.connect(self.close)

        # Küçültme butonu (➖)
        self.minimize_button = QPushButton("➖", self)
        self.minimize_button.setGeometry(self.width() - 80, 0, 30, 30)  # Kapatmanın soluna
        self.minimize_button.clicked.connect(self.showMinimized)

        

        # Butonların arkaplanını saydam yap
#        for btn in (self.close_button, self.minimize_button):
#            btn.setStyleSheet(
#                "background: transparent; font-size: 16px; border: none;"
#               "color: white; padding: 5px;"
#            )

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.oldPos is not None:
            delta = event.globalPosition().toPoint() - self.oldPos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self.oldPos = None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("acs.ico"))
    window = MyApp()
    window.show()
    sys.exit(app.exec())
