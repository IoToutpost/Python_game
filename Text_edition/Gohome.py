print ('《回村》0.1版本','Author: Medivh & Winter')
print ('附注：基于 Andrew Gillett 的 Demo 开发')
print ('更多内容请关注微博或微信公众号：IoT前哨站')
print ('')
print ('欢迎来到风景优美的山谷。但是时间不早了，你要返回村庄。亲戚朋友还在等你回去聚餐。')
print ('')
directions = ['北面','南面','东面','西面']

# Data structure to store details of each location in the game

class Location:
    # Constructor - set up
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.linkedLocations = {}
        # Empty dictionary - will store which locations are linked to which other locations



    def addLink(self, direction, destination):
        # Add link to linkedLocations dictionary (if the specified direction and destination are valid)
   

        if direction not in directions:
            raise ValueError('方向错误')
        elif destination not in locations:
            raise ValueError('目的地无效')
        else:
            self.linkedLocations[direction] = destination

# Dictionary with location ID strings as keys and Location objects as the values


locations = {
              '森林':Location('有个森林', '你在森林。这里有很多树。'),
              '湖泊':Location('有个湖泊', '你现在在湖边，这里很潮湿。'),
              '小山':Location('有个小山', '这里有蜿蜒的小路。'),
              '村庄':Location('有个村庄', '*恭喜你，你现在到村庄了，大家正等你吃饭呢。*')
              }


locations['森林'].addLink('北面','湖泊')
locations['森林'].addLink('东面','小山')
locations['湖泊'].addLink('南面','森林')
locations['小山'].addLink('西面','森林')
locations['小山'].addLink('南面','村庄')
locations['村庄'].addLink('北面','小山')

currentLocation = locations['森林']

# Main game loop
while True:
    # Display description of current location

    print(currentLocation.description)

    # Display neighbouring locations

    for linkDirection,linkedLocation in currentLocation.linkedLocations.items():
        print(linkDirection + ': ' + locations[linkedLocation].name)

    # Read player input
    command = input('>').lower()
    if command in directions:
        if command not in currentLocation.linkedLocations:
            print('你不能走那里。')
        else:
            newLocationID = currentLocation.linkedLocations[command]
            currentLocation = locations[newLocationID]
    else:
        print('尝试一个方向: ' + ', '.join(directions))
        # Show list of directions, separated by commas



#让玩家走出一个森林，回到村庄。
