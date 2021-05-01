import prompt
from random import randint


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def main():
    welcome_user


username = welcome_user()
score = 0


def is_prime(number):
    d = 2
    while number % d != 0:
        d += 1
    if d == number:
        global pr
        pr = number
    else:
        pr = 51


def brain_prime(n):
    global score
    counter = 0
    while counter < 3:
        number = randint(1, 50)
        is_prime(number)
        print('Question:', number)
        print('Your answer:')
        answer = input()
        if number == pr and answer == str('yes'):
            print('Correct!')
            counter = counter + 1
            score += 1
        elif number != pr and answer == str('no'):
            print('Correct!')
            counter = counter + 1
            score += 1
        elif number == pr and answer == str('no'):
            print("'no' is wrong answer ;(. Correct answer was 'yes'")
            counter = counter + 3
        elif number != pr and answer == str('yes'):
            print("'yes' is wrong answer ;(. Correct answer was 'no'")
            counter = counter + 3


print("Answer \"yes\" if the number is prime, otherwise answer \"no\".")
brain_prime(3)


if score == 3:
    print('Congratulations, ' + username + '!')
else:
    print("Let's try again, " + username + "!")
