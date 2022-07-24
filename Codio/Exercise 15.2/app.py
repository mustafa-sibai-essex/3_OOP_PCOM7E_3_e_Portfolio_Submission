import copy
from turtle import *
from Rectangle import *


def draw_rect(turtleObj: Turtle, rectangle: Rectangle):
    rect = copy.deepcopy(rectangle)

    turtleObj.color("red")
    turtleObj.hideturtle()
    turtleObj.penup()
    turtleObj.setposition(rect.topLeftCorner.x, rect.topLeftCorner.y)
    turtleObj.speed(1)
    turtleObj.showturtle()
    turtleObj.pendown()
    turtleObj.goto(rect.topRightCorner.x, rect.topRightCorner.y)
    turtleObj.setheading(-90)
    turtleObj.goto(rect.bottomRightCorner.x, rect.bottomRightCorner.y)
    turtleObj.setheading(-180)
    turtleObj.goto(rect.bottomLeftCorner.x, rect.bottomLeftCorner.y)
    turtleObj.setheading(-270)
    turtleObj.goto(rect.topLeftCorner.x, rect.topLeftCorner.y)
    turtleObj.setheading(0)


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")

my_turtle = Turtle("turtle")
rect = Rectangle(Point(50, 100), Point(200, 300))

draw_rect(my_turtle, rect)

exitonclick()
