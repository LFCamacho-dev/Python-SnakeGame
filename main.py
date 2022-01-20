from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Python Game")
screen.tracer(0)

snake = Snake()
food = Food()

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

    # Detect collision
    if snake.head.distance(food) <= 15:
        food.refresh()

screen.exitonclick()
