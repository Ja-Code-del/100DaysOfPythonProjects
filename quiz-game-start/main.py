from question_model import Question
from data import question_data
#The Question bank
question_bank = []
for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))
