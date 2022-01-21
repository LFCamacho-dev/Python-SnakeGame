from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 260)
        self.color("gray")
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}", False, 'center', ('Courier', 16, 'bold'))

    def plus_one(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ('Courier', 22, 'bold'))