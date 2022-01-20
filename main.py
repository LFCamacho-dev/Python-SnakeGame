import turtle
from turtle import Screen, Turtle


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Python Game")

turtle.speed(0)
turtle.penup()

number_of_squares = 3
starting_positions = (0, 0), (-20, 0), (-40, 0)

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    # new_segment.speed(0)
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    for seg in segments:
        seg.forward(20)













screen.exitonclick()