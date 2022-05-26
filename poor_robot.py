from random import randint
import random
board_length = 10
board_width = 10
hole_count = 2
cell_size = 3
length_size = 41
robot_sign = "X"
hole_sign = "#"
safe_house_sign = "H"
final_home = "W"
holes_situation = list()
board = list()
safe_house_situation = [(6, 4), (8, 2)]
final_home_x = 9
final_home_y = 9
for x in range(board_length):
    new_row = list()
    for y in range(board_width):
        new_row.append("-")
    board.append(new_row)
robot_x = 0
robot_y = 0
board[robot_y][robot_x] = robot_sign
board[final_home_y][final_home_x] = final_home
def print_board():
    def str_center(item):
        return str(item).center(cell_size)
    print("-" * length_size)
    for row in board:
        row_cell = "|" + "|".join(map(str_center, row)) + "|"
        print(row_cell)
        print("-" * length_size)
for safe_x, safe_y in safe_house_situation:
    board[safe_y][safe_x] = safe_house_sign
def can_move(x, y):
    global robot_y, robot_x
    valid_move = False
    if 0 <= x < board_length and 0 <= y < board_width:
        valid_move = True
        return valid_move
    else:
        print("can not move!")
        return valid_move
def move(x, y):
    global robot_y, robot_x
    board[robot_y][robot_x] = "-"
    robot_x, robot_y = x, y
    board[robot_y][robot_x] = robot_sign
def move_right():
    new_x = robot_x + 1
    new_y = robot_y
    if can_move(new_x, new_y):
        move(new_x, new_y)
def move_left():
    new_x = robot_x - 1
    new_y = robot_y
    if can_move(new_x, new_y):
        move(new_x, new_y)
def move_up():
    new_x = robot_x 
    new_y = robot_y - 1
    if can_move(new_x, new_y):
        move(new_x, new_y)
def move_down():
    new_x = robot_x 
    new_y = robot_y + 1
    if can_move(new_x, new_y):
        move(new_x, new_y)
for i in range(hole_count):
        hole_x = randint(0, board_length - 1)
        hole_y = randint(0, board_width - 1)
        if board[hole_y][hole_x] != safe_house_sign and board[hole_y][hole_x] != final_home and board[hole_y][hole_x] != robot_sign and board[hole_y][hole_x] != hole_sign:
            board[hole_y][hole_x] = hole_sign
            holes_situation.append((hole_y, hole_x))
            
def make_hole():
    while True:
        hole_x = randint(0, board_length - 1)
        hole_y = randint(0, board_width - 1)
        if hole_x != robot_x and hole_y != robot_y and board[robot_y][robot_x] != safe_house_sign and board[robot_y][robot_x] != final_home and board[robot_y][robot_x]!=hole_sign:
            board[hole_y][hole_x] = hole_sign
            holes_situation.append((hole_x, hole_y))
            break

controller = {"U": move_up, "D": move_down, "R": move_right, "L": move_left}
game_round = 1
while True:
    print_board()
    
    direction = input("enter direction: ")
    chance = "UDRL"
    result = controller.get(random.choice(chance))
    for i in range(randint(1, 4)):
        result()
    for hole_x, hole_y in holes_situation:
        board[hole_y][hole_x] = hole_sign
    for safe_x, safe_y in safe_house_situation:
        board[safe_y][safe_x] = safe_house_sign
    for safe_x, safe_y in safe_house_situation:
        if robot_x == safe_x and robot_y == safe_y:
            safe_direction = input("enter safe direction: ").upper()
            side = controller.get(safe_direction)
            side()
            for hole_x, hole_y in holes_situation:
                board[hole_y][hole_x] = hole_sign
            for safe_x, safe_y in safe_house_situation:
                board[safe_y][safe_x] = safe_house_sign
    if robot_x == final_home_x and robot_y == final_home_y:
        print("You win!")
        exit()

    for hole_x, hole_y in holes_situation:
        if robot_x == hole_x and robot_y == hole_y:
            print("game over!")
            exit()

    if game_round % 3 == 0:
        make_hole()

    game_round += 1
    
    



