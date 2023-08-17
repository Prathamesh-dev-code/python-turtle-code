import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]
yourName = turtle.textinput("Enter your name", "What is your name?")
for x in range(100):
    t.pencolor(colors[x%4])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(yourName, font = ("Arial", int( (x + 4) / 4), "bold"))
    t.left(92)
    t.speed(100)
