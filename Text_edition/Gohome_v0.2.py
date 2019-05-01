print ('《回村》v0.2版本','Author: Medivh')
print ('附注：基于 Andrew Gillett 的 Demo 开发')
print ('更多内容请关注微博或微信公众号：IoT前哨站')
print ('')
print ('欢迎来到风景优美的山谷。但是时间不早了，你要找到牛肉和红酒。亲戚朋友还在等你回去聚餐。')
print ('不要被强盗抓住哦。')
print ('')

print('''玩法:
  移动 [四个方向，比如输入“去 北面”]
  获取 [拿起物品，比如输入“拿起 牛肉”]
''')


directions = ['北面','南面','东面','西面']

#集合所有重要信息的字典
locations  = {

            '森林' : { '南面' : '湖泊',
                  '东面'  : '小山',
                  '物品'  : '牛肉'
                },        

            '湖泊' : { '北面' : '森林',
                  '物品'  : '强盗'
                },
                
            '小山' : { '西面'  : '森林',
                  '南面' : '村庄',
                  '物品'  : '红酒'
              
                },
                
            '村庄' : { '北面' : '小山' }

         }


currentLocation = '森林'

def showStatus():
    
  print('---------------------------')
  print('你现在的位置在：' + currentLocation)
  print("物品： " + str(inventory))
  if "物品" in locations[currentLocation]:
    print('这里有：' + locations[currentLocation]['物品'])
  print("---------------------------")

inventory = []

while True:

  showStatus()

  move = ''
  while move == '':  
    move = input('>')
    
  move = move.lower().split()


  if move[0] == '去':
    if move[1] in locations[currentLocation]:
      currentLocation = locations[currentLocation][move[1]]
    else:
      print('你走不过去!')

  if move[0] == '拿起' :
    if '物品' in locations[currentLocation] and move[1] in locations[currentLocation]['物品']:
      inventory += [move[1]]
      print(move[1] + ' 已得到!')
      del locations[currentLocation]['物品']
    else:
      print('无法获得 ' + move[1] + '!')

  if '物品' in locations[currentLocation] and '强盗' in locations[currentLocation]['物品']:
    print('一队强盗抓到了你...GAME OVER!')
    break

  if currentLocation == '村庄' and '牛肉' in inventory and '红酒' in inventory:
    print('你带着食物回到村庄了，大家都为你感到高兴!')
    break
  


