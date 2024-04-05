from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt


class KeyDisplayer(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("color: white; font-size: 30px; background: none;")
        self.setText("key")

    def set_key(self, key=""):
        print("key")
        if len(key) > 1 or len(key) == 0:
            return
        curr_text = self.text()
        if len(curr_text) > 4:
            curr_text = curr_text[-4:]
        self.setText(curr_text + key)
        # self.setText(key)
