import turtle
from random import randint

size = 50
circles = 20
turtle.speed(100)
turtle.bgcolor('black')

turtle.color('black')

def move(length, angle):
                turtle.right(angle)
                turtle.forward(length)

def hex():
        turtle.pendown()
        turtle.color("#ffd230")
        turtle.begin_fill()
        for i in range(6):
                move(size,-60)
        turtle.end_fill()
        turtle.penup()

# start
turtle.penup()

for circle in range (circles):
        if circle == 0:
                hex()
                move(size,-60)
                move(size,-60)
                move(size,-60)
                move(0,180)
        for i in range (6):
                move(0,60)
                for j in range (circle+1):
                        hex()
                        move(size,-60)
                        move(size,60)
                move(-size,0)
        move(-size,60)
        move(size,-120)
        move(0,60)

turtle.exitonclick()
