"""
创建窗口
绘制蛇，苹果
"""


import random
import sys
import time
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent, QPaintEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from PyQt5.QtCore import*

COLOR_BLACK = QColor(0,0,0)
COLOR_RED = QColor(255,0,0)
COLOR_GREEN = QColor(0,255,0)

SCREEN_WIDTH,SCREEN_HEIGHT =640,480
BLOCK_SIZE =20
SCREEN_W =SCREEN_WIDTH // BLOCK_SIZE
SCREEN_H =SCREEN_HEIGHT // BLOCK_SIZE



DIR_UP = (0,-1)
DIR_DOWN=(0,1)
DIR_LEFT=(-1,0)
DIR_RIGHT=(1,0)


class SnakeGame(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        
        self.setWindowTitle("贪吃蛇游戏V1.0")
        #self.resize(640,480)
        self.setFixedSize(640,480)
        self.fram =GameFrame(self)
        
        self.setCentralWidget(self.fram)
        
class GameFrame(QFrame):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        
        self.setFocusPolicy(Qt.StrongFocus)
        
        self.snake=[[5,10],[4,10],[3,10]]
        self.food = self.generate_food()
        
        self.direction = DIR_RIGHT
        self.score= 0
        
        
        
        
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updata_gamme)
        self.timer.start(200)
        
    def generate_food(self):
        
        while True:
            food = [random.randint(0,31),random.randint(0,23)]
            if food not in self.snake:
                return food
    
        
    def updata_gamme(self):
        #print("刷新界面：",time.time())
        
        head_x,head_y = self.snake[0]
        dir_x,dir_y = self.direction
        
        new_head = [head_x+dir_x,head_y+dir_y]
        
        self.snake.insert(0,new_head)
        
        if new_head == self.food:
            self.score+=1
            self.food = self.generate_food()
        else:
            self.snake.pop()
            
        
        self.update()
        
    def keyPressEvent(self, event: QKeyEvent):
        # print(event.key())
        if event.key() == Qt.Key_Up and self.direction !=DIR_DOWN:
            # print("向上")
            self.direction = DIR_UP
        elif event.key() == Qt.Key_Down and self.direction != DIR_UP:
            # print("向下")
            self.direction = DIR_DOWN
        elif event.key() == Qt.Key_Left and self.direction != DIR_RIGHT:
            # print("向左")
            self.direction = DIR_LEFT
        elif event.key() == Qt.Key_Right and self.direction != DIR_LEFT:
            # print("向右")
            self.direction = DIR_RIGHT
        
    
    def paintEvent(self,event:QPaintEvent):
        
        painter= QPainter(self)
        
        
        painter.setBrush(QBrush(COLOR_BLACK))
        painter.drawRect(self.rect())
        
        # 绘制食物
        painter.setBrush(QBrush(COLOR_RED)) # Red, Green, Blue
        painter.drawRect(self.food[0] * BLOCK_SIZE, self.food[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        # 绘制蛇
        painter.setBrush(QBrush(COLOR_GREEN)) # Red, Green, Blue
        for x, y in self.snake:
            painter.drawRect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        
        
if __name__ =='__main__':
    app = QApplication(sys.argv)
    
    game = SnakeGame()
    game.show()
    
    sys.exit(app.exec_())
    