import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()

        # 初始化UI
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('PyQt5 示例')
        self.setGeometry(100, 100, 300, 200)

        # 创建一个垂直布局
        layout = QVBoxLayout()

        # 创建一个标签
        self.label = QLabel('Hello, PyQt5!', self)
        layout.addWidget(self.label)

        # 创建一个按钮
        self.button = QPushButton('点击我', self)
        self.button.clicked.connect(self.onButtonClick)
        layout.addWidget(self.button)

        # 设置窗口的布局
        self.setLayout(layout)

    def onButtonClick(self):
        # 当按钮被点击时更新标签文本
        self.label.setText('按钮已点击')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimpleApp()
    ex.show()
    sys.exit(app.exec_())