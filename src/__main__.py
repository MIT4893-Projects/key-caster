#!/usr/bin/python3

import sys
import threading
import keyboard

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget

from ui.CentralWidget import CentralWidget
from ui.KeyDisplayer import KeyDisplayer
from ui.ModKeyDisplayer import ModKeyDisplayer


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setStyleSheet("background-color: rgba(0, 0, 0, 40%)")
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint
            | QtCore.Qt.FramelessWindowHint
            | QtCore.Qt.X11BypassWindowManagerHint,
        )

        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight,
                QtCore.Qt.AlignCenter,
                QtCore.QSize(220, 100),
                QtWidgets.qApp.desktop().availableGeometry(),
            )
        )

        self.key_dis = KeyDisplayer(self)
        self.mod_dis = ModKeyDisplayer(self)
        self.central_widget = CentralWidget(self, self.key_dis, self.mod_dis)
        self.setCentralWidget(self.central_widget)

        self.worker = Worker(self.key_dis, self.mod_dis)
        self.worker.start()

    def location_on_the_screen(self):
        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()

        widget = self.geometry()
        x = ag.width() - widget.width() - 50
        y = 2 * ag.height() - sg.height() - widget.height() - 80
        self.move(x, y)


class Worker(QThread):
    finished = pyqtSignal()

    def __init__(self, key_dis, mod_dis):
        QThread.__init__(self)
        self.key_dis = key_dis
        self.mod_dis = mod_dis

    def run(self):
        while True:
            last = keyboard.KeyboardEvent(event_type=keyboard.KEY_UP, scan_code=0)
            while True:
                e = keyboard.read_event()
                if (
                    len(e.name) == 1
                    and e.event_type == keyboard.KEY_DOWN
                    and e.event_type != last.event_type
                ):
                    self.mod_dis.set_modifiers(e.modifiers)
                    self.key_dis.set_key(e.name)
                    print(e.name, e.modifiers)
                elif len(e.name) > 1 and e.event_type == keyboard.KEY_DOWN:
                    print("mod pressed")
                    self.mod_dis.set_modifiers((e.name,) + e.modifiers)
                elif e.event_type == keyboard.KEY_UP:
                    print("mod released", e.name)
                    self.mod_dis.reset_modifiers((e.name,))
                last = e


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MainWindow()
    mywindow.location_on_the_screen()
    mywindow.show()

    app.exec_()
