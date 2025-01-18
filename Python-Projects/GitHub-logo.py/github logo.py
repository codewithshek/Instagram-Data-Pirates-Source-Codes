from turtle import *
speed(0)
fillcolor('#211F1F')
begin_fill()
circle(100)
end_fill()
penup()
goto(25,150)
left(170)
pendown()
pencolor('white')
fillcolor('white')
begin_fill()
# head upper part
for i in range(95):
    forward(0.5)
    left(0.2)

# head left part
for i in range(30):
    forward(1)
    left(1)
for i in range(24):
    forward(0.5)
    left(1)
for i in range(17):
    forward(1)
    left(1)
for i in range(17):
    forward(1.7)
    left(0.6)
for i in range(25):
    left(1)
    forward(0.5)
for i in range(24):
    left(1)
    forward(0.5)
for i in range(30):
    left(1)
    forward(1)

# left side of the body
right(125)
for i in range(70):
    forward(0.2)
    left(0.55)
for i in range(58):
    forward(0.5)
    left(0.2)
for i in range(30):
    forward(0.3)
    right(8)
penup()
right(30)
forward(74)
right(90)
forward(10)
left(177)

# righ part of the body
pendown()

forward(6)
for i in range(58):
    left(0.2)
    forward(0.5)
for i in range(70):
    forward(0.2)
    left(0.55)

# head right part
right(125)
for i in range(30):
    forward(1)
    left(1)
for i in range(24):
    forward(0.5)
    left(1)
for i in range(25):
    forward(0.5)
    left(1)
for i in range(17):
    left(0.6)
    forward(1.7)
for i in range(17):
    left(1)
    forward(1)
for i in range(24):
    left(1)
    forward(0.5)
for i in range(30):
    forward(1)
    left(1)
end_fill()
penup()
left(90)
forward(210)
pendown()
fillcolor('white')
begin_fill()
left(90)
circle(45)
end_fill()
penup()
left(110)
forward(97)
right(110)
left(180)
forward(5)
pendown()
fillcolor('white')
begin_fill()
for i in range(35):
    forward(0.5)
    right(1.5)
for i in range(30):
    forward(0.5)
    left(1.5)
for i in range(50):
    forward(0.1)
    left(3)
for i in range(20):
    forward(1)
    right(1)
for i in range(30):
    forward(1)
    left(4)
end_fill()
penup()
forward(127)
pendown()
fillcolor('white')
begin_fill()
for i in range(250):
    forward(0.1)
    left(0.2)
left(70)
for i in range(282):
    left(0.2)
    forward(0.1)
end_fill()
penup()
right(50)
forward(50)
right(60)
pendown()
fillcolor('white')
begin_fill()
for i in range(250):
    forward(0.1)
    left(0.2)
left(70)
for i in range(280):
    left(0.2)
    forward(0.1)
end_fill()
hideturtle()
done()