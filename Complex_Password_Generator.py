# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 21:48:26 2025

@author: nkart

Password Generator based on Based on User Input

"""
import random #Import random module to choose random value
import string # Imbuild module for getting the string values

d=string.ascii_letters # to get the a-z and A-Z values
print (d)
d=string.digits
print (d) # to get the 0-9 values
print(type(type(d))) #type
d=string.punctuation # to get symbols 
print(d) 
string.ascii_lowercase
string.ascii_uppercase


print("Welcome to Pypassword Generator!")

#get the user input
let = input("How many letter would you like in your password?\n")
sym = input("How many symbols would you like?\n")
num = input("How many numbers would you like?\n")


#assign initial values 
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','-','+']
numbers = ['1','2','3','4','5','6','7','8','9','0']

#generate password
password=[]
for i in range (int(let)):
    password+=random.choice(alpha)
for j in range (int(sym)):
    password.append(random.choice(symbols))
for k in range (int(num)):
    password.append(random.choice(numbers))

#shuffle the password
print(password)
random.shuffle(password)
print(password)

#convert the list to string
c=''
for char in password:
    c+=char
print(f"your AI generated password is:{c}")

d=''.join(password)
print(d)    

