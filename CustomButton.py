from PyQt5.QtWidgets import QPushButton


class CustomButton(QPushButton):
    def __init__(self, Text, parent = None):
        super(CustomButton, self).__init__()
        self.isX = False
        self.isO = False
        self.setupbt(Text)

    def setupbt(self, Text):
        self.setFlat(True)
        self.setText(Text)
        self.setGeometry(200,100, 60, 35)
        self.move(300,300)
        print('chegu aqui')
        self.setToolTip('Isso muito maneiro <b>Artur</b>')
        self.show()
