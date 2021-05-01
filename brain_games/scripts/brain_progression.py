from random import randint
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def main():
    welcome_user


username = welcome_user()
score = 0


def prog(n):
    global score
    counter = 0
    while counter < 3:
        delta = randint(1, 10)
        n1 = randint(1, 15)
        n2 = n1 + delta
        n3 = n2 + delta
        n4 = n3 + delta
        n5 = n4 + delta
        print("Question:", n1, '..', n3, n4, n5)
        answer = input()
        if answer == str(n2):
            print('Your answer:', answer)
            print('Correct!')
            score += 1
            counter = counter + 1
        else:
            print("'" + str(answer) + "'", "is wrong answer.")
            print("Correct answer was", "'" + str(n2) + "'")
            counter = counter + 3


print('What number is missing in the progression?')
prog(3)
if score == 3:
    print('Congratulations, ' + username + '!')
else:
    print("Let's try again, " + username + "!")
