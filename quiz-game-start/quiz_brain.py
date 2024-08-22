#ASKING THE QUESTIONS
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text}. (True / False)\n")
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        """Return True (or False) if there are still questions to ask"""
        return self.question_number < len(self.question_list)

    #CHECKING IF THE ANSWER WAS CORRECT
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
            print(f"Your current score is: {self.score}")
        else:
            print("That's wrong")
            print(f"The correct answer was : {correct_answer}")
            print(f"Your current score is: {self.score}")
            print("\n")


