import turtle
s=turtle.Screen()
s.bgcolor("light blue")
w = turtle.Turtle()
w.pencolor("black")
w.fillcolor("red")
w.penup()
w.goto(-200,0)
w.pendown()
w.begin_fill()
#To draw a square
for i in range(4):
 w.forward(100)
 w.left(90)
w.penup()
w.goto(100,0)
w.pendown()
#To draw a square
for i in range(4):
 w.forward(100)
 w.left(90)
w.end_fill()
w.penup()
w.goto(-100,50)
w.pendown()
w.forward(200)
#To draw the arrow head
w.left(45)
w.backward(10)
w.forward(10)
w.right(90)
w.backward(10)
w.forward(10)
w.left(45)
#To write the text
w.penup()
w.goto(0,50)
w.pendown()
w.write("connect",align="center")
#w.hideturtle()
w.penup()
w.goto(-150,0)
w.pendown()
w.right(90)
w.pendown()
w.forward(200)
w.backward(200)
w.left(180)
w.left(45)
w.pensize(5)
w.backward(10)
w.forward(10)
w.right(90)
w.backward(10)
w.forward(10)
w.left(45)
w.right(90)

