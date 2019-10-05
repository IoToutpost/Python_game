from time import time

WIDTH  = 800
HEIGHT = 300

ACCELERATION = 0.005
DECELERATION = 0.0008
# 代表1M的像素数
SCALE = 75

# 在跑道上以特定距离显示图像的函数。
def displayAt(img, pos, y):
    screen.blit(img,(sprinter.x + (pos * SCALE) - (sprinter.distance * SCALE), y))

class Sprinter(Actor):
    def __init__(self, **kwargs):
        super().__init__(image='idle', pos=(200,220), **kwargs)
        self.startTime = time()
        self.finishTime = time()
        self.runFrames = ['run' + str(i) for i in range(1,16)]
        self.timeOnCurrentFrame = 0
        self.speed = 0
        self.lastPressed = None
        self.keyPressed = False
        self.distance = 0
        
    # 将运动员推进到下一帧
    def nextFrame(self):
        # 如果当前空闲，则启动正在运行的动画。 
        if self.image == 'idle':
            self.image = self.runFrames[0]
        else:
            # 在列表中找到下一个图像，然后返回到第一个图像 
            # 当列表已经到末尾的时候
            nextImageIndex = (self.runFrames.index(self.image) + 1) % len(self.runFrames)
            self.image = self.runFrames[nextImageIndex]
            
    # 检查左右方向键是否正确
    # 被交替按下
    def isNextKeyPressed(self):
        if keyboard.left and self.lastPressed is not 'left' and not keyboard.right:
            self.lastPressed = 'left'
            return True
        if keyboard.right and self.lastPressed is not 'right' and not keyboard.left:
            self.lastPressed = 'right'
            return True
        return False
        
    def update(self):
        # 更新短跑运动员的速度
        # 交替按键加速
        if self.isNextKeyPressed() and self.distance < 100:
            self.speed = min(self.speed + ACCELERATION, 0.15)
        # 如果没有按键，减速
        else:
            self.speed = max(0, self.speed-DECELERATION)
        # 根据短跑运动员的速度更新距离 
        self.distance += self.speed
        # 根据短跑运动员的速度对其进行动画 
        self.timeOnCurrentFrame += 1
        if self.speed > 0 and self.timeOnCurrentFrame > 10 - (self.speed * 75):
            self.timeOnCurrentFrame = 0
            self.nextFrame()
        # 如果不移动，则设置为空闲
        if self.speed <= 0:
            self.image = 'idle'


#--------

sprinter = Sprinter()

def update():
    # move and animate the sprinter
    sprinter.update()
    # add to the finish time if race is still in progress
    if sprinter.distance < 100:
        sprinter.finishTime = time()

def draw():
    screen.clear()
    # draw the track
    screen.blit('track', (0,0))
    # draw distance markers and finish line
    displayAt('25m', 25, 200)
    displayAt('50m', 50, 200)
    displayAt('75m', 75, 200)
    displayAt('finishline', 100, 230)
    # draw the sprinter
    sprinter.draw()
    # draw the current distance and time
    screen.draw.text('Distance(m): ' + str(int(min(100, sprinter.distance))), (20, 20), fontsize=32, color="white")
    screen.draw.text('Time(s): ' + str(round(sprinter.finishTime - sprinter.startTime, 2)), (250, 20), fontsize=32, color="white")
