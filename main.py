from question_model import Question
from data import question_data
from QuizBrain import quizbrain
from quiz_interface import QuizUI



question_bank=[]

for question in question_data:
    question_text = question["question"]
    correct_answer = question["correct_answer"]
    new_question = Question(question_text,correct_answer)
    question_bank.append(new_question)


quiz=quizbrain(question_bank)
quizui= QuizUI(quiz)

while quiz.still_have_question():
     quiz.new_question()

#print(f"Quiz Completed!\nYour final score is {quiz.score}")

