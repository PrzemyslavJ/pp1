import turtle

def drawSquare(x,y,n):
    Square = turtle.Turtle()
    Square.penup()
    Square.setposition(x,y)
    Square.pendown()
    for i in range(4):
        Square.forward(n)
        Square.setheading(270-i*90)

def drawStructure(x,y,n):
    Structure = turtle.Turtle()
    for i in range(4):
        for j in range(4):
            Structure.penup() 
            Structure.setposition(x+j*n,y-i*n)
            Structure.pendown()
            for k in range(4):
                Structure.forward(n)
                Structure.setheading(270-k*90)
                   
      
        
drawStructure(10,10,30)
