from turtle import Turtle


class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.refresh()
        self.hideturtle()

    def refresh(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}", align="center", font=('Arial', 20, 'normal'))

    def update_score(self):
        self.score += 1
        self.refresh()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w")  as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()