import random
while True:
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input('rock, paper, scissors? ').lower()
    if player == computer:
        print('computer: %s'%computer)
        print('player: %s'%player)
        print('Tile')
    elif player == 'rock':
        if computer == 'paper':
            print('computer: %s'%computer)
            print('player: %s'%player)
            print('you lose!')
        if computer == "scissors":
            print('computer: %s'%computer)
            print('player: %s'%player)
            print('you win!')
    elif player == 'paper':
        if computer == 'rock':
            print('computer: %s'%computer)
            print('player: %s'%player)
            print('you win!')
        if computer == "scissors":
            print('computer: %s'%computer)
            print('player: %s'%player)
            print('you lose!')
    elif player == 'scissors':
        if computer == 'paper':
            print('computer: %s'%computer)
            print('player: %s'%player)
            print('you win!')
        if computer == "rock":
            print('computer: %s'%computer)
            print('player: %s'%player)
            print('you lose!')
    play_again = input('would you want to play again? (yes/no): ').lower()
    if play_again == 'yes':
        continue
    elif play_again == "no":
        break
print('bye')
