#Miguel Tarazona 
#Final Project
#The purpose: To create paint
#Professor: 2022-12-07

#importing the library turtle and random 
import turtle 
from turtle import Turtle, Screen
import random

#The window size, the colour of the screen and the title 
canvas = turtle.Screen()
canvas.title(" Miguel's Paint ")
canvas.bgcolor("snow")
canvas.setup(width = 800, height = 800)

#Creating the icon of the pen which will be a turtle 
turtle_icon = Turtle("turtle")
turtle_icon.width(3)
turtle_icon.speed(-1)

#All of the 8 colours used in this program
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'black']


