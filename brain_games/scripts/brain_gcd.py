from random import randint
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


username = welcome_user()
score = 0


def main():
    (welcome_user)


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def brain_gcd(n):
    global score
    counter = 0
    while counter < 3:
        x = randint(1, 100)
        y = randint(1, 100)
        print('Find the greatest common divisor of given numbers.')
        print('Question:', str(x), str(y))
        answer = input()
        print('Your answer:', answer)
        
        def finder_gcd(x, y):
            while y != 0:
                (x, y) = (y, x % y)
            return x
        x = finder_gcd(x, y)
        if answer == str(x):
            print('Correct!')
            score += 1
            counter = counter + 1
        else:
            print(answer + " is wrong answer ;(. Correct answer was " + str(x))
            counter = counter + 4


brain_gcd(3)
if score == 3:
    print('Congratulations, ' + username + '!')
else:
    print("Let's try again, " + username + "!")
main()
