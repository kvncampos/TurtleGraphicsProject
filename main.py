import turtle
from turtle import Turtle, Screen, exitonclick
import random

# creating turtle pen
t = Turtle()
turtle.colormode(255)


# color = input("Change fill color: red, blue or green? ").lower().strip()
# square_size = int(input("How big do you want the square? "))
# # start the filling color
# t.begin_fill()
# t.fillcolor(color)
# # drawing the square of side s
# for _ in range(4):
#     t.forward(square_size)
#     t.right(90)
#
# # ending the filling of the color
# t.end_fill()


def draw_dot(space, x):
    """Space between dots, x is for how many dots per loop"""
    for i in range(x):
        for j in range(x):
            t.dot()

            t.forward(space)
        t.backward(space * x)

        t.right(90)
        t.forward(space)
        t.left(90)


# This is an example of Dotted Lines using Turtle
# t.shape("turtle")
# t.penup()
# draw_dot(10, 25)
# t.hideturtle()

def draw_dash(space, x):
    """Draws a dotted line, space for distance and x for Rows"""
    for i in range(x):
        for j in range(10):
            t.pendown()
            t.forward(space)
            t.penup()
            t.forward(space)

        t.backward(space * x * 10)

        t.right(90)
        t.forward(space)
        t.left(90)
    t.hideturtle()


def random_color():
    """Generate Random RGB Colors"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_rgb = (r, g, b)
    return random_rgb


def random_walk(distance):
    """Random  Generator of a Turtle Line"""
    distance = 40
    turn = [0, 90, 180, 270, 360]
    t.width(10)
    t.speed(10)
    direction = [1, 2]
    t.hideturtle()
    for _ in range(500):
        if t.xcor() == 200 or t.xcor() == -200:
            t.left(180)  # to turn back on x-axis#
        t.pencolor(random_color())
        turtle_move = random.choice(direction)
        if turtle_move == 1:
            t.forward(distance)
        elif turtle_move == 2:
            t.backward(distance)

        t.setheading(random.choice(turn))
    t.hideturtle()


def random_circle(size_of_circle):
    """Generate a random circle, add the size of circle you want"""
    t.width(2)
    t.speed("fastest")
    for x in range(38):
        t.color(random_color())
        t.pencolor(random_color())
        t.circle(size_of_circle)
        t.setheading(x * 10)
    t.hideturtle()


def main():
    screen = Screen()
    screen.setup(width=800, height=800)

    random_circle(50)
    exitonclick()


if __name__ == "__main__":
    main()
