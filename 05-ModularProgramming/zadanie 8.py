import turtle

x = int(input('Podaj współrzędną x: '))
y = int(input('Podaj współrzędną y: '))
n = int(input('Podaj bok n: '))
pen = turtle.Turtle()
def smallSquare(n):
    for m in range(0,4):
        pen.forward(n/4)
        pen.right(90)
def move(n):
    pen.right(90)
    pen.forward(n/4)
    pen.right(90)
    pen.forward(n)
    pen.right(180)
def drawSquare(x,y,n):
    turtle.penup()
    turtle.setpos(x,y)
    turtle.pendown()
    for i in range(0,4):
        pen.forward(n)
        pen.right(90)
    for m in range(0,4):
        for i in range(0,4):
            smallSquare(n)
            pen.forward(n/4)
        move(n)
    
        

drawSquare(x,y,n)