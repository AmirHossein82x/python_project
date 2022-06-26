import csv
import random
import sys
import tabulate
class Cell:
    def __init__(self):
        self.__content = []

    @property
    def content(self):
        return self.__content
    
    def add_content(self, obj):
        self.__content.append(obj)

    def remove_content(self, obj):
        self.__content.remove(obj)
    
    def __str__(self):
        return '-'.join(map(str, self.__content)).center(3)

class Winhouse:
    def __init__(self):
        self.x = 9
        self.y = 9

    def __str__(self):
        return "W".center(3)

class Teleport:
    def __init__(self):
        self.x = 4
        self.y = 5

    def __str__(self):
        return "T".center(3)
    
class Board:
    def __init__(self, length, width):
        self.__road = [[Cell() for i in range(width)]for i in range(length)]
        winer_house = Winhouse()
        tele_house = Teleport()
        self.__road[winer_house.y][winer_house.x] = winer_house
        self.__road[tele_house.y][tele_house.x] = tele_house

    @property
    def road(self):
        return self.__road

    def add_content(self,obj):
        if obj.x < 0 or obj.y < 0:
            raise IndexError
        else:
            self.__road[obj.y][obj.x].add_content(obj)

    def remove_content(self,obj):
        self.__road[obj.y][obj.x].remove_content(obj)

    @property
    def add_bomb(self):
        count = 0
        while count < 1:
            bomb_x = random.randint(0, 9)
            bomb_y = random.randint(0, 9)
            cell = self.road[bomb_y][bomb_x]
            if isinstance(cell, Cell):
                self.road[bomb_y][bomb_x] = Bomb()
                count += 1

    @property
    def show(self):
        for row in self.__road:
            new_row = "|" + "|".join(map(str, row)) + "|"
            print("-" * len(new_row))
            print(new_row)
        print("-" * len(new_row))

street = Board(10, 10)

class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        street.add_content(self)

    
    def move(self, direction):
        if direction == 'right':

            try:
                street.remove_content(self)
                self.x += 1
                cell = street.road[self.y][self.x]

                if isinstance(cell, Winhouse):
                    sys.exit('YOU WIN!')

                elif isinstance(cell, Bomb):
                    sys.exit('YOU LOST')

                elif isinstance(cell, Teleport):
                    while True:
                        new_x, new_y = list(map(int, input('enter new_x, new_y (new_x,new_y): ').split(",")))
                        self.x = new_x
                        self.y = new_y
                        cell = street.road[self.y][self.x]

                        if isinstance(cell, Winhouse):
                            print('you can not choose finall house!')

                        elif isinstance(cell, Teleport):
                            print('you can not choose Teleport house again!')
                        

                        elif isinstance(cell, Bomb):
                            sys.exit('YOU LOST')
                        else:
                            street.add_content(self)
                            break
                else:
                    street.add_content(self)

            except IndexError:
                self.x -= 1
                street.add_content(self)
                print('can not move!')

        elif direction == 'left':

            try:
                street.remove_content(self)
                self.x -= 1
                cell = street.road[self.y][self.x]

                if isinstance(cell, Bomb):
                    sys.exit('YOU LOST')

                elif isinstance(cell, Teleport):
                    while True:
                        new_x, new_y = list(map(int, input('enter new_x, new_y (new_x,new_y): ').split(",")))
                        self.x = new_x
                        self.y = new_y
                        cell = street.road[self.y][self.x]

                        if isinstance(cell, Winhouse):
                            print('you can not choose finall house!')

                        elif isinstance(cell, Teleport):
                            print('you can not choose Teleport house again!')

                        elif isinstance(cell, Bomb):
                            sys.exit('YOU LOST')
                        else:
                            street.add_content(self)
                            break
                else:
                        street.add_content(self)

            except IndexError:
                self.x += 1
                street.add_content(self)
                print('can not move!')

        elif direction == 'up':

            try:
                street.remove_content(self)
                self.y -= 1
                cell = street.road[self.y][self.x]

                if isinstance(cell, Bomb):
                    sys.exit('YOU LOST')

                elif isinstance(cell, Teleport):
                    while True:
                        new_x, new_y = list(map(int, input('enter new_x, new_y (new_x,new_y): ').split(",")))
                        self.x = new_x
                        self.y = new_y
                        cell = street.road[self.y][self.x]

                        if isinstance(cell, Winhouse):
                            print('you can not choose finall house!')

                        if isinstance(cell, Teleport):
                            print('you can not choose teleport house again!')

                        elif isinstance(cell, Bomb):
                            sys.exit('YOU LOST')
                        else:
                            street.add_content(self)
                            break
                else:
                    street.add_content(self)

            except IndexError:
                self.y += 1
                street.add_content(self)
                print('can not move!')

        elif direction == 'down':

            try:
                street.remove_content(self)
                self.y += 1
                cell = street.road[self.y][self.x]

                if isinstance(cell, Winhouse):
                    sys.exit('YOU WIN!')

                elif isinstance(cell, Bomb):
                    sys.exit('YOU LOST')

                elif isinstance(cell, Teleport):
                    while True:
                        new_x, new_y = list(map(int, input('enter new_x, new_y (new_x,new_y): ').split(",")))
                        self.x = new_x
                        self.y = new_y
                        cell = street.road[self.y][self.x]

                        if isinstance(cell, Winhouse):
                            print('you can not choose finall house!')

                        if isinstance(cell, Teleport):
                            print('you can not choose teleport house again!')


                        elif isinstance(cell, Bomb):
                            sys.exit('YOU LOST')
                        else:
                            street.add_content(self)
                            break
                else:
                    street.add_content(self)

            except IndexError:
                self.y -= 1
                street.add_content(self)
                print('can not move!')

    def __str__(self):
        return "R".center(3)

class Bomb:

    @property
    def add_bomb(self):
        count = 0
        while count < 2:
            dots = []
            
            
            for i in range(2):
                x = random.randint(1, 8)
                y = random.randint(1, 8)
                dots.append((x, y))
            for bomb_x, bomb_y in dots:
                cell = street.road[bomb_y][bomb_x]
                if isinstance(cell, Cell):
                   street.road[bomb_y][bomb_x] = self
                   count += 1
                   
                        
            
        
    def __str__(self):
        return "B".center(3)

a = Bomb()
a.add_bomb
robot = Robot()
with open("pro_robot_info.csv", "r") as file:
    reader = csv.DictReader(file)
    print(tabulate.tabulate(reader, headers="keys", tablefmt="grid"))

class GameEngin:
    
    @property
    def run(self):
        self.round = 0
        while True:
            street.show
            direction = input('which direction would you want to go: ')
            robot.move(direction=direction)
            self.round += 1
            if self.round % 2 == 0:
                street.add_bomb

game = GameEngin()
game.run