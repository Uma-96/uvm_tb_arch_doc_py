import turtle
s=turtle.Screen()
s.bgcolor("light blue")
w = turtle.Turtle()
w.pencolor("black")
w.fillcolor("red")
w.penup()
w.goto(-200,50)
w.pendown()
w.begin_fill()
#To draw a square
for i in range(4):
 w.forward(100)
 w.left(90)
w.penup()
w.goto(-50,0)
w.pendown()
#To draw a square
for i in range(4):
 w.left(90)
 w.forward(200)
w.end_fill()

