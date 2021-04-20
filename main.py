#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from random import randint
from art import logo
print (logo)
level = input ("Welcome to GuessHame.\nTry to guess number from 1 to 100.\n Choose your dificult level: 'hard' or 'easy'.\n") 

rand_number = randint (1, 101)
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

number_guessed = True
while  number_guessed:
  number_guessed = check_number (user_number)
  attempts -= 1
  if attempts == 0:
    number_guessed = False
    print (f"You've run out of guesses, you lose. The unguessed number is {rand_number}")