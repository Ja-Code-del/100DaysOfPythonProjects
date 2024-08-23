from question_model import Question
from quiz_brain import QuizBrain


class Levels:
    def __init__(self, level, average_score):
        # level is the actual list of data
        self.level = level
        #stack of question
        self.question_bank = []
        self.quiz = QuizBrain(self.question_bank)
        self.score_to_passe = average_score

    def initialize(self):
        self.quiz.score = 0
        for item in self.level:
            self.question_bank.append(Question(item["text"], item["answer"], item["info"]))

    def process(self):
        while self.quiz.still_has_question():
            self.quiz.next_question()

        print("NIVEAU TERMINE")
        print(f"VOTRE SCORE FINAL EST : {self.quiz.score}/{len(self.question_bank)}")

    def user_passed(self, this_quiz):
        if this_quiz.score > self.score_to_passe:
            print("Bien joué, vous passez au niveau suivant!!!")
            print("------------------------------------------------------------------------------------------")
            return True
        else:
            print("MALHEUREUSEMENT VOTRE COURSE S'ARRETE ICI.\nSCORE INSUFFISANT")
            return False

    def reload(self, this_quiz):
        """Return the choice of the user to use it and loop on a quiz he or she loses"""
        choice = input("VOULEZ-VOUS REJOUEZ LA PARTIE? FERIEZ-VOUS MIEUX? (OUI / NON)").lower()
        return choice

    def check_reload(self, this_quiz):
        if self.reload(this_quiz) == 'oui':
            return True
        else:
            return False
