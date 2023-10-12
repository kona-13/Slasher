# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:36:57 2023

@author: Steven
"""
import os
import random

#Putting my variables and shit at the top
ansY = ["y", "Y"]
ansN = ["n", "N"]
slasher = [0, 1, 2, 3, 4]

print("Slasher!")
print("A text based slasher game!")
print("Try to escape the house without getting killed - but beware, there is a slasher in here with you and you don't know when he'll strike...")
print()
print("Would you like to play? y/n")

start = input(">>")


def startofchoices():
    print("In the hallway there are 3 possible ways to go. Would you like to...")
    print("1.) Go left?")
    print("2.) Go straight?")
    print("3.) Go right?")
    choice1 = input(">>")
    
    if choice1 == "1":
        dooronleft1()
    elif choice1 == "2":
        doorstraightahead1()
    elif choice1 == "3":
        dooronright1()
    else:
        print("Choose an option.")
        startofchoices()
    
def slashergotyou():
    print("The slasher has got you. You have died.")
    print("Play again? y/n")
    playagain = input(">>")
    if playagain in ansY:
        startofchoices()
    else:
        os._exit(0)
        

def dooronleft1():
    print("You take the door on the left.")
    slasherhere = random.choice(slasher)
    if slasherhere == 1:
        slashergotyou() 
    print("You look around and there is nothing here.")
    print("You return to the hallway...")
    startofchoices()
    
    
def doorstraightahead1():
    print("You take the door straight ahead.")
    slasherhere = random.choice(slasher)
    if slasherhere == 1:
        slashergotyou()
    plschoose1()
    
def plschoose1():
    print("There are two doors in this room. Which one would you like to take?")
    print("1.) Straight ahead?")
    print("2.) Door on the left?")
    choice1 = input(">>")
    
    if choice1 == "1":
        straight2()
    elif choice1 == "2":
            left2()
    else:
        print("Please choese an option...")
        plschoose1()
        
    
def dooronright1():
    print("You take the door on the right.")
    slasherhere = random.choice(slasher)
    if slasherhere == 1:
        slashergotyou()
    print("There is nothing here...")
    print("You head back...")
    startofchoices()

def straight2():
    print("You take the door straight ahead.")
    slasherhere = random.choice(slasher)
    if slasherhere == 1:
        slashergotyou() 
    plschoose2()

def plschoose2():        
    print("You look around and there are 2 more doors. Would you like to go...")
    print("1.) Left?")
    print("2.) Right?")
    choice2 = input(">>")
    if choice2 == "1":
        left3()
    elif choice2 == "2":
        right3()
    else:
        print("Please choose an option...")
        plschoose2()

def right2():
    print("You reach a dead end...")
    print("You turn around...")
    slasherhere = random.choice(slasher)
    if slasherhere == 1:
        slashergotyou() 
    print("You return to the hallway...")
    startofchoices()
    
def left2():
    print("You reach a dead end...")
    print("You turn around...")
    slasherhere = random.choice(slasher)
    if slasherhere == 1:
        slashergotyou() 
    print("You return to the hallway...")
    startofchoices()
    
def left3():
    print("You arrive in a spacious room.")
    slasherhere = random.choice(slasher)
    if slasherhere == 1:
        slashergotyou() 
    plschoose3()

def plschoose3():
    print("You look around and see that there are 2 doors...")
    print("Would you like to...")
    print("1.) Go straight?")
    print("2.) Go right?")
    choice3 = input(">>")
    if choice3 == "1":
        straight3()
    elif choice3 == "2":
        right4()
    else:
       print("Please choose an option...")
       plschoose3()

def straight3(): #Dead end
    print("This is a dead end....")
    slasherhere = random.choice(slasher)
    if slasherhere == 1:
        slashergotyou() 
    print("You go back...")
    startofchoices()

def right4():
    print("You arrive in a rather cramped hallway with two doors.")
    print("You hear a noise and turn around...")
    slasherhere = random.choice(slasher)
    if slasherhere == 1:
        slashergotyou() 
    plschoose4()
        
def plschoose4():
    print("Must have been the wind....")
    print("Would you like to go...")
    print("1.) Left?")
    print("2.) Right?")
    choice4 = input(">>")
    if choice4 == "1":
        left4()
    elif choice4 == "2":
        right5()
    else:
        print("Please choose an option...")
        plschoose4()


def left4(): # Dead end
    print("You arrive at a dead end...")
    print("You hear the door slam!")
    print("You go to open the door...")
    slasherhere = random.choice(slasher)
    if slasherhere == 1:
        slashergotyou() 
    print("Must have been the wind...")
    print("You head back...")
    startofchoices()
    
def right5(): #Possible exit 1
    print("You find a open window!!")
    plschoose5()
        
def plschoose5():
    print("It looks like a way out. Would you like to go through it? y/n")
    leave1 = input(">>")
    if leave1 in ansY:
        print("You leave through the open window...")
        print("You are safe!")
        print()
        print("Thanks for playing!")
        goodbyelol()
    elif leave1 in ansN:
        print("You head back to look for a safer way out...")
        startofchoices()
    else:
        print("Please chose an option...")
        plschoose5()
        
def right3():
    print("You arrive at the bottom of a set of stairs...")
    print("You feel like you are being watched...")
    print("You turn around...")
    slasherhere = random.choice(slasher)
    if slasherhere == 1:
        slashergotyou()
    plschoose6()
    
def plschoose6():
    print("There was nothing there... Strange")
    print("Would you like to...")
    print("1.) Go up the stairs?")
    print("2.) Go back?")
    choice6 = input(">>")
    if choice6 == "1":
        upstairs()
    elif choice6 == "2":
        startofchoices()
    else:
        print("Please choose an option...")
        plschoose6()
    
def upstairs():
    print("You get to the top of the stairs")
    print("Something catches your eye...")
    slasherhere = random.choice(slasher)
    if slasherhere == 1:
        slashergotyou()
    print("It was just your shadow...")
    plschoose7()

def plschoose7():    
    print("At the top of the stairs you find 2 doors...")
    print("Would you like to go...")
    print("1.) Straight?")
    print("2.) Left?")
    choice7 = input(">>")
    if choice7 == "1":
        straight5()
    elif choice7 == "2":
        left5()
    else:
        print("Please choose an option...")
        plschoose7()

def left5():
    print("It is a dead end...")
    slasherhere = random.choice(slasher)
    if slasherhere == 1:
        slashergotyou()
    print("You head back...")
    plschoose7()

def straight5():
    print("You go straight...")
    slasherhere = random.choice(slasher)
    if slasherhere == 1:
        slashergotyou()
    plschoose8()


def plschoose8():
    print("Before you is 2 more doors...")
    print("Would you like to go....")
    print("1.) Right?")
    print("2.) Left?")
    choice8 = input(">>")
    if choice8 == "1":
        right6()
    elif choice8 == "2":
        left6()
    else:
        print("It was just your shadow...")
        plschoose8()
        
    
def left6():
    print("You slip and fall over...")
    print("You hear running towards you...")
    slashergotyou()
    
def right6(): #ending 2
    print("You reach an open window...")
    print("It looks like you can get out this way...")
    print("Would you like to go through it? y/n")
    leave2 = input(">>")
    if leave2 in ansY:
        print("You climb through the window and fall to the ground...")
        print("You landed rather awkwardly and are unable to move...")
        print("At least I am out of the house, you think to yourself...")
        print("You hear rusting in a nearby bush...")
        print("The rustling then turns to foot steps...")
        print("Something is approaching you - oh no!")
        print("...")
        print("...")
        gnomed()
    

def gamelogic():
    print("You look around the dark room and to the left of you is a door. Would you like to go through it? y/n")
    door1 = input(">>")
    if door1 in ansY:
        print("You go through the door and arrive in a long hallway.")
        startofchoices()
        
def gnomed():
    print("You've been GNOMED!")
    print("You win - idk how to finish this plot lol xD")
    print("Happy Halloween!!!!")
    print("Thanks for platying this little thing I made :) ") #if you didn't, then thanks for reading my code for whatever reason (I am sorry xD) 
    goodbyelol()
    

if start in ansY:
    gamelogic()
    
if start in ansN:
    os._exit(0)
    
def goodbyelol():
    os._exit(0)
