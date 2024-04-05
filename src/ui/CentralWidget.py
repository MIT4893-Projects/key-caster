from PyQt5.QtWidgets import QWidget, QVBoxLayout

from ui.KeyDisplayer import KeyDisplayer
from ui.ModKeyDisplayer import ModKeyDisplayer


class CentralWidget(QWidget):
    def __init__(self, parent, key_dis, mod_dis):
        super().__init__(parent)

        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.layout.addWidget(key_dis)
        self.layout.addWidget(mod_dis)
