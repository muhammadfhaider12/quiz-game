import html


class quizbrain:
    def __init__(self,question_list):
        self.questionNumber =0
        self.question_list=question_list
        self.score=0

    def new_question(self):
        current_question=self.question_list[self.questionNumber-1]
        self.questionNumber +=1
        q_text=html.unescape(current_question.text)
        return f"Q.{self.questionNumber}:{q_text}"
        # user_answer = input(f"Q.{self.questionNumber}: {q_text} (True/False)")
        #self.check_answer(current_question.answer,user_answer)

    def still_have_question(self):
        return len(self.question_list) > self.questionNumber

    def check_answer(self,user_answer):
        current_question = self.question_list[self.questionNumber-1]
        correct_answer=current_question.answer
        if correct_answer.lower()==user_answer.lower():
            self.score +=1
            return True
        else:
            return False



