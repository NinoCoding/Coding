import turtle

turtle.speed(10)

#quadrado
turtle.fillcolor('orange')
turtle.begin_fill()
for x in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

turtle.penup()
turtle.forward(100)
turtle.pendown()

#retangulo
turtle.fillcolor('yellow')
turtle.begin_fill()
for x in range(2):
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

turtle.penup()
turtle.left(90)
turtle.forward(100)
turtle.pendown()

#triangulo
turtle.fillcolor('pink')
turtle.begin_fill()
for x in range(3):
    turtle.left(30)
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

turtle.penup()
turtle.right(90)
turtle.forward(200)
turtle.pendown()

turtle.left(120)

#trapezio
turtle.fillcolor('red')
turtle.begin_fill()
for x in range(2):
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
turtle.end_fill()


#porta
turtle.penup()
turtle.goto(25, 0)
turtle.pendown()

turtle.right(150)

turtle.fillcolor('black')
turtle.begin_fill()
for x in range(2):
    turtle.forward(50)  
    turtle.right(90)
    turtle.forward(50)  
    turtle.right(90)
turtle.end_fill()

#janelas 1
turtle.penup()
turtle.goto(80, 25)
turtle.right(90)
turtle.forward(50)
turtle.pendown()

turtle.fillcolor('black')
turtle.begin_fill()
for x in range(4):
    turtle.forward(25)
    turtle.left(90)
turtle.end_fill()

turtle.speed(1)

#janelas 2
turtle.penup()
turtle.goto(160, 25)
turtle.forward(50)
turtle.pendown()

turtle.fillcolor('black')
turtle.begin_fill()
for x in range(4):
    turtle.forward(25)
    turtle.left(90)
turtle.end_fill()