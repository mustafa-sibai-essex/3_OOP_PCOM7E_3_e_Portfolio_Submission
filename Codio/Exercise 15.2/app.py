import copy
from turtle import *
from Rectangle import *


def draw_rect(turtle_obj: Turtle, rectangle: Rectangle):
    rect = copy.deepcopy(rectangle)

    turtle_obj.color("red")
    turtle_obj.hideturtle()
    turtle_obj.penup()
    turtle_obj.setposition(rect.topLeftCorner.x, rect.topLeftCorner.y)
    turtle_obj.speed(1)
    turtle_obj.showturtle()
    turtle_obj.pendown()
    turtle_obj.goto(rect.topRightCorner.x, rect.topRightCorner.y)
    turtle_obj.setheading(-90)
    turtle_obj.goto(rect.bottomRightCorner.x, rect.bottomRightCorner.y)
    turtle_obj.setheading(-180)
    turtle_obj.goto(rect.bottomLeftCorner.x, rect.bottomLeftCorner.y)
    turtle_obj.setheading(-270)
    turtle_obj.goto(rect.topLeftCorner.x, rect.topLeftCorner.y)
    turtle_obj.setheading(0)


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")

my_turtle = Turtle("turtle")
rect = Rectangle(Point(50, 100), Point(200, 300))

draw_rect(my_turtle, rect)

exitonclick()
