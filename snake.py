from turtle import Turtle

SNAKE_SPEED = 20
class Snake():
    
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]
        
    def create_snake(self):
        for x in range(3):
            self.add_segment()
            self.turtles[x].goto(x=x*-20,y=0)
        
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90) 
               

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)    
    
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)    
    
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)        

    def add_segment(self):
        new_turtle = Turtle(shape='square')
        new_turtle.penup()
        new_turtle.color('white')
        self.turtles.append(new_turtle)

    def extend(self):
        self.add_segment()
        self.turtles[-1].goto(self.turtles[-2].pos())
    
    def move(self):
        for snake_num in range(len(self.turtles)-1, 0, -1):
            new_x = self.turtles[snake_num-1].xcor()
            new_y = self.turtles[snake_num-1].ycor()
            
            self.turtles[snake_num].goto(new_x, new_y)
        self.head.forward(SNAKE_SPEED)
    
    def reset(self):
        for x in self.turtles:
            x.goto(-500, -500)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]