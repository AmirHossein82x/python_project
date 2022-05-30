board_lengh, board_width = 5, 5

board = [["-"for i in range(board_lengh)]for i in range(board_width)]

class Street:

    @property
    def print_board(self):

        print('-' * ((board_lengh * 4) + 1))
        for item in board:
            row_cell = "|" + "|".join(map(lambda x: str(x).center(3), item)) + "|"
            print(row_cell)
            print('-' * ((board_lengh * 4) + 1))

class Car:
    def __init__(self, shape, x, y):
        self.shape = shape
        self.x = x
        self.y = y
        board[self.y][self.x] = self.shape

    
    def move_up(self):

        def can_move(x, y):

            if  0 <= x < board_width and 0 <= y < board_lengh:
                return True

            else:
                print('can not move! ')
                return False

        board[self.y][self.x] = " - "
        self.x = self.x
        self.y -= 1

        if can_move(self.x, self.y):
            board[self.y][self.x] = self.shape

        else:
            self.x = self.x
            self.y += 1
            board[self.y][self.x] = self.shape

    def move_down(self):

        def can_move(x, y):

            if  0 <= x < board_width and 0 <= y < board_lengh:
                return True

            else:
                print('can not move! ')
                return False

        board[self.y][self.x] = " - "
        self.x = self.x
        self.y += 1

        if can_move(self.x, self.y):
            board[self.y][self.x] = self.shape

        else:
            self.x = self.x
            self.y -= 1
            board[self.y][self.x] = self.shape
    
    def move_right(self):

        def can_move(x, y):

            if  0 <= x < board_width and 0 <= y < board_lengh:
                return True

            else:
                print('can not move! ')
                return False

        board[self.y][self.x] = " - "
        self.x += 1
        self.y = self.y
        if can_move(self.x, self.y):
            board[self.y][self.x] = self.shape

        else:
            self.x -= 1
            self.y = self.y
            board[self.y][self.x] = self.shape
    
    def move_left(self):

        def can_move(x, y):

            if  0 <= x < board_width and 0 <= y < board_lengh:
                return True

            else:
                print('can not move! ')
                return False

        board[self.y][self.x] = " - "
        self.x -= 1
        self.y = self.y
        if can_move(self.x, self.y):
            board[self.y][self.x] = self.shape

        else:
            self.x += 1
            self.y = self.y
            board[self.y][self.x] = self.shape

    @property
    def crash(self):
        return [(self.x, self.y)]

car1 = Car("#", 1, 1)
car2 = Car("$",2, 2)
street = Street()
street.print_board

controler_1 = {"up":car1.move_up, "down": car1.move_down, 'right':car1.move_right, 'left': car1.move_left}
controler_2 = {"up":car2.move_up, "down": car2.move_down, 'right':car2.move_right, 'left': car2.move_left}

while True:

    question = input('which car would you want to move? (car1 / car2): ').lower()
    
    if question == "car1":

        directoin = input('which direction would you want to move? (right, left, up, down): ').lower()
        try:

            a = controler_1.get(directoin)
            a()
            street.print_board
        except Exception:
            print("please enter correctly")

    elif question == "car2":

        directoin = input('which direction would you want to move? (right, left, up, down): ').lower()
        try:

            a = controler_2.get(directoin)
            a()
            street.print_board

        except Exception:
            print("please enter correctly")

    else:
        print('please enter correctly')

    if car1.crash == car2.crash:
        print('CRASH')
        break