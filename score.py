from turtle import Turtle


class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.refresh()
        self.hideturtle()

    def refresh(self):
        self.write(f"Score:{self.score}", align="center", font=('Arial', 20, 'normal'))

    def update_score(self):
        self.clear()
        self.score += 1
        self.refresh()

    def game_end(self):
        self.color("red")
        self.goto(0,0)

        self.write(f"Game Over...")
