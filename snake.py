from turtle import Screen, Turtle
import time

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake = []
        self.move_dist = 20
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        ozle = Turtle("square")
        ozle.color("white")
        ozle.penup()
        ozle.goto(position)
        self.snake.append(ozle)

    def reset(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def extend(self):
        # Add new segment to the snake
        self.add_segment(self.snake[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        # On this code below, for loop goes backward. It started from the end and moves to the start.
        # Input in range represents (start=, stop=, step=)
        for ozl_num in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[ozl_num - 1].xcor()
            new_y = self.snake[ozl_num - 1].ycor()
            self.snake[ozl_num].goto(new_x, new_y)
            # With this for loop, snake's tail follows the previous part of the tail.
        self.head.forward(self.move_dist)
