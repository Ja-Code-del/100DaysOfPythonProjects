from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#The Question bank which contains question objects
question_bank = []
for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))

#create cerebro our QuizBrain object
cerebro = QuizBrain(question_bank)

#until cerebro has question, he could ask
while cerebro.still_has_question():
    cerebro.next_question()

#ending of the game
print("You completed this level")
print(f"Your final score is: {cerebro.score}/{len(question_bank)}")

