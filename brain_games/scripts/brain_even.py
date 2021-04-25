import prompt
from random import randint


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def main():
    (welcome_user)


username = welcome_user()
score = 0


def brain_even(n):
    global score
    counter = 0
    while counter < 3:
        user_number = int(randint(1, 100))
        print("Question:", user_number)
        print('Your answer:')
        answer = input()
        if (user_number) % 2 == 0 and answer == str('yes'):
            print('Correct!')
            counter = counter + 1
            score += 1
        elif (user_number) % 2 == 0 and answer == str('no'):
            print("'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, " + username + "!")
            counter = counter + 1
        elif (user_number) % 2 != 0 and answer == str('no'):
            print('Correct!')
            counter = counter + 1
            score += 1
        elif (user_number) % 2 != 0 and answer == str('yes'):
            print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, " + username + "!")
            counter = counter + 1
        else:
            print('Incorrect answer type')
            counter = counter + 1


print("Answer \"yes\" if the number is even, othervise answer \"no\".")
brain_even(3)


if score == 3:
    print('Congratulations, ' + username + '!')
else:
    print('Sorry, but you lost, ' + username + '. You can rerun the game.')
    main()
