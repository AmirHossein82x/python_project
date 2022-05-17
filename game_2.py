def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1
    
    for key in questions:
        print('--------------------------------------')
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input('Enter (A, B, C, D): ').upper()
        guesses.append(guess)


        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print('correct')
        return 1
    else:
        print('wrong')
        return 0
def display_score(correct_guesses, guesses):
    print('------------------------------------')
    print('RESULT')
    print('------------------------------------')
    print('Answers: ', end='')
    for i in questions:
        print(questions.get(i), end=' ')
    print()

    print('Gueses: ', end='')
    for j in guesses:
        print(j, end=' ')
    print()

    score = int((correct_guesses/len(questions))*100)
    print("your score is: "+ str(score)+ "%")
def play_again():
    response = input('Do you want to play again? (yes or no): ').upper()
    if response == "YES":
        return True
    else:
        return False
questions = {
    'who created python? ': 'A',
    'what yrear was python created? ': 'B',
    'python is tributed to which comedy group? ':'C',
    "is the earth round? ":'A'
}

options = [['A. Guide van Rossum', 'B. Elon Mask', 'C. Bill Gates', 'Mark Zackerburg'],
          ['A. 1989', 'B. 1991', 'C. 2000', 'D. 2016'],
          ['A. Lonley Island', 'B. Smosh', 'C. Monty python', 'D. SNL'],
          ['A. True', 'B. False', 'C. Sometimes', "D. what's earh"]]
new_game()
while play_again():
    new_game()
print('bye')



