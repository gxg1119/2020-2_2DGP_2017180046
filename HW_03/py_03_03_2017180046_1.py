import turtle

count=0

def H(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(x,y-50)
    turtle.penup()
    turtle.goto(x-100, y-50)
    turtle.pendown()
    turtle.goto(x+100, y-50)
    turtle.penup()
    turtle.goto(x, y-70)
    turtle.left(180)
    turtle.pendown()
    turtle.circle(50)

    
def T(x,y):
    for count in [0,1,2]:
         turtle.penup()
         turtle.goto(x,y-(100*count))
         turtle.pendown()
         turtle.forward(100)
         
         count = count+1

    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x,y-200)
    
         
def E(x,y):
    for count in [0, 1]:
        turtle.penup()
        turtle.goto(x+(70*count),y)
        turtle.pendown()
        turtle.goto(x+(70*count),y-200)
        count = count +1
        
    turtle.penup()
    turtle.goto(x, y-100)
    turtle.pendown()
    turtle.forward(70)


def Yeo(x,y):
    for count in[0,1]:
        turtle.penup()
        turtle.goto(x,y-(50*count))
        turtle.pendown()
        turtle.goto(x-50,y-(50*count))
        count = count +1

    turtle.penup()
    turtle.goto(x,y+50)
    turtle.pendown()
    turtle.goto(x, y-100)

def N(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x,y-100)
    turtle.goto(x+100,y-100)

H(-300,200)
turtle.left(180)
H(-300,0)
turtle.left(180)
T(-150,100)
E(20, 100)
H(250,200)
Yeo(400,100)
N(250,0)

turtle.exitonclick()


