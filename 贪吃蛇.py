import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, QTimer, QRect
from PyQt6.QtGui import QPainter, QColor, QFont

class SnakeGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 400)
        self.setStyleSheet("background-color: black;")
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)  # 新增焦点策略
        self.setFocus()  # 主动获取焦点
        
        # 游戏初始化
        self.snake = [(100, 100), (90, 100), (80, 100)]  # 蛇身坐标
        self.food = self.generate_food()
        self.direction = Qt.Key.Key_Right  # 初始方向
        self.score = 0
        self.game_over = False
        
        # 定时器（控制蛇移动速度）
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_snake)
        self.timer.start(200)  # 每200ms更新一次

    def generate_food(self):
        """随机生成食物位置"""
        return (random.randint(0, 59) * 10, random.randint(0, 39) * 10)

    def move_snake(self):
        """移动蛇并检测碰撞"""
        if self.game_over:
            return
        
        head_x, head_y = self.snake[0]
        # 根据方向计算新头部位置
        if self.direction == Qt.Key.Key_Right: head_x += 10
        elif self.direction == Qt.Key.Key_Left: head_x -= 10
        elif self.direction == Qt.Key.Key_Down: head_y += 10
        elif self.direction == Qt.Key.Key_Up: head_y -= 10
        
        new_head = (head_x, head_y)
        
        # 检测碰撞：边界或自身
        if (head_x < 0 or head_x >= 600 or 
            head_y < 0 or head_y >= 400 or 
            new_head in self.snake):
            self.game_over = True
            self.timer.stop()
            self.update()
            return
        
        self.snake.insert(0, new_head)
        
        # 检测是否吃到食物
        if new_head == self.food:
            self.score += 1
            self.food = self.generate_food()
        else:
            self.snake.pop()  # 未吃到食物则移除尾部
        
        self.update()

    def paintEvent(self, event):
        """绘制游戏画面"""
        painter = QPainter(self)
        # 绘制食物（红色方块）
        painter.setBrush(QColor(255, 0, 0))
        painter.drawRect(*self.food, 10, 10)
        
        # 绘制蛇身（绿色方块）
        painter.setBrush(QColor(0, 255, 0))
        for segment in self.snake:
            painter.drawRect(*segment, 10, 10)
        
        # 游戏结束提示
        if self.game_over:
            painter.setFont(QFont("Arial", 24))
            painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, f"Game Over! Score: {self.score}")

    def keyPressEvent(self, event):
        """处理键盘输入"""
        key = event.key()
        # 防止反向移动（例如向右时不能立即向左）
        if (key == Qt.Key.Key_Right and self.direction != Qt.Key.Key_Left) or \
           (key == Qt.Key.Key_Left and self.direction != Qt.Key.Key_Right) or \
           (key == Qt.Key.Key_Down and self.direction != Qt.Key.Key_Up) or \
           (key == Qt.Key.Key_Up and self.direction != Qt.Key.Key_Down):
            self.direction = key

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("贪吃蛇游戏")
        self.setFixedSize(600, 450)
        
        # 状态栏显示得分
        self.status_label = QLabel(f"得分: 0")
        self.statusBar().addWidget(self.status_label)
        
        # 主游戏区域
        self.game = SnakeGame()
        self.game.timer.timeout.connect(self.update_score)
        self.setCentralWidget(self.game)
    
    def update_score(self):
        """更新状态栏分数"""
        self.status_label.setText(f"得分: {self.game.score}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
