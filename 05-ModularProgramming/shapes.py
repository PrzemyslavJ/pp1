import turtle

def drawSquare(x,y,n):
    Square = turtle.Turtle()
    Square.penup()
    Square.setposition(x,y)
    Square.pendown()
    for i in range(4):
        Square.forward(n)
        Square.setheading(270-i*90)

    Square.hideturtle()

def drawCircle(x,y,r):
    Circle = turtle.Turtle()
    Circle.penup()
    Circle.setposition(x,y)
    Circle.pendown()
    Circle.circle(r)

def Triangle(x,y,m):
    Triangle = turtle.Turtle()
    Triangle.penup()
    Triangle.setposition(x,y)
    Triangle.pendown()
    for i in range(3):
        Triangle.forward(m)
        Triangle.left(120)

def drawStar(x,y,n):
    Star = turtle.Turtle()
    Star.penup()
    Star.setposition(x,y)
    Star.pendown()
    for i in range(5):
        Star.forward(n)
        Star.right(144)
        Star.forward(n)
        Star.left(72) 
    
def drawFillSquare(x,y,n):
    Square = turtle.Turtle()
    Square.penup()
    Square.setposition(x,y)
    Square.pendown()
    Square.fillcolor('black')
    Square.begin_fill()
    for i in range(4):
        Square.forward(n)
        Square.setheading(270-i*90)
    Square.end_fill()

def CheesBoard(x,y,m):
    board = turtle.Turtle()
    board.fillcolor('black')
    for i in range(4):
        for j in range(4):
            board.penup() 
            board.setposition(x+j*m,y-i*m)
            board.pendown()
            if(j==i or j==i+2 or j==i-2):
                board.begin_fill()
                for k in range(4):
                    board.forward(m)
                    board.setheading(270-k*90)
                board.end_fill()
            else:
                for k in range(4):
                    board.forward(m)
                    board.setheading(270-k*90)

    board.hideturtle()
    
                    
CheesBoard(10,10,50)
    

    
