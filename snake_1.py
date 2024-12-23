from turtle import Screen
from snake_2 import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake=Snake()
food=Food()
Score=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.change()
        snake.extend()
        Score.increase_score()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        Score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            Score.game_over()
screen.exitonclick()
