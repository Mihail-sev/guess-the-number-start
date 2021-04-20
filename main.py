
from random import randint
from art import logo
print (logo)
level = input ("Welcome to GuessHame.\nTry to guess number from 1 to 100.\n Choose your dificult level: 'hard' or 'easy'.\n") 

rand_number = randint (1, 100)
if level == "easy":
  attempts = 10
else:
  attempts = 5  

user_number = int(input(f"You have {attempts} attempts. \n Make you guess:  "))
attempts -= 1
def check_number(checked_number):
  """ Check guessed user number to correct answer"""
  global user_number
  if checked_number == rand_number:
    print (f"You got it! Correct answer was {rand_number}")
    return False
  elif checked_number < rand_number:
    user_number = int(input(f"Too low.\n Guess again.\n You have {attempts} attempts remaining to guess the number.\n \n Make you guess:  "))
    return True
  elif checked_number > rand_number:
    user_number = int(input (f"Too high.\n Guess again.\n You have {attempts} attempts remaining to guess the number.\n \n Make you guess:  "))
    return True

number_unguessed = True
while  number_unguessed:
  number_unguessed = check_number (user_number)
  attempts -= 1
  if attempts == 0:
    number_unguessed = False
    print (f"You've run out of guesses, you lose. The unguessed number is {rand_number}")