import turtle
import time
import snake
import score
from food import Food

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)
position = [(0, 0), (-20, 0), (-40, 0)]

new_snake = snake.Snake()
food = Food()
score = score.Score()
screen.update()


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    screen.listen()
    screen.onkey(new_snake.left,'a')
    screen.onkey(new_snake.right,'d')

    new_snake.move()
    if new_snake.squares[0].distance(food) < 15:
        food.refresh()
        new_snake.grow()
        score.update()
    if new_snake.squares[0].xcor() > 300 or new_snake.squares[0].xcor() < -300 or new_snake.squares[0].ycor() > 300 or new_snake.squares[0].ycor() < -300:
        game_is_on = False
    for segment in new_snake.squares:
        if segment == new_snake.squares[0]:
            pass
        elif new_snake.squares[0].distance(segment) < 5:
            game_is_on = False
gameover = turtle.Turtle()
gameover.color('white')
gameover.write("GAME OVER", align="center", font=('Arial', 20, 'normal'))
gameover.hideturtle()



screen.exitonclick()
