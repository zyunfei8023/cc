"""
创建窗口
绘制蛇，苹果
"""


import random
import sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from PyQt5.QtCore import*

COLOR_GRAY = QColor(0, 0, 0, 50)
COLOR_BLACK = QColor(0, 0, 0)
COLOR_RED = QColor(255, 0, 0)
COLOR_GREEN = QColor(0, 255, 0)
COLOR_BLUE = QColor(0, 50, 255)

SCREEN_WIDTH,SCREEN_HEIGHT =640,480
BLOCK_SIZE =20
SCREEN_W =SCREEN_WIDTH // BLOCK_SIZE
SCREEN_H =SCREEN_HEIGHT // BLOCK_SIZE

# 构建地图网格二维数组
map = []
for x in range(0, SCREEN_W):     # 0, 1, 2, 3, 4 .. 31
    for y in range(0, SCREEN_H): # 0, 1, 2, 3 .. 23
        map.append([x, y])

DIR_UP   =  (0,-1)
DIR_DOWN =  (0,1)
DIR_LEFT =  (-1,0)
DIR_RIGHT=  (1,0)


class SnakeGame(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        #设置窗口图标
        self.setWindowIcon(QIcon("./icon.png"))
        
        self.setWindowTitle("贪吃蛇游戏V1.0")
        #self.resize(640,480)
        self.setFixedSize(SCREEN_WIDTH,SCREEN_HEIGHT)#设置固定窗口大小
        
        #创建画画板QFrame
        self.fram = GameFrame(self)
        #设置到当前窗口   
        self.setCentralWidget(self.fram)
       
# 蛇头运动方向字典
DIR_DICT = {
    Qt.Key_Right : (1, 0),
    Qt.Key_Left  : (-1,0),
    Qt.Key_Up    : (0, -1),
    Qt.Key_Down  : (0, 1)
}

# 蛇头旋转方向字典
ROTATE_DICT = {
    Qt.Key_Right : -90,
    Qt.Key_Left  : 90,
    Qt.Key_Up    : 180,
    Qt.Key_Down  : 0
}
        
class Snake:
    def __init__(self):
        self.body=[[3,2]]
        self.direction = Qt.Key_Right
        self.direction_change = None # 方向改变
        self.is_cross_enable = True
        self.score = 0
        
        self.head_img = QImage("./head-red.png").scaled(BLOCK_SIZE,BLOCK_SIZE)
        
        
        #身体生长两格
        self.grow()
        self.grow()
        
        
    def move(self):
        if self.direction_change is not None:
            self.direction = self.direction_change
            self.direction_change = None
        #获取蛇头坐标
        head_x,head_y = self.body[0]
        dir_x,dir_y = DIR_DICT[self.direction]
        #往前进方向修改坐标，添加到0号位
        new_head = [head_x+dir_x,head_y+dir_y]
        
        # ------------ 穿越
        if self.is_cross_enable:
            if new_head[0] >= SCREEN_W:
                new_head[0] = 0
            elif new_head[0] < 0:
                new_head[0] = SCREEN_W - 1
            elif new_head[1] >= SCREEN_H:
                new_head[1] = 0
            elif new_head[1] < 0:
                new_head[1] = SCREEN_H - 1
        self.body.insert(0,new_head)
        #删除蛇尾
        self.body.pop()
    
    
    def grow(self):
        #复制一份蛇尾坐标
        tail_x,tail_y = self.body[-1]
        
        self.body.append([tail_x,tail_y])
        
    def handle_event(self,event:QKeyEvent):
        # print(event.key())
        if event.key() == Qt.Key_Up and self.direction != Qt.Key_Down:
            #print("向上")
            self.direction_change = Qt.Key_Up
        elif event.key() == Qt.Key_Down and self.direction != Qt.Key_Up:
            #print("向下")
            self.direction_change = Qt.Key_Down
        elif event.key() == Qt.Key_Left and self.direction != Qt.Key_Right:
            #print("向左")
            self.direction_change = Qt.Key_Left
        elif event.key() == Qt.Key_Right and self.direction != Qt.Key_Left:
            #print("向右")
            self.direction_change = Qt.Key_Right
            
        

    def draw(self,qp:QPainter):
        
        qp.setRenderHint(QPainter.Antialiasing) # 抗锯齿
        
        qp.setPen(QColor(0, 0, 0, 0)) # 边线为透明色
        qp.setBrush(COLOR_BLUE) # Red, Green, Blue
        # 绘制蛇身
        qp.setBrush(COLOR_GREEN) # Red, Green, Blue
        for x, y in self.body[1:]:
             qp.drawRoundedRect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE, 5, 5)
       
         # 绘制蛇头 -------------------------------
        head_x, head_y = self.body[0]
        # 获取当前的方向对应的旋转角度
        angle = ROTATE_DICT[self.direction]
        # 将蛇头图片进行旋转， 得到一个新图片
        rotated_img = self.head_img.transformed(QTransform().rotate(angle))
        # 绘制图片
        qp.drawImage(head_x * BLOCK_SIZE, head_y * BLOCK_SIZE, rotated_img)

 
class Food:
    def __init__(self, snake:Snake)->None:
        
        self.pos = self.generate_food(snake)
        
    def generate_food(self, snake:Snake):
        temp_map = [node for node in map if node not in snake.body]
        
        if len(temp_map) == 0:
            return
        node  = random.choice(temp_map)
        print("生成食物：",node)
        return node
    
    def draw(self, qp: QPainter):
        qp.setBrush(COLOR_RED) # Red, Green, Blue
        qp.drawRect(self.pos[0] * BLOCK_SIZE, self.pos[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
      

class GameFrame(QFrame):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        #自动获取焦点
        self.setFocusPolicy(Qt.StrongFocus)
        
        self.bg_img = QImage("./bg.png").scaled(SCREEN_WIDTH,SCREEN_HEIGHT)

        self.is_game_success = False
        self.is_game_over = False
        
        self.timer = QTimer(self)

        
        #游戏初始化
        self.init_game()
        
        self.timer.timeout.connect(self.updata_gamme)
        self.timer.start(200)
    def init_game(self):
        #初始化蛇
        self.snake=Snake()
        self.food= Food(self.snake)    
        self.timer.setInterval(200)   
        
    def updata_gamme(self):
        #print("刷新界面：",time.time())
        if len(self.snake.body) >= len(map):
            print("游戏胜利")
            QMessageBox.information(self,"游戏胜利",f"得分：{self.snake.score}关闭窗口重启游戏")
            print("重启游戏")
            self.init_game()
            return 
        
        self.snake.move()
        head = self.snake.body[0]
        
        if head == self.food.pos:
            self.snake.score+=1
            
            self.snake.grow()
            #重新生成食物
            self.food = Food(self.snake)
            interval = max(50, 200 - self.snake.score * 20)
            self.timer.setInterval(interval)
       
        new_head_x,new_head_y = head
        if(head in self.snake.body[1:] 
           or (new_head_x >= SCREEN_W or new_head_x<0) 
           or (new_head_y>=SCREEN_H or new_head_y < 0)):
           print("游戏结束")
           QMessageBox.warning(self,"游戏结束",f"得分：{self.snake.score}关闭窗口重启游戏")
           print("重启游戏")
           self.init_game()
           return 
        
        self.update()
       
        
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.init_game()
            return
        
        self.snake.handle_event(event)
        
        
    
    def paintEvent(self,event:QPaintEvent):
        
        qp= QPainter(self)
        qp.setRenderHint(QPainter.Antialiasing, True)
        qp.drawImage(0, 0, self.bg_img)
        
        qp.setPen(COLOR_GRAY)
        # 绘制网格
        # 绘制横线  y => [0, 20, 40 ... 480] 
        # (0,  0) -> (SCREEN_WITH, 0)
        # (0, 20) -> (SCREEN_WITH,20)
        for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
            qp.drawLine(0, y, SCREEN_WIDTH, y)
        # 绘制竖线  x => [0, 20, 40 ... 620] 
        # (0,  0) -> (0, SCREEN_HEIGHT)
        # (20,0) -> (20,SCREEN_HEIGHT)
        for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
            qp.drawLine(x, 0, x, SCREEN_HEIGHT)
        
        # 绘制食物
        self.food.draw(qp)
       
        self.snake.draw(qp)
        
        # 画笔设置白色
        qp.setPen(QColor(255, 255, 255))
        # 设置字体：微软雅黑，字号16
        qp.setFont(QFont("微软雅黑", 16))
        # 左上角绘制得分
        qp.drawText(10, 20, f"得分：{self.snake.score}")
        # 右上角绘制帧率  200ms -> 1000ms / 200ms = 5帧/s
        qp.drawText(SCREEN_WIDTH - 120, 20, "帧率：{:.1f}".format(1000 / self.timer.interval()))
        
        
        
if __name__ =='__main__':
    app = QApplication(sys.argv)
    
    game = SnakeGame()
    game.show()
    
    sys.exit(app.exec_())
    