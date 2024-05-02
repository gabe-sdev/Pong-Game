from turtle import Turtle

#Create a Constant Variable that will never change throughout the code
MOVE_DISTANCE = 20


#The 'Pongpaddle' class will inherent all the attribute and methods from the parent Turtle class
class Pongpaddle(Turtle):
    #Updated Code
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        # The shape of the square by default is 20px by 20px. By setting the 'stretch_wid=5'
        # it will multiply 20x5 = 100px and the 'stretch_len=1' (20x1) will keep the length at 20px
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.pu()
        self.goto(position)

    # Methods below handle the movement of the snake
    def up(self):
        #The 'ycor()' methods retrieve the current y coordinate of the 'paddle1'object, and we are adding
        #the "MOVE_DISTANCE" (20) amount to it and then setting the new coordinates of the 'paddle1' object
        #to stay at x=350 and y = y +20 ea time the up arrow is pressed.
        if self.ycor() != 260:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(x=self.xcor(), y=new_y)

        print(self.ycor())
        
    def down(self):
        # The 'ycor()' methods retrieve the current y coordinate of the 'paddle1'object, and we are adding
        # the "MOVE_DISTANCE" (20) amount to it and then setting the new coordinates of the 'paddle1' object
        # to stay at x=350 and y = y - 20 ea time the down arrow is pressed.
        if self.ycor() != -240:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(x=self.xcor(), y=new_y)

        print(self.ycor())
