from turtle import *


#step 1 square

speed(50)
width(7)
color("brown")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)    
left(90)
forward(200)
end_fill()

#step 2 door

left(90)
forward(80)
color("orange")
begin_fill()
left(90)
forward(60)
right(90)
forward(40)
right(90)
forward(60)
right(90)
forward(40)
end_fill()

#step 3 roof

penup()
goto(200, 200)
pendown()

color("blue")
begin_fill()
right(40)
forward(125)
left(77)
forward(131)
left(143)
forward(200)
end_fill()

#step 4 windows

#window 1

penup()       
goto(15, 20)
pendown()

color("yellow")
begin_fill()
left(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

#window 2

penup()       
goto(55, 150)
pendown()

color("yellow")
begin_fill()
left(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

#window 3

penup()       
goto(142, 110)
pendown()

color("yellow")
begin_fill()
left(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

#window 4
penup()       
goto(182, 60)
pendown()

color("yellow")
begin_fill()
left(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

#step 5 black bars


penup()       
goto(-300, -200)
pendown()

color("black")
forward(750)
left(90)
forward(660)
left(90)
forward(750)
left(90)
forward(660)

#step 6 ground

penup()       
goto(-299, -199)
pendown()

width("2")
color("green")
begin_fill()
left(90)
forward(750)
left(90)
forward(200)
left(90)
forward(750)
left(90)
forward(200)
end_fill()








exitonclick()