import turtle
my_turtle_cursor = turtle.Turtle()
my_turtle_screen = turtle.Screen()
def pause():
    my_turtle_cursor.speed(2)
    for i in range(100):
        my_turtle_cursor.left(90)
def write_coding_inside_heart():
    my_turtle_cursor.penup()
    my_turtle_cursor.goto(-240, 15)
    my_turtle_cursor.pencolor("#FFFFFF")
    my_turtle_cursor.write("Coding", font=("Helevetica", 50, "bold"))
def write_is_inside_heart():
    my_turtle_cursor.penup()
    my_turtle_cursor.goto(10, 15)
    my_turtle_cursor.pencolor("#FFFFFF")
    my_turtle_cursor.write("Is", font=("Helevetica", 54, "bold"))
def write_love_inside_heart():
    my_turtle_cursor.penup()
    my_turtle_cursor.goto(80, 15)
    my_turtle_cursor.pencolor("#FFFFFF")
    my_turtle_cursor.write("Love", font=("Helevetica", 54, "bold"))
def draw_complete_heart():
    my_turtle_cursor.fillcolor("#FF0000")
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.left(140)
    my_turtle_cursor.forward(294)
    draw_left_curve_of_heart()
    my_turtle_cursor.right(190)
    draw_right_curve_of_heart()
    my_turtle_cursor.forward(294)
    my_turtle_cursor.end_fill()
def draw_left_curve_of_heart():
    my_turtle_cursor.speed(50)
    for i in range(450):
        my_turtle_cursor.right(0.5)
        my_turtle_cursor.forward(1.2)
def draw_right_curve_of_heart():
    my_turtle_cursor.speed(100)
    for i in range(450):
        my_turtle_cursor.right(0.5)
        my_turtle_cursor.forward(1.2)
my_turtle_cursor.penup()
my_turtle_cursor.goto(0, -200)
my_turtle_cursor.pendown()
my_turtle_cursor.speed(50)
draw_complete_heart()
write_coding_inside_heart()
write_is_inside_heart()
write_love_inside_heart()
turtle.do
