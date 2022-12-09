#Miguel Tarazona 
#Final Project
#The purpose: To create paint
#Professor: 2022-12-07
#Due Date: 2022-12-10
#Reference link #1: https://docs.python.org/3/library/turtle.html  
#Reference link #2: https://youtu.be/YdkcpdMifpA  

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
    style = ('Courier', 10, 'bold')
    turtle_icon.color("black")
    turtle_icon.penup()
    turtle_icon.setpos(-350, 200)
    turtle_icon.write("Click to move the mouse and drag to draw. Right-click to clear.", font=style)
    turtle_icon.setpos(-350, 180)
    turtle_icon.write("Press 'c' to change colour, 's' to stamp, and use the arorow keys to draw a straight line", font=style)
  
    #The texture of the pen
    turtle_icon.color(current_colour)
    turtle_icon.setpos(x, y)
    turtle_icon.write("" + str(current_colour), font=style)#For the current colour dipslay it's name 
    turtle_icon.pendown()

#The purpose of this function is to change colours from the list above randomly
def change_colour():
    random_colour = random.choice(colours)
    colour1 = (random_colour, random_colour)
    colour2 = turtle_icon.color()

    while colour1 == colour2:
        random_colour = random.choice(colours)
        colour1 = (random_colour, random_colour)
        colour2 = turtle_icon.color()

#The colour will be changed to a random colour 
    turtle_icon.color(random_colour)
    current_colour = random_colour
    message(current_colour, turtle_icon.xcor(), turtle_icon.ycor())

#THe purpose of this funbction is when the user presses the key word s it will stamp
def stamp():
    turtle_icon.stamp()

#Creating the directions and speed of the turtle pen
def up():#The speed of how fast the pen will go when going up
    turtle_icon.seth(90)
    turtle_icon.forward(100)


def down():#The speed of how fast the pen will go when going doown
    turtle_icon.seth(270)
    turtle_icon.forward(100)

def left():#The speed of how fast the pen will go to the left
    turtle_icon.seth(180)
    turtle_icon.forward(100)

def right():#The speed of how fast the pen will go to the right 
    turtle_icon.seth(0)
    turtle_icon.forward(100)

#The dragging begins start the drawing
def drag(x, y):
    turtle_icon.pendown()
    turtle_icon.ondrag(None)
    turtle_icon.seth(turtle_icon.towards(x, y))
    turtle_icon.goto(x, y)
    turtle_icon.ondrag(drag)

#when the user right clicks it will clear the screen and start over
def clear_screen(x, y):
    turtle_icon.clear()
    message(current_colour, turtle_icon.xcor(), turtle_icon.ycor())

#When the user uses the left click on the mouse to drag then the pen will start drawing
def draw_screen(x,y):
    turtle_icon.penup()
    turtle_icon.setpos(x, y)
    turtle_icon.pendown()


def main():
#The pen will draw something when dragged while holding the left click
# THe screen will clear if the user right clicks only once    
    turtle.listen()
    turtle_icon.ondrag(drag)
    turtle.onscreenclick(draw_screen, 1)
    turtle.onscreenclick(clear_screen, 3)

#Key arrows and keywords to do two other things when drawing
    turtle.onkey(up, 'Up')#The pen will go up in a staright line if the key arrow up is pressed
    turtle.onkey(down, 'Down')#The pen will go down in a staright line
    turtle.onkey(left, 'Left')#A straight line will drawn to the left 
    turtle.onkey(right, 'Right')#right straight line when the right key arrow is pressed
    turtle.onkey(change_colour, 'c')#The colour will change when the user presses the keyword c
    turtle.onkey(stamp, 's')#There will be a stamp if the user presses the keyword s

    canvas.mainloop()

#The colour of the turtle icon will start as black 
current_colour = "black"
message(current_colour, turtle_icon.xcor(), turtle_icon.ycor())
main()#Calling the function



















