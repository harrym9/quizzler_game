from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

from ui import QuizInterface

question_bank = []

for question in question_data:
    quiz = Question(question["question"], question["correct_answer"])
    question_bank.append(quiz)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
