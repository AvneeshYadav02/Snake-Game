from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

food = Food()
my_score = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("SNAKE")
screen.tracer(0)

snake = Snake()

screen.onkey(fun=snake.up,key='Up')
screen.onkey(fun=snake.down,key='Down')
screen.onkey(fun=snake.left,key='Left')
screen.onkey(fun=snake.right,key='Right')
screen.listen()

score = Score()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    #Detect collision with Food
    if snake.head.distance(food) <= 15:
        food.refresh()
        score.score_up()
        snake.extend()
    
    #Detect collision with Wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score.reset()
        snake.reset()
        
    #Detect Collision with Tail
    for x in snake.turtles[1:]:
        if snake.head.distance(x) < 10:
            score.reset()
            snake.reset()
screen.exitonclick()