#ASKING THE QUESTIONS
class QuizBrain:
    """Quiz class to generate every quiz game and manage them """
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text}. (Vrai / Faux)\n")
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        """Return True (or False) if there are still questions to ask"""
        return self.question_number < len(self.question_list)

    #CHECKING IF THE ANSWER WAS CORRECT
    def check_answer(self, user_answer, correct_answer):
        """Check the answer of the user and upgrade his score"""
        information = self.question_list[self.question_number - 1].info
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Bien joué\n")
            print(f'En effet : {information}')
            print(f"Votre score est: {self.score}")
            print("\n")
        else:
            print("Mauvaise réponse\n")
            print(f"Il fallait dire : {correct_answer}")
            print(f'Explication : {information}')
            print(f"Votre score reste: {self.score}")
            print("\n")
