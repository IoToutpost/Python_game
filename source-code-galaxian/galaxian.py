# Galaxian
from random import randint
WIDTH = 600
HEIGHT = 800

bullet = Actor('bullet', center=(0, -10))
ship = Actor('ship', center=(300, 700))
backY = count = gameover = 0
aliens = []
for a in range(0, 8):
    aliens.append(Actor('alien0', center=(200+(a*50),200)))
    aliens[a].status = 0
    aliens[a].side = int(a/4)
        
for a in range(0, 8):
    aliens.append(Actor('alien0', center=(200+(a*50),250)))
    aliens[a+8].status = 0
    aliens[a+8].side = int(a/4)

def draw():
    screen.blit("background", (0, 0))
    screen.blit("stars", (0, backY))
    screen.blit("stars", (0, backY-800))
    bullet.draw()
    drawAliens()
    if gameover != 1 or (gameover == 1 and count%2 == 0): ship.draw()
    
def update():
    global backY, count
    count += 1
    if gameover == 0:
        backY += 0.2
        if backY > 800: backY = 0
        if bullet.y > -10: bullet.y -= 5
        if keyboard.left and ship.x > 50 : ship.x -= 4
        if keyboard.right and ship.x < 550 : ship.x += 4
        if keyboard.space :
            if bullet.y < 0: bullet.pos = (ship.x,700)
        updateAliens()
        
def drawAliens():
    for a in range(0, 16):
        if aliens[a].status < 5 : aliens[a].draw();

def updateAliens():
    global gameover
    for a in range(0, 16):
        aliens[a].image = "alien0"
        if count%30 < 15 : aliens[a].image = "alien1"
        if count%750 < 375:
            aliens[a].x -=0.4
        else:
            aliens[a].x +=0.4
        if aliens[a].collidepoint(bullet.pos) and aliens[a].status < 2:
            aliens[a].status = 2
            bullet.y = -10
        if aliens[a].colliderect(ship) : gameover = 1
        if randint(0,1000) == 1 and aliens[a].status == 0 : aliens[a].status = 1
        if aliens[a].status == 1 : flyAlien(a)
        if aliens[a].status > 1 and aliens[a].status < 5:
            aliens[a].image = "alien" + str(aliens[a].status)
            aliens[a].status += 1

def flyAlien(a):
    if aliens[a].side == 0:
        if aliens[a].angle < 180 :
            aliens[a].angle += 2
            aliens[a].x -= 1
            if aliens[a].angle < 90: aliens[a].y -= 1
        if aliens[a].angle >= 90 :
            aliens[a].y += 2
        if aliens[a].angle >= 180 :
            aliens[a].angle = 180
            aliens[a].x += 1
    else:
        if aliens[a].angle > -180 :
            aliens[a].angle -= 2
            aliens[a].x += 1
            if aliens[a].angle > -90: aliens[a].y -= 1
        if aliens[a].angle <= -90 :
            aliens[a].y += 2
        if aliens[a].angle <= -180 :
            aliens[a].angle = -180
            aliens[a].x -= 1
