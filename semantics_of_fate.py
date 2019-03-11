# HOMEWORK 6 --- ES2
# Semantics of Fate
#
# FILL THESE COMMENTS IN
#*****************************************
# YOUR NAME:
# NUMBER OF HOURS TO COMPLETE:
# YOUR COLLABORATION STATEMENT(s):
# 
#
#*****************************************

import random
import numpy as np

def flipacoin():
    #This function flips a virtual coin and returns "Heads" or "Tails"
    coin = random.randint(1, 2) #returns a 1 or a 2
    if coin == 1:
        coin = "Heads"
    elif coin == 2:
        coin = "Tails"

def flipNcoins(n):
    #This function flips a coin a number of times (n flips total) and returns a string stating results.
    total_heads = 0
    total_tails = 0
    for i in range(n):
        if flipacoin() == "Heads":
            total_heads += 1
        else:
            total_tails += 1
    return "Heads " + str(total_heads) + ", Tails " + str(total_tails) 


def rolladie():
    #This function rolls a virtual die and returns a number between 1 and 6.
    die = random.randint(0,6)
    return die

def rolltwodice():
    #This function rollstwo virtual dice and returns a tuple of the two values.
    die1 = rolladie()
    die2 = rolladie()
    return die1, die2

def rollNdice(n):
    #This function rolls n virtual dice and returns an array of roll values between 1 and 6.
    rolls = np.zeros((n,))
    for i in range(n):
        die = rolladie()
        rolls[i] = die   
    return rolls

# Test Function Lines Lines
print("=====================================")
print("Coin Flip Result: " + str(flipacoin()))
print("1000 Flips: " + flipNcoins(1000))
print("=====================================")
print("Die Roll Result: " + str(rolladie()))
print("Two Dice Result: " + str(rolltwodice))
print("10 Dice Result: " + str(rollNdice(10)))
