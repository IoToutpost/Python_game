# Lunar Lander
import math
from pygame import image, Color
import time
start_time = time.time()
backgroundImage = image.load('images/background.png')
lander = Actor('lander',(50,30))
lander.angle = lander.direction = -80
lander.thrust = 0.5
gravity = 0.8
lander.burn = speedDown = gameState = gameTime = 0

def draw():
    global gameTime
    screen.blit('background',(0,0))
    screen.blit('space',(0,0))
    r = lander.angle
    if(lander.burn > 0):
        lander.image = "landerburn"
    else:
        lander.image = "lander"
    lander.angle = r
    lander.draw()
    if gameState == 0:
        gameTime = int(time.time() - start_time)
    screen.draw.text("Altitude : "+ str(getAlt()), topleft=(650, 10), owidth=0.5, ocolor=(255,0,0), color=(255,255,0) , fontsize=25)
    screen.draw.text("Time : "+ str(gameTime), topleft=(40, 10), owidth=0.5, ocolor=(255,0,0), color=(255,255,0) , fontsize=25)
    if gameState == 2:
        screen.draw.text("Congratulations \nThe Eagle Has Landed", center=(400, 50), owidth=0.5, ocolor=(255,0,0), color=(255,255,0) , fontsize=35)
    if gameState == 1:
        screen.draw.text("Crashed", center=(400, 50), owidth=0.5, ocolor=(255,0,0), color=(255,255,0) , fontsize=35)

def update():
    global gameState, speedDown
    if gameState == 0:
        if keyboard.up:
            lander.thrust = limit(lander.thrust+0.01,0,1)
            changeDirection()
            lander.burn = 1
        if keyboard.left: lander.angle += 1
        if keyboard.right: lander.angle -= 1
        oldPos = lander.center
        lander.y += gravity
        newPos = calcNewXY(lander.center, lander.thrust, math.radians(90-lander.direction))
        lander.center = newPos
        speedDown = newPos[1] - oldPos[1]
        lander.thrust = limit(lander.thrust-0.001,0,1)
        lander.burn = limit(lander.burn-0.05,0,1)     
        if speedDown < 0.2 and getAlt() == 1 and lander.angle > -5 and lander.angle < 5:
            gameState = 2
        if getAlt() == 0:
            gameState = 1

def changeDirection():
    if lander.direction > lander.angle: lander.direction -= 1
    if lander.direction < lander.angle: lander.direction += 1

def limit(n, minn, maxn):
    return max(min(maxn, n), minn)

def calcNewXY(xy,speed,ang):
    newx = xy[0] - (speed*math.cos(ang))
    newy = xy[1] - (speed*math.sin(ang))
    return newx, newy

def getAlt():
    testY = lander.y+8
    height = 0;
    while testPixel((int(lander.x),int(testY))) == Color('black') and height < 600:
        testY += 1
        height += 1
    return height

def testPixel(xy):
    if xy[0] >= 0 and xy[0] < 800 and xy[1] >= 0 and xy[1] < 600:
        return backgroundImage.get_at(xy)
    else:
        return Color('black')
