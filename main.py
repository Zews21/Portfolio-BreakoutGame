from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from brick_manager import BrickManager
FONT = ("Courier", 20, "bold")


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)


ball = Ball()
paddle = Paddle((0, -250))
brick_manager = BrickManager()

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")


running = True
x_coord = -380
y_coord = 250
for n in range(0, 4):
    for i in range(0, 16):
        brick_manager.create_bricks(x_coord, y_coord)
        x_coord += 50
    y_coord -= 40
    x_coord = -380

while running:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() < -250:
        ball.reset_position()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(paddle) < 30 and ball.ycor() > -250:
        ball.bounce_y()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    for brick in brick_manager.all_bricks:
        if ball.distance(brick) < 30:
            ball.bounce_y()
            brick_manager.remove_brick(brick)
            if len(brick_manager.all_bricks) == 0:
                ball.hideturtle()
                ball.goto(0, 0)
                ball.write("YOU WIN", align="center", font=FONT)
                running = False


screen.exitonclick()
