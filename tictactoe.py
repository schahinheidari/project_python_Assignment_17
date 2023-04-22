from functools import partial
import random
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('tictactoc.ui', None)
        self.ui.show()
        self.game = [[self.ui.btn1,self.ui.btn2,self.ui.btn3],
                     [self.ui.btn4,self.ui.btn5,self.ui.btn6],
                     [self.ui.btn7,self.ui.btn8,self.ui.btn9]]

        #self.ui.rBtn1Player.clicked.connect()
        #self.ui.rBtn2Player.clicked
        self.ui.btnRestart.clicked.connect(self.restart)
        self.playerX_score = 0
        self.playerO_score = 0
        self.total_games = 0

        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet('coloer: Black; background-color: skyblue')
                self.game[i][j].clicked.connect(partial(self.play, i, j))

        self.counter = 0
        self.player = 'X'

    def play(self, i, j):
        #print(i, j)
        #if self.counter % 2 == 0:
        #    self.game[i][j].setText('X')
        #else:
       #     self.game[i][j].setText('O')
        #self.counter += 1
        if self.game[i][j].text() == '':
            if self.player == 'X':
                self.game[i][j].setText('X')
                self.game[i][j].setStyleSheet('color: green; background-color: lightgreen')
                self.game[i][j].setStyleSheet("border :3px solid blue;"
                                   "border-top-left-radius :35px;"
                                   " border-top-right-radius : 20px; "
                                   "border-bottom-left-radius : 50px; "
                                   "border-bottom-right-radius : 10px")
                self.player = 'O'
            else:
                self.game[i][j].setText('O')
                self.game[i][j].setStyleSheet('color: red; border: 3px solid blue; border-top-left-radius: 35px; background-color: pink')
                self.player = 'X'

        self.check()

    def onePlayer(self, i, j):
        row = random.randrange()
    
    def check(self):
        if self.game[0][0].text() == 'X' and self.game[0][1].text() == 'X' and self.game[0][2].text() == 'X':
            msgBox = QMessageBox()
            msgBox.setText('player 1 wins! ')
            msgBox.exec_()
            self.playerX_score.setText(self.playerX_score.toString())
    
    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        else:
            return False
    

    def restart(self):
        self.player = 'X'
        self.counter = 0
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
                self.game[i][j].clicked.connect(partial(self.play, i, j))
                self.game[i][j].setStyleSheet('coloer: Black; background-color: skyblue')
                self.game[i][j].setEnabled(True)



app = QApplication([])
window = TicTacToe()

app.exec_()


