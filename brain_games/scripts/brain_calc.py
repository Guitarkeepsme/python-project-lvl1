from random import randint
from random import choice
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def main():
    (welcome_user)


username = welcome_user()
score = 0


def calc(n):
    global score
    counter = 0
    while counter < 3:
        n_1 = randint(1, 50)
        n_2 = randint(1, 50)
        n_3 = randint(1, 10)
        n_4 = randint(1, 10)
        n_5 = randint(25, 50)
        n_6 = randint(1, 25)
        game_sum = str(n_1) + ' + ' + str(n_2)
        prod = str(n_3) + ' * ' + str(n_4)
        diff = str(n_5) + ' - ' + str(n_6)
        math_syq = [game_sum, prod, diff]
        result = choice(math_syq)
        print('What is the result of the expression?')
        print('Question:', result)
        answer = input()
        print('Your answer:', answer)
        if result == game_sum and answer == str(n_1 + n_2):
            print('Correct!')
            score += 1
            counter = counter + 1
        elif result == game_sum and answer != str(n_1 + n_2):
            print(answer + " is wrong answer ;(. Correct answer was " + str(n_1 + n_2))
            counter = counter + 3
        elif result == prod and answer == str(n_3 * n_4):
            print('Correct!')
            score += 1
            counter = counter + 1
        elif result == prod and answer != str(n_3 * n_4):
            print(answer + " is wrong answer ;(. Correct answer was " + str(n_3 * n_4))
            counter = counter + 3
        elif result == diff and answer == str(n_5 - n_6):
            print('Correct!')
            score += 1
            counter = counter + 1
        elif result == diff and answer != str(n_5 - n_6):
            print(answer + " is wrong answer ;(. Correct answer was " + str(n_5 - n_6))
            counter = counter + 3


calc(3)
if score == 3:
    print('Congratulations, ' + username + '!')
else:
    print("Let's try again, " + username + "!")
