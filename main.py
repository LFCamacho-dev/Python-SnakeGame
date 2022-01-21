from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Python Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkeypress(key="Up", fun=snake.up)
screen.onkeypress(key="Down", fun=snake.down)
screen.onkeypress(key="Right", fun=snake.right)
screen.onkeypress(key="Left", fun=snake.left)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) <= 15:
        food.refresh()
        snake.extend()
        score.plus_one()

    # Detect collision with wall
    if (snake.head.xcor() > 280) or (snake.head.xcor() < -280) \
            or (snake.head.ycor() > 280) or (snake.head.ycor() < -280):
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
