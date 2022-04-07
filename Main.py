'''
Created on Apr 1, 2022
@author: Tobey Bill, Max Kemper, Marcos Leal, Jose Andres Castillo
'''

import turtle
from turtle import Turtle, Screen, Shape
from tkinter import PhotoImage

from random import seed, randint

import math
from math import sqrt

win = turtle.Screen()
win.bgcolor("white")
win.title("Points")
pen = turtle.Turtle()
pen.color("black")
pen.pensize(10)
pen.speed(1)

text = turtle.Turtle()
text.color("black")
text.speed(10)
text.penup()
text.hideturtle()
text.goto(0, 280)

rate = turtle.Turtle()
rate.speed(10)
rate.penup()
rate.hideturtle()
rate.goto(-260, 280)
rate.color("black")
style = ('Arial', 20, 'bold')

x = [0, 0, 0]
y = [0, 0, 0]
costPerPixel = 0.058
totalCost = 0

rate.write("Rate: {}/mile".format(costPerPixel), font = style, align = 'center')

def drawPath():
    global x, y
    
    for i in range(3):
        x[i] = randint(-300, 300)
        y[i] = randint(-300, 250)
        pen.penup()
        pen.goto(x[i], y[i])
        pen.pendown()
        pen.forward(1)

    pen.penup()
    pen.goto(x[0], y[0])
    pen.pensize(4)
    pen.pendown()
    
    for i in range(3):
        pen.goto(x[i], y[i])

def moveCar():
    global x, y, totalCost
    pen.penup()
    pen.goto(x[0], y[0])
    
    larger = PhotoImage(file="car.gif").subsample(4, 4)
    win.addshape("smallCar", Shape("image", larger))
    pen.shape("smallCar")
    
    for i in range(3):
        pen.goto(x[i], y[i])
        if i > 0 and i < 3:
            distance = round(sqrt((x[i]-x[i-1])**2+(y[i]-y[i-1])**2), 2)
            totalCost += distance * costPerPixel
            costsTable(i)
        
        
def costsTable(i):
    text.pendown()
    text.clear()
    style = ('Arial', 20, 'bold')
    text.write("Total Cost After Trip {}: ${}".format(i, round(totalCost, 2)), font = style, align = 'center')

drawPath()
moveCar()
win.exitonclick()