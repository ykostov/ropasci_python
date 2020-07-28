from random import randint
import time
gamelist = ["rock", "paper", "scissors"]
machine = gamelist[randint(0,2)]
player = False

print ()
print ("Welcome to the game 'Rock-Paper-Scissors' written with Python3 by Yasen Kostov")
time.sleep(5)
print ()
print ("The Machine is ready, are you?")
time.sleep(4)
print ()

while player == False:
    player = input("Chose something between 'rock', 'paper' or 'scissors': ")
    print ()
    time.sleep(1)
    print ("3")
    time.sleep(1)
    print ("2")
    time.sleep(1)
    print ("1")
    time.sleep(1)
    print ()
    if player == machine:
        print ("Draw! The Machine chose ", machine, "too")
    elif player == "rock":
        if machine == "paper":
            print ("You lost! The Machine chose 'paper'")
        else:
            print ("You Won! The Machine chose 'scissors'")
    elif player == "paper":
        if machine == "scissors":
            print ("You Lost! The Machine chose 'scissors'")
        else:
            print ("You Won! The Machine chose 'rock'")
    elif player == "scissors":
        if machine == "rock":
            print ("You Lost! The Machine chose 'rock'")
        else:
            print ("You Won! The Machine chose 'paper'")
    else:
        print ("Something went wrong.. Be sure to answer me only with 'rock', 'paper' or 'scissors'")
    print ()
    time.sleep(5)
    again = input("You wanna try again? (yes, no): ")
    if again == "yes":
        print ()
        player = False
        machine = gamelist[randint(0,2)]
    elif again == "no":
        print ()
        print ("Ok! Goodbye then!")
        time.sleep(2)
    else:
        print ()
        time.sleep(1)
        print ("Uh..")
        time.sleep(1)
        print ("Are you absolutely sure you told me what I need to?")
        time.sleep(3)
        print ()
        print ("Never mind.. Goodbye!")

# Written by Yasen Kostov
