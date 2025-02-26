from data import question_data
from question_model import Question
from quiz_brain import QuizzBrain
from ui import QuizInterface

question_bank = []

for question in question_data:
    quiz = Question(question["question"], question["correct_answer"])
    question_bank.append(quiz)

quiz = QuizzBrain(question_bank)
quiz_ui = QuizInterface()

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"You're final score is {quiz.user_score}/{quiz.question_number}")
