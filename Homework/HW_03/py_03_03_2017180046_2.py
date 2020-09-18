import turtle

count = 0

while (count <= 5):
    turtle.penup()
    turtle.goto(count*60, 300)
    turtle.pendown()
    turtle.goto(count*60, 0)
    count = count + 1

for count in [0, 1, 2, 3, 4, 5]:
    turtle.penup()
    turtle.goto(0, count*60)
    turtle.pendown()
    turtle.goto(300, count*60)
    count = count + 1
    
turtle.exitonclick()

    
