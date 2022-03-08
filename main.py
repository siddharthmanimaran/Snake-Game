from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score_Board

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
screen.listen()
food = Food()
score = Score_Board()

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.update_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_end()
        game = False
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game = False
            score.game_end()

screen.exitonclick()
