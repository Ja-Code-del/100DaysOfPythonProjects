class Question:
    #Each question object has text and answer attributes
    def __init__(self, q_text, q_answer, q_info):
        self.text = q_text
        self.answer = q_answer
        self.info = q_info
