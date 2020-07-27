# Warining! This code is not finished yet!
# Using: Python 3
# Written by Yasen Kostov

import time
import random
numberlist = ['1', '2', '3']

print ("Welcome to Rock-Paper-Scissors game!")
print ()
time.sleep(2)

a = int(input("Choose your item (1 for rock, 2 for paper, or 3 for scissors): "))
b = random.choice(numberlist)
print ()


if a == 1:
    if b == 1:
        print("Draw! The Machine chose rock too")
    if b == 2:
        print("You Lost! The Machine chose paper.")
    if b == 3:
        print("You Won! The Machine chose scissors.")

if a == 2:
    if b == 1:
        print ("You won! The Machine chose rock")
    if b == 2:
        print ("Draw! The Machine chose paper too")
    if b == 3:
        print ("You Lost! The Machine chose scissors")
if a == 3:
    if b == 1:
        print ("You Lost! The Machine chose rock")
    if b == 2:
        print ("You win! The Machine chose paper")
    if b == 3:
        print ("Draw! The Machine chose scissors too")
