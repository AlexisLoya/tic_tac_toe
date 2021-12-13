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
        self.setWindowTitle("Tic Tac Toe")
        # Couter to keep tracking
        self.counter = 0
        self.winner_x = 0
        self.winner_o = 0

        #Grid buttons
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
        self.label_x = self.findChild(QLabel, 'label_x')
        self.label_o = self.findChild(QLabel, 'label_o')
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
        self.check()
        self.counter += 1
        
        b.setEnabled(False)


    def o_turn(self,b):
        b.setText("O")
        self.label_title.setText("X's Turn")
    
    
    def x_turn(self,b):
        b.setText("X")
        self.label_title.setText("O's Turn")
    
    def check(self):
        winner = ("X" if self.counter % 2 == 0 else 'O')
        
        #Check horizontal
        if (self.button_1.text() == self.button_4.text() == self.button_7.text() != ''):
            buttons = [self.button_1,self.button_4,self.button_7]
            self.set_winner(winner, buttons)
        
        if (self.button_2.text() == self.button_5.text() == self.button_8.text() != ''):
            buttons = [self.button_2,self.button_5,self.button_8]
            self.set_winner(winner, buttons)
        
        if (self.button_3.text() == self.button_6.text() == self.button_9.text() != ''):
            buttons = [self.button_3,self.button_6,self.button_9]
            self.set_winner(winner, buttons)
        
        #Check vertical
        if (self.button_1.text() == self.button_2.text() == self.button_3.text() != ''):
            buttons = [self.button_1,self.button_2,self.button_3]
            self.set_winner(winner, buttons)
        
        if (self.button_4.text() == self.button_5.text() == self.button_6.text() != ''):
            buttons = [self.button_4,self.button_5,self.button_6]
            self.set_winner(winner, buttons)
        
        if (self.button_7.text() == self.button_8.text() == self.button_9.text() != ''):
            buttons = [self.button_7,self.button_8,self.button_9]
            self.set_winner(winner, buttons)
        
        #Check diagonals
        if (self.button_1.text() == self.button_5.text() == self.button_9.text() != ''):
            buttons = [self.button_1,self.button_5,self.button_9]
            self.set_winner(winner, buttons)
            
        if (self.button_7.text() == self.button_5.text() == self.button_3.text() != ''):
            buttons = [self.button_7,self.button_5,self.button_3]
            self.set_winner(winner, buttons)
            
        if self.counter == 8:
            self.label_title.setText("The match ended in a draw")
    
    
    def set_winner(self, winner=None,buttons=None ):
        self.reset(won=True)
        self.label_title.setText(f"{winner}'s won")
        if winner == 'X':
            self.winner_x += 1
            self.label_x.setText(f"x: {self.winner_x}")
            for b in buttons:
                b.setStyleSheet('QPushButton {color:#f51625;}')
        else:
            self.winner_o += 1
            self.label_o.setText(f"o: {self.winner_o}")
            for b in buttons:
                b.setStyleSheet('QPushButton {color:#167af5;}')



    def reset(self, won=False):
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
            if not won:
                b.setText("") 
                b.setStyleSheet('QPushButton {color:#5e5e5e;}')
                b.setEnabled(True)
            else:
                b.setEnabled(False)
                
        if not won:
            self.label_title.setText("X's Turn")
        self.counter = 0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    UIWindow = UI()
    sys.exit(app.exec_())