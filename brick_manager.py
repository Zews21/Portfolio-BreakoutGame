from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class BrickManager:
    def __init__(self):
        self.all_bricks = []

    def create_bricks(self, x_coord, y_coord):
        new_brick = Turtle(shape="square")
        new_brick.shapesize(1, 2)
        new_brick.penup()
        new_brick.color(random.choice(COLORS))
        new_brick.goto(x_coord, y_coord)
        self.all_bricks.append(new_brick)

    def remove_brick(self, brick):
        brick.hideturtle()
        self.all_bricks.remove(brick)

