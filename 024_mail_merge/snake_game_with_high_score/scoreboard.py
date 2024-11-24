from turtle import Turtle

HIGH_SCORE_FILE = "data.txt"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center")

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_scoreboard()

    def load_high_score(self) -> int:
        with open(HIGH_SCORE_FILE) as file:
            return int(file.read())

    def write_high_score(self) -> None:
        with open(HIGH_SCORE_FILE, mode="w") as file:
            file.write(str(self.high_score))


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center")
