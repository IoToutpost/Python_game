import random
secret = random.randint(1,10)
print('------猜数字游戏！-----')
guess = 0
while guess != secret:
    temp = input('猜数字游戏开始，请输入数字：')
    guess = int(temp)
    if guess > secret:
        print('您输入的数字大了！')
    else:
        print('您输入的数字小了！')
    if guess == secret:
        print('恭喜，您猜对了！')
        print('游戏结束，再见！^_^')