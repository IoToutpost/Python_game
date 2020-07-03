# Jet Pac
import random
import time
t0 = time.clock()
jetman = Actor('jetmanl',(400,500))
ground = Actor('ground',(400,550))
platform1 = Actor('platform1',(400,350))
platform2 = Actor('platform2',(200,200))
platform3 = Actor('platform3',(650,200))
rocket1 = Actor('rocket1',(520,500))
rocket2 = Actor('rocket2',(400,300))
rocket3 = Actor('rocket3',(200,150))
rocketFire = Actor('rocketfire',(521,0))
fuel = Actor('fuel',(50,-50))
gravityList = [jetman,rocket1,rocket2,rocket3,fuel]
drawList = [rocket1,rocket2,rocket3,ground,platform1,platform2,platform3,fuel]
platformList = [ground,platform1,platform2,platform3]
collideList = [rocket1,rocket2,rocket3]
pickupList = [rocket2,rocket3,fuel,0,fuel,0,fuel,0,0]
gravity = 1.5
jetman.thrust = jetman.holding = jetman.item = gameState = fuelLevel = timeElapsed = 0
jetman.dir = "l"

def draw():
    global timeElapsed
    screen.clear()
    for i in range(0, len(drawList)):
        drawList[i].draw()
    if gameState == 0:
        jetman.draw()
        timeElapsed = int(time.clock() - t0)
    else:
        rocketFire.draw()
        screen.draw.text("MISSION ACCOMPLISHED", center = (400, 300), owidth=0.5, ocolor=(255,255,255), color=(0,0,255) , fontsize=80)
    screen.draw.text("TIME:"+str(timeElapsed), center= (400, 20), owidth=0.5, ocolor=(255,255,255), color=(255,0,0) , fontsize=40)
    
def update():
    global gameState, fuelLevel
    burn = ""
    if gameState == 0:
        if keyboard.up:
            jetman.thrust = limit(jetman.thrust+0.3,0,5)
            burn = "f"
        if keyboard.left:
            jetman.dir = "l"
            jetman.x -= 1
        if keyboard.right:
            jetman.dir = "r"
            jetman.x += 1
        applyGravity()
        coll = checkCollisions(platformList,(jetman.x,jetman.y-32))
        if coll == False:
            jetman.y -= jetman.thrust
        if pickupList[jetman.item] != 0:
            if checkTouching(pickupList[jetman.item], jetman):
                jetman.holding = pickupList[jetman.item]        
        jetman.thrust = limit(jetman.thrust-0.1,0,5)
        jetman.image = "jetman" + jetman.dir + burn
        if jetman.holding != 0 :
            jetman.holding.pos = jetman.pos
            if jetman.holding.x == rocket1.x and jetman.holding.y < 440:
                jetman.holding = 0
                jetman.item += 1
        if fuel.x == rocket1.x and fuel.y+16 > rocket3.y-32 and jetman.holding == 0:
            fuelLevel += 1
            if fuelLevel < 4:
                jetman.item += 1
                if fuelLevel < 3 :
                    fuel.pos = (random.randint(50, 750),-50)
                else:
                    fuel.pos = (0,650)
                gravityList[fuelLevel].image = "rocket"+str(fuelLevel)+"f"
        if fuelLevel == 3 and jetman.x == rocket1.x and jetman.y > rocket3.y:
            gameState = 1       
    if gameState == 1:
        rocket1.y -= 1
        rocket2.y -= 1
        rocket3.y -= 1
        rocketFire.y = rocket1.y + 50
            
def limit(n, minn, maxn):
    return max(min(maxn, n), minn)

def checkCollisions(cList, point):
    for i in range(0, len(cList)):
        if cList[i].collidepoint(point):
            return True
    return False
    
def checkTouching(a1,a2):
    if a1.colliderect(a2): return True
    return False
    
def applyGravity():
    for i in range(0, len(gravityList)):
        if checkCollisions(platformList,(gravityList[i].x,gravityList[i].y+(gravityList[i].height/2))) == False and checkCollisions(collideList,(gravityList[i].x,gravityList[i].y+(gravityList[i].height/2))) == False:
            gravityList[i].y += gravity
