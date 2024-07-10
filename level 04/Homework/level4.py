#drawing castle

from turtle import *

speed(100)
penup()
goto(-500, -300)
pendown()

#drawing sky
width(2)
color("skyblue")
begin_fill()
forward(1000)
left(90)
forward(1000)
left(90)
forward(1000)
left(90)
forward(1000)
end_fill()

#drawing ground

color("green")
begin_fill()
forward(100)
left(90)
forward(1000)
left(90)
forward(100)
left(90)
forward(1000)
end_fill()

#drawing sun and clouds
speed(100)
penup()
goto(-400, 300)
fillcolor("yellow")
begin_fill()
circle(80)
end_fill()

penup()
goto(-300, 200)
import turtle as t
t.Screen().bgcolor("lightblue")

def filled_circle(radius, color):
    t.color(color,color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


radius = 20
cloud_color="white"

filled_circle(radius,cloud_color)
t.forward(radius)
filled_circle(radius,cloud_color)
t.right(90)
filled_circle(radius,cloud_color)
t.right(90)
filled_circle(radius,cloud_color)
t.right(90)
filled_circle(radius,cloud_color)
t.right(90)


penup()
goto(-200, 300) 
import turtle as t
t.Screen().bgcolor("lightblue")

def filled_circle(radius, color):
    t.color(color,color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


radius = 30
cloud_color="white"

filled_circle(radius,cloud_color)
t.forward(radius)
filled_circle(radius,cloud_color)
t.right(90)
filled_circle(radius,cloud_color)
t.right(90)
filled_circle(radius,cloud_color)
t.right(90)
filled_circle(radius,cloud_color)
t.right(90)

penup()
goto(0, 250) 
import turtle as t
t.Screen().bgcolor("lightblue")

def filled_circle(radius, color):
    t.color(color,color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


radius = 25
cloud_color="white"

filled_circle(radius,cloud_color)
t.forward(radius)
filled_circle(radius,cloud_color)
t.right(90)
filled_circle(radius,cloud_color)
t.right(90)
filled_circle(radius,cloud_color)
t.right(90)
filled_circle(radius,cloud_color)
t.right(90)

penup()
goto(300, 250) 
import turtle as t
t.Screen().bgcolor("lightblue")

def filled_circle(radius, color):
    t.color(color,color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


radius = 35
cloud_color="white"

filled_circle(radius,cloud_color)
t.forward(radius)
filled_circle(radius,cloud_color)
t.right(90)
filled_circle(radius,cloud_color)
t.right(90)
filled_circle(radius,cloud_color)
t.right(90)
filled_circle(radius,cloud_color)
t.right(90)

#drawing castle

penup()
goto(-500, -300)
pendown()

color("green")
begin_fill()
right(180)
forward(100)
color("gray")
left(90)
forward(400)
right(90)
forward(150)
right(90)
forward(400)
right(90)
forward(150)


goto(-250, -300)
right(90)
forward(200)
right(90)
forward(500)
right(90)
forward(200)
right(90)
forward(500)

right(180)
forward(500)
left(90)
forward(400)
right(90)
forward(150)
right(90)
forward(400)
end_fill()

begin_fill()
right(90)
forward(500)
right(90)
forward(450)
right(90)
forward(200)
right(90)
forward(450)
right(90)
forward(200)

end_fill()

#drawing roofs

#1 roof

forward(300)
right(90)
forward(400)
left(90)
color("purple")
begin_fill()
forward(25)
right(90)
forward(0)
right(50)
forward(130)
right(80)
forward(130)
right(140)
forward(190)
end_fill()

#2 roof


right(180)
forward(160)
right(90)
color("gray")
forward(200)
left(90)
forward(155)
left(90)
forward(250)
color("purple")
begin_fill()
left(90)
forward(25)
right(90)
forward(0)
right(50)
forward(165)
right(80)
forward(165)
right(140)
forward(190)
end_fill()

#3 roof
right(180)
forward(185)
color("skyblue")
forward(120)
right(90)
forward(50)
left(90)
forward(10)
color("purple")
left(180)
begin_fill()
forward(25)
right(90)
forward(0)
right(50)
forward(130)
right(80)
forward(130)
right(140)
forward(190)
end_fill()

#drawing windows and the door
color("skyblue")
left(90)
forward(200)
color("gray")
right(90)
forward(140)
color("gray")
left(90)
forward(200)
right(90)
forward(160)
color("DarkSlateGray")
begin_fill()
right(90)
forward(100)
right(90)
forward(125)
right(90)
forward(100)
right(90)
forward(125)
end_fill()

#windows 
#1 

right(180)
forward(40)
left(90)
forward(100)
color("gray")
forward(300)
color("DarkSlateGray")
begin_fill()
right(90)
forward(45)
right(90)
forward(60)
right(90)
forward(45)
right(90)
forward(60)
end_fill()

#window 2
left(180)
color("gray")
forward(200)
right(90)
forward(320)
right(90)
forward(130)
color("DarkSlateGray")
begin_fill()
right(90)
forward(40)
right(90)
forward(60)
right(90)
forward(40)
end_fill()

#window 3
right(180)
color("gray")
forward(95)
color("skyblue")
forward(145)
color("gray")
forward(205)
left(90)
forward(60)
right(90)
color("skyblue")
forward(150)
color("gray")
forward(50)
color("DarkSlateGray")
begin_fill()
right(90)
forward(60)
left(90)
forward(40)
left(90)
forward(60)
end_fill()

#create flag
penup()
goto(0, 255)
pendown()

forward(70)
right(90)
color("green")
begin_fill()
forward(130)
right(90)
forward(60)
right(90)
forward(130)
right(90)
forward(60)
end_fill()
exitonclick()

