"""
创建窗口
绘制蛇，苹果
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from PyQt5.QtCore import*

class SnakeGame(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.setWindowTitle("贪吃蛇游戏V1.0")
        self.resize(640,480)
        
        self.fram =GameFrame(self)
        self.setCentralWidget(self.fram)
        
class GameFrame(QFrame):
    def __init__(self,parent:QWidget)->None:
        super().__init__(parent)
        
        
if __name__ =='__main__':
    app = QApplication(sys.argv)
    game = SnakeGame()
    game.show()
    
    sys.exit(app.exec_())
    