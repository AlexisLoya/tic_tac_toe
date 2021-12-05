from PyQt5.QtWidgets import QPushButton


class CustomButton(QPushButton):
    def __init__(self):
        QPushButton.__init__(self)
        self.isX = False
        self.isO = False