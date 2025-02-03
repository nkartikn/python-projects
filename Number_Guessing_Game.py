# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 18:49:00 2025

@author: nkart

Number Gussing game

use Random to import

Challenges:
Add Difficulty Levels:

Allow the user to choose a difficulty level (e.g., easy, medium, hard).
Adjust the number of attempts based on the difficulty:
Easy: 10 attempts
Medium: 7 attempts
Hard: 5 attempts

Track Best Score:
Keep track of the user's best score (fewest attempts to guess the number).
Display the best score at the end of each round.

Add a Timer:
Measure how long it takes the user to guess the number.
Display the time taken at the end of the game.

Input Validation:
Ensure the user enters a number within the valid range (e.g., 1 to 100).
Display an error message if the input is out of range.

Hints:
Provide hints after a certain number of failed attempts (e.g., "The number is even" or "The number is greater than 50").

Custom Range:
Allow the user to choose the range of numbers (e.g., 1 to 50, 1 to 200, etc.).

Multiplayer Mode:
Allow two players to take turns guessing the number.
The player who guesses the number in fewer attempts wins.

Score System:
Assign points based on the number of attempts:
Fewer attempts = higher score.

Display the score at the end of each round.

Visual Feedback:

Use ASCII art or emojis to provide visual feedback (e.g., 🎉 for a win, 😢 for a loss).

Save Progress:

Save the user's best score or progress to a file.
Load the saved data when the game starts.

"""
import random  # to choose random value
import time

#Code Begins

print('''Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100. Can you guess it in 5 chances?''')

next_round = False # to continue the loop till user inputs no

best_attempt = float("inf")

while not next_round:
    attempt = 0    # resets no of attempts by user
    chosen=random.randint(1,100)   # choose random number
    time_taken=time.time()

    difficulty = input("Enter difficulty of the game easy/medium/hard to play:") # deciding difficulty of the game
    if difficulty not in ('easy','medium','hard'):
        print("Enter valid input from below")
        continue
    if difficulty == 'easy':
        attempts = 15
    elif difficulty == 'medium':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
        
    while attempt<attempts:   # restricted to no of attempts to 5(use for loop to include invalid attempt as well)
        guess=input("Enter your guess:")    # user input
        if not guess.isnumeric():       # to Handle Invalid number
            print("Invalid Input! Try again")
            continue
        if int(guess) < 0 or int(guess) > 100:
            print("Enter no between 1 to 100")
            continue    # if invalid no continue the cycle and it wont increase the attempt
        
        guess = int(guess)
        attempt +=1 # attempt will increase only for valid input


        if chosen < guess:   #checking the user input with predicted value
            print("Too high! Try again.")
        elif chosen > guess:
            print("Too low! Try again.")
        elif chosen == guess:
            print(f"Correct🎉! You guessed the number in {attempt} attempts and {time.time()-time_taken:.2f} seconds")
            if attempt<best_attempt:
                best_attempt = attempt
                print("New best score",best_attempt,"attempts")
            else:
                print("Best score is:",best_attempt,"attempts")
            break
    else:  # it will execute one time after full loop range gets complete without break
        print(f"Game Over😢! You ran out of attempts. chosen word is {chosen}")

    nex = input ("Would you like to play again? (yes/no):").lower() # to continue the loop for next round
    if nex == 'no':
        print("Thanks for playing! Goodbye!")
        next_round = True
        


