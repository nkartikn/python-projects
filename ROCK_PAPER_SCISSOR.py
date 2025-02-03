# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 19:48:34 2025

@author: nkart

ROCK PAPER SCISSOR
using RANDOM
ROCK = 0
PAPER = 1
SCISSOR = 2
0>1
"""
#Random module to select random int
import random

#Rock paper scissor ascii art
def roc_pap_sci(a,player):
    if a == 0:
        return print(f'''{player} Choosed ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')
    elif a == 1:
        return print(f'''{player} choosed PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''')
    else:
        return print(f'''{player} choosed SCISSOR
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')

#Decision making
def decision(you,cpu):
    if you == cpu:
        a="its a tie!\n"
    elif (you == 0 and cpu == 1) or (you == 1 and cpu == 2) or (you == 2 and cpu == 0) :
        a="CPU won the game!"
    elif (you == 0 and cpu ==2) or (you == 1 and cpu == 0) or (you == 2 and cpu == 1) :
        a="YOU won the game!"
    return a + '''
	 {}
    /__\\
  /|    |\\
 (_|    |_)
    \\  /
     )(
   _|__|_
  |______|'''
#Main Code Begins
a='Y'
print("Let's Play Rock Paper Scissor Game:\n")

#Loop to continue the game based on user input

while  a=='Y':
    
    if a=='Y':
        cpu=random.randint(0, 2) # To get the Random int no from 0-2
        you=input("Choose Rock(0), Paper(1) or Scissor(2) :\n") #User Input from 0-2
        if you.isnumeric() and you in ('0','1','2'): #User Input Validation
            roc_pap_sci(int(you), 'you') # function for ascii art
            roc_pap_sci(cpu, 'cpu')
            print(decision(int(you),cpu)) # function for descision
        else:
            print("Enter Valid input from below")
            you=input("Choose Rock(0), Paper(1) or Scissor(2) :\n")
        roc_pap_sci(int(you), 'you')
        roc_pap_sci(cpu, 'cpu')
        print(decision(int(you),cpu))

    else:
        break

    b=input("Press 'Y' to play again or any other button to EXIT:\n").upper()
    a=b;
    
    

