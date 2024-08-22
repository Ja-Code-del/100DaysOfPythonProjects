from question_model import Question
from quiz_brain import QuizBrain


class Levels:
    def __init__(self, level):
        # level is the actual list of data
        self.level = level
        self.question_bank = []
        self.cerebro = QuizBrain(self.question_bank)

    def initialize(self):
        self.cerebro.score = 0
        for item in self.level:
            self.question_bank.append(Question(item["text"], item["answer"], item["info"]))

    def process(self):
        while self.cerebro.still_has_question():
            self.cerebro.next_question()

        print("NIVEAU TERMINE")
        print(f"VOTRE SCORE FINAL EST : {self.cerebro.score}/{len(self.question_bank)}")

    def user_can_pass(self, this_cerebro):
        if this_cerebro.score > round(len(self.level) / 2):
            print("Bien joué, vous passez au niveau suivant!!!")
            print("------------------------------------------------------------------------------------------")
            return True
        else:
            print("MALHEUREUSEMENT VOTRE COURSE S'ARRETE ICI.\nSCORE INSUFFISANT")
            return False
