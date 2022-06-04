class Cell:

    def __init__(self, pos):
        self.__pos = pos
        self.__content = []

    @property
    def pos(self):
        return self.__pos

    def add_content(self, element):
        if isinstance(element, Car):
            self.__content.append(element)
        else:
            print('Invalid Type')

    def remove_content(self, element):
        self.__content.remove(element)

    def __str__(self):
        return " ".join(map(lambda item: item.name, self.__content)).center(20)

class Street:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        self.__road = [[Cell(i)for i in range(self.__width)] for i in range(self.__length)]

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width
    
    def add_content(self, pos_x, pos_y, element):
        self.__road[pos_y][pos_x].add_content(element)

    def remove_content(self, pos_x, pos_y, element):
        self.__road[pos_y][pos_x].remove_content(element)

    def print_street(self):

        print("-" * ((16 * self.__length) + 10))

        for item in self.__road:
            row = "|" + "|".join(map(str, item)).center(20)
            print(row)
            print("-" * ((16 * self.__length) + 10))

         
my_street = Street(6, 6)

class Car:

    def __init__(self, name):
        self.__name = name
        self.__pos_x = 0
        self.__pos_y = 0
        global my_street
        my_street.add_content(self.__pos_x, self.__pos_y, self)

    @property
    def name(self):
        return self.__name

    def move(self, direction):

        global my_street

        if direction == "forward":
            new_pos_x = self.__pos_x + 1
            new_pos_y = self.__pos_y 

            if 0 <= new_pos_x < my_street.length:
                my_street.remove_content(self.__pos_x, self.__pos_y, self)
                self.__pos_x = new_pos_x
                self.__pos_y = new_pos_y
                my_street.add_content(self.__pos_x,self.__pos_y, self)

            else:
                print("can not move")

        elif direction == 'back':
             new_pos_x = self.__pos_x - 1
             new_pos_y = self.__pos_y

             if new_pos_x>= 0:
                my_street.remove_content(self.__pos_x,self.__pos_y, self)
                self.__pos_x = new_pos_x
                self.__pos_y = new_pos_y
                my_street.add_content(self.__pos_x, self.__pos_y, self)

             else:
                print("can not move")

        elif direction == "up":
            new_pos_x = self.__pos_x
            new_pos_y = self.__pos_y - 1

            if new_pos_y > 0:
                my_street.remove_content(self.__pos_x,self.__pos_y, self)
                self.__pos_x = new_pos_x
                self.__pos_y = new_pos_y
                my_street.add_content(self.__pos_x, self.__pos_y, self)

            else:
                print("can not move")

        elif direction == "down":
            new_pos_x = self.__pos_x
            new_pos_y = self.__pos_y + 1

            if new_pos_y < my_street.width:
                my_street.remove_content(self.__pos_x,self.__pos_y, self)
                self.__pos_x = new_pos_x
                self.__pos_y = new_pos_y
                my_street.add_content(self.__pos_x, self.__pos_y, self)
                
            else:
                print("can not move")


class GameEngin:
    def run(self):
        
        cars_list = {}
        user = int(input('how many cars would you want to create? '))
        for i in range(user):
            name = input('enter name of car: ')
            name_of_car = Car(name)
            cars_list[name] = name_of_car
        my_street.print_street()
        
        while True:
            car_name = input('which car would you want to move? ')
            car_direction = input('which direction? ')
            choosen_car = cars_list.get(car_name)
            choosen_car.move(car_direction)
            my_street.print_street()
            user1 = input('would you want to stop? ').lower()
            if user1 == 'yes':
                print('Good luck')
                break


a = GameEngin().run()
