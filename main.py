import turtle

window = turtle.Screen()
window.bgcolor("white")
window.setup(width=600, height=600)

border = turtle.Turtle()
border.penup()
border.goto(-100, -100)
border.pendown()
border.pensize(3)
for _ in range(4):
    border.forward(200)
    border.left(90)
border.hideturtle()

arrow = turtle.Turtle()
arrow.shape("turtle")
arrow.color("yellow")
arrow.penup()
arrow.speed(0)
arrow.goto(0, 0)
arrow.dx = 3  # Aumentar velocidad en el eje x
arrow.dy = 2  # Diferente velocidad en el eje y para variar el movimiento

def move_arrow():
    x, y = arrow.xcor(), arrow.ycor()
    
    if x + arrow.dx > 100 or x + arrow.dx < -100:
        arrow.dx *= -1
    if y + arrow.dy > 100 or y + arrow.dy < -100:
        arrow.dy *= -1
    
    arrow.setx(x + arrow.dx)
    arrow.sety(y + arrow.dy)
    
    window.ontimer(move_arrow, 10)

move_arrow()

turtle.mainloop()


