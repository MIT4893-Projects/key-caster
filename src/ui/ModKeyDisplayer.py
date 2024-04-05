from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt


class ModKeyDisplayer(QWidget):
    modifier_icons = {
        "shift": "󰘶",
        "ctrl": "⌃",
        "alt": "⌥",
        "windows": "⌘",
    }

    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)

        self.modifiers = {
            key: QLabel(text=f'<font color="gray">{icon}</font>')
            for key, icon in self.modifier_icons.items()
        }

        for mod in self.modifiers.values():
            mod.setAlignment(Qt.AlignCenter)
            mod.setStyleSheet("font-size: 20px; background: none;")
            self.layout.addWidget(mod)

    def set_modifiers(self, modifiers):
        for key, icon in self.modifier_icons.items():
            self.modifiers[key].setText(f'<font color="gray">{icon}</font>')
        for mod in modifiers:
            if mod in self.modifiers:
                self.modifiers[mod].setText(
                    f'<font color="white">{self.modifier_icons[mod]}</font>'
                )

    def reset_modifiers(self, reset_modifiers):
        for mod in reset_modifiers:
            if mod in self.modifiers:
                self.modifiers[mod].setText(
                    f'<font color="gray">{self.modifier_icons[mod]}</font>'
                )
