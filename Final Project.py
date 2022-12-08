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

#An introduction to the user and a guide on how to use paint
def message(current_colour, x, y):
    letter_style = ('Courier', 10, 'bold')
    turtle_icon.color("black")
    turtle_icon.penup()
    turtle.setpos(-350, 350)
    turtle_icon.write("Click to move the mouse and drag to draw. Right-click to clear.", font=letter_style)
    turtle_icon.setpos(-350, 320)
    turtle_icon.write("Press 'c' to change colour, 's' to stamp, and use the arorow keys to draw a straight line", font=letter_style)
  
    #The texture of the pen
    turtle_icon.color(current_colour)
    turtle_icon.write("" + str(current_colour), font=letter_style)#For the current colour dipslay it's name 
    turtle_icon.pendown()

#The purpose of this function is to change colours from the list above randomly


