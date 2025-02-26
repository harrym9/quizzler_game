class QuizzBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.user_score = 0
        self.question_list = q_list
        self.still_has_questions()

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?: ").title()
        self.check_answer(user_answer, current_question)


    def check_answer(self, user_input, current_answer):
        answer = current_answer.answer
        if user_input == answer:
            self.user_score += 1
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"Your score is: {self.user_score}/{self.question_number}")
        print("\n")