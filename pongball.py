from turtle import Turtle


#The 'Ball' class will inherent all the attribute and methods from the parent Turtle class
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        #All of these methods are inherited from the 'Turtle' class
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.08
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        #multiplying by negative one now makes the 'y_move' a negative number which caused the 'move' function
        #to change the new_y. ex. new_y = 280 + 10; the ball hits the top wall at 290; y_move=10 * -1 now = -10
        #the next new_y is now 290 + (-10) = 280; 280 + (-10) = 270, etc.
        self.y_move *= -1

    def bounce_x(self):
        #multiplying by negative one now makes the 'y_move' a negative number which caused the 'move' function
        #to change the new_x. ex. new_x = 340 + 10; x_move=10 * -1 is now = -10
        #the next new_x is now 350 + (-10) = 340; 340 + (-10) = 330, etc.
        self.x_move *= -1
        self.move_speed *= 0.5

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.5
        self.bounce_x()
