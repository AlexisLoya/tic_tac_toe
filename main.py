import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from PyQt5.QtGui import QCursor
# Build Initial App
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        
        # Load the ui file
        uic.loadUi('tic_tac_toe.ui', self)
        
        # Define the widgets
        
        # Couter to keep track of who's turn it is
        self.counter = 0
        
        #Grid
        self.button_1 = self.findChild(QPushButton, 'button_1')
        self.button_2 = self.findChild(QPushButton, 'button_2')
        self.button_3 = self.findChild(QPushButton, 'button_3')
        self.button_4 = self.findChild(QPushButton, 'button_4')
        self.button_5 = self.findChild(QPushButton, 'button_5')
        self.button_6 = self.findChild(QPushButton, 'button_6')
        self.button_7 = self.findChild(QPushButton, 'button_7')
        self.button_8 = self.findChild(QPushButton, 'button_8')
        self.button_9 = self.findChild(QPushButton, 'button_9')
        
        # UI
        self.button_start = self.findChild(QPushButton, 'button_start')
        self.label_x = self.findChild(QLabel, 'label_X')
        self.label_o = self.findChild(QLabel, 'label_O')
        self.label_title = self.findChild(QLabel, 'label_title')
        
        # Click the button
        self.button_1.clicked.connect(lambda: self.clicker(self.button_1))
        self.button_2.clicked.connect(lambda: self.clicker(self.button_2))
        self.button_3.clicked.connect(lambda: self.clicker(self.button_3))
        self.button_4.clicked.connect(lambda: self.clicker(self.button_4))
        self.button_5.clicked.connect(lambda: self.clicker(self.button_5))
        self.button_6.clicked.connect(lambda: self.clicker(self.button_6))
        self.button_7.clicked.connect(lambda: self.clicker(self.button_7))
        self.button_8.clicked.connect(lambda: self.clicker(self.button_8))
        self.button_9.clicked.connect(lambda: self.clicker(self.button_9))
        self.button_start.clicked.connect(self.reset)
        
        # Show the app
        self.show()
    
    # Methods
    
    def clicker(self, b):
        if self.counter % 2 == 0:
            self.x_turn(b)
        else:
            self.o_turn(b)
        
        self.counter += 1
        
        b.setEnabled(False)


    def o_turn(self,b):
        b.setText("O")
        self.label_title.setText("X's Turn")
    
    
    def x_turn(self,b):
        b.setText("X")
        self.label_title.setText("O's Turn")
    
    
    def reset(self):
        button_list = [
            self.button_1,
            self.button_2,
            self.button_3,
            self.button_4,
            self.button_5,
            self.button_6,
            self.button_7,
            self.button_8,
            self.button_9,
        ]
        
        for b in button_list:
            b.setText("")
            b.setEnabled(True)
        self.counter += 1
        self.label_title.setText("X's Turn")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    UIWindow = UI()
    sys.exit(app.exec_())