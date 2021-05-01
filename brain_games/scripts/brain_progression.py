from random import randint, choice
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


def brain_progression(n):
    global score
    counter = 0
    while counter < 3:
        delta = randint(1, 10)
        n1 = randint(1, 15)
        n2 = n1 + delta
        n3 = n2 + delta
        n4 = n3 + delta
        n5 = n4 + delta
        n6 = n5 + delta
        brain_numbers = [n1, n2, n3, n4, n5, n6]
        hider = choice(brain_numbers)
        if hider == n1:
            print('What number is missing in the progression?')
            print('..', n2, n3, n4, n5, n6)
            answer = input()
            print('Your answer:', answer)
            if answer == str(n1):
                print('Correct!')
                score += 1
                counter = counter + 1
            else:
                print("'" + str(answer) + "'", "is wrong answer ;(. Correct answer was", "'" + str(n1) + "'")
                counter = counter + 3
        elif hider == str(n2):
            print('What number is missing in the progression?')
            print(n1, '..', n3, n4, n5, n6)
            answer = input()
            print('Your answer:', answer)
            if answer == n2:
                print('Correct!')
                score += 1
                counter = counter + 1
            else:
                print("'" + str(answer) + "'", "is wrong answer ;(. Correct answer was", "'" + str(n2) + "'")
                counter = counter + 3
        elif hider == n3:
            print('What number is missing in the progression?')
            print(n1, n2, '..', n4, n5, n6)
            answer = input()
            print('Your answer:', answer)
            if answer == str(n3):
                print('Correct!')
                score += 1
                counter = counter + 1
            else:
                print("'" + str(answer) + "'", "is wrong answer ;(. Correct answer was", "'" + str(n3) + "'")
                counter = counter + 3
        elif hider == n4:
            print('What number is missing in the progression?')
            print(n1, n2, n3, '..', n5, n6)
            answer = input()
            print('Your answer:', answer)
            if answer == str(n4):
                print('Correct!')
                score += 1
                counter = counter + 1
            else:
                print("'" + str(answer) + "'", "is wrong answer ;(. Correct answer was", "'" + str(n4) + "'")
                counter = counter + 3
        elif hider == n5:
            print('What number is missing in the progression?')
            print(n1, n2, n3, n4, '..', n6)
            answer = input()
            print('Your answer:', answer)
            if answer == str(n5):
                print('Correct!')
                score += 1
                counter = counter + 1
            else:
                print("'" + str(answer) + "'", "is wrong answer ;(. Correct answer was", "'" + str(n5) + "'")
                counter = counter + 3
        elif hider == n6:
            print('What number is missing in the progression?')
            print(n1, n2, n3, n4, n5, '..')
            answer = input()
            print('Your answer:', answer)
            if answer == str(n6):
                print('Correct!')
                score += 1
                counter = counter + 1
            else:
                print("'" + str(answer) + "'", "is wrong answer ;(. Correct answer was", "'" + str(n6) + "'")
                counter = counter + 3


brain_progression(3)
if score == 3:
    print('Congratulations, ' + username + '!')
else:
    print("Let's try again, " + username + "!")

