from turtle import Turtle

#Create a Constant Variable that will never change throughout the code
ALIGNMENT = "center"
FONT_1 = ("Arial", 80, "normal")
FONT_2 = ("Arial", 10, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        #All of these attributes are inherited from the 'Turtle' class
        self.color("White")
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        self.goto(x=-90, y=180)
        self.divider_line()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-90, y=180)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT_1)
        self.goto(x=90, y=180)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT_1)
        self.divider_line()

    def divider_line(self):
        for y_cord in range(-300, 300, 20):
            self.goto(x=0, y=y_cord)
            self.pd()
            self.write("|", align=ALIGNMENT, font=FONT_2)
            self.pu()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
