import random
import sys

print('Hello what is your name?')  # ask user for name
name = input()

secretNumber = random.randint(1, 20)  # generate random number
# ask user for number
print('Hi, ' + name + ', can guess what number I am thinking, 1 to 20')

for guessesTaken in range(1, 7):
    guess = int(input())

    if guess < secretNumber:
        print('Your number is too low. Try again!')
    elif guess > secretNumber:
        print('Your number is too high. Try again!')
    elif guess == secretNumber:
        print('Correct! It only took you ' + str(guessesTaken) +
              ' tries to guess my number. You are a mind reader.')
        sys.exit()  # end program

# ask if they want to know the number
print('Sorry, you took ' + str(guessesTaken) +
      ' guesses and still don\'t know. Want to know the answer? Yes or No:')
answer = str(input())
if answer == "yes":
    print('It was: ' + str(secretNumber) + '!')
else:
    print("Have it your way.")
