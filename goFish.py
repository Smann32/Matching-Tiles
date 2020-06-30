#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 00:06:47 2020
@author: Dr. Z
Creates a turtle that moves to the location of a mouse click
"""
#Modified from https://keepthinkup.wordpress.com/programming/python/python-turtle-handling-with-mouse-click/

import turtle
import tkinter
import random
w = 1080
h = 720
turtle.setup(w,h) # sets up screen size and turns on listener ***REQUIRED***
window = turtle.Screen() # create our Screen variable
window.clear()
window.title("Go Fish!")
window.bgcolor("lightblue")
window.setworldcoordinates(0, w, h, 0)
# Create our turle variable
button = turtle.Turtle(shape = "square") 
size = 10
button.shapesize(size)

"""
Define a class that will create 'card' objects
each card should hold a unique identifier
    each card should have a unique value
    each card should have a unique position
-------------------------------------------------
When you generate a card object:
    It shall be given a random color
    and a definite position.

    let position = [1,2,3]
    0 <= value <= 2
    
Create 3 buttons with turtle:
    A = cardOne
    B = cardTwo
    C = cardThree

now A - C shares all attributes of cardOne - cardThree

-------------------------------------------------

Now create a 2nd round of cards and append them to new list

    can use same class myCard:
    create different randomVal function for second set of cards

Create 3 more buttons with turtle:
    D = cardFour
    E = cardFive
    F = cardSix
    
now D - F share attributes of cardFour - cardFive
-------------------------------------------------
:::::::::::::handling the match checking piece:::::::::::::
    
    When user clicks a button -> store those attributes in new array
    doesItMatch[0]
    
    When user clicks 2nd button -> store those attributes in doesItMatch[1]
    
    if doesItMatch.length = 2:
        compareCards()
    def compareCards():
        if doesItMatch[0].val = doesItMatch[1].val
            print("its a match")
            score + 1
            delete clicked cards
        else
            print("go fish")
    if score == 2:
        score + 1
        print("Theres only one set left, you won")    
        exit()
"""

class myCard:
    
    
    def __init__(self,val,xCor,yCor):
        self.val = val
        self.xCor = xCor
        self.yCor = yCor
"""
::::::Create Cards::::::::::

"""

card = [] #top row of cards get appended here
matchCard = [] #bottom row of cards get appended here
doesItMatch = [] # use to compare two clicked cards




   

randomVal = random.sample(range(0,3), 3)# create 3 card objects, and give them random but not equal values
 
cardOne = myCard(randomVal[0],w/6,h/4)
card.append(cardOne)# append each object to the card array
cardTwo = myCard(randomVal[1],2*w/6,h/4)
card.append(cardTwo)
cardThree = myCard(randomVal[2],3*w/6,h/4)
card.append(cardThree)


A = cardOne
B = cardTwo
C = cardThree

matchVal = random.sample(range(0,3), 3)
cardFour = myCard(matchVal[0],w/6,3*h/4)
cardFive = myCard(matchVal[1],2*w/6,3*h/4)
cardSix  = myCard(matchVal[2],3*w/6,3*h/4)
matchCard.append(cardFour)
matchCard.append(cardFive)
matchCard.append(cardSix)


D = cardFour
E = cardFive
F = cardSix
"""
::::::End Create Cards::::::::::

"""
 

"""
::::::Create Buttons::::::::::

"""
style = ('Courier', 30, 'italic')
button.hideturtle()
for i in range(3):
    button.penup()
    button.color('black')
    button.goto((i+1)*w/6,h/4)
    button.stamp()
    button.goto((i+1)*w/6, 3*h/4)
    button.stamp()
    
for i in range(3):
    button.penup()
    button.color('magenta')
    button.goto((i+1)*w/6,h/4)
    button.write('Click', font = style, align = 'center')
    button.goto((i+1)*w/6, 3*h/4)    
    button.write('Click', font = style, align = 'center')

"""
onclick(logCardClick)

def logCardClick():
    get x/y coordinate
    if x cord & y cord = card[0].xCor & card[0].yCor:
        doesItMatch.append(A)
        match +=
    if x cord & y cord = card[1].xCor & card[1].yCor:
        doesItMatch.append(B)
        match +=
    if x cord & y cord = card[2].xCor & card[2].yCor:
        doesItMatch.append(C)
        match +=
    if x cord & y cord = matchCard[0].xCor & matchCard[0].yCor:
        doesItMatch.append(D)
        match +=
    if x cord & y cord = matchCard[1].xCor & matchCard[1].yCor:
        doesItMatch.append(E)
        match +=
    if x cord & y cord = matchCard[2].xCor & matchCard[2].yCor:
        doesItMatch.append(F)
        match +=
    if score == 2:
        compareCards()
def compareCards():
    if doesItMatch[0].val == doesItMatch[1].val:
        score +=
    if score == 2:
        button.goto(w/2,h/2)
        button.write("you win", font = style, align='center')
        exit()
""" 





