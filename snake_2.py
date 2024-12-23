from turtle import Turtle
positions=[(0,0),(-20,0),(-40,0)]
distance=20
Up=90
Down=270
Left=180
Right=0
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for position in positions:
            self.add(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(distance)
    def up(self):
        if self.head.heading()!=Down:
            self.head.setheading(Up)

    def down(self):
        if self.head.heading()!=Up:
         self.head.setheading(Down)

    def right(self):
        if self.head.heading()!=Left:
            self.head.setheading(Right)
    def left(self):
        if self.head.heading()!=Right:
            self.head.setheading(Left)

    def add(self,position):
        snake = Turtle("square")
        snake.color("grey")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add(self.segments[-1].position())