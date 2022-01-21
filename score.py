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
        # self.high_score = 0
        with open("hi-score.txt") as file:
            self.high_score = int(file.read())
        self.update_scoreboard()

        # File Management
        self.hi_score_file = "hi-score.txt"
        # self.content = self.hi_score_file.read()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} | High Score = {self.high_score}", False, 'center', ('Courier', 16, 'bold'))

    def plus_one(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_file()
        self.score = 0
        self.update_scoreboard()

    def write_file(self):
        with open(self.hi_score_file, "w") as file:
            file.write(str(self.high_score))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, "center", ('Courier', 22, 'bold'))
