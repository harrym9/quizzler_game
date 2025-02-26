from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label()
        self.score_label.config(text=f"Score: {self.quiz.user_score})", bg=THEME_COLOR, fg="white", font=("Arial", 13, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="",
            width=290,
            font=("Arial", 15, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        t_button = PhotoImage(file="images/true.png")
        self.true_button = Button(image=t_button, highlightthickness=0, command=self.true_press)
        self.true_button.grid(row=2, column=0)
        f_button = PhotoImage(file="images/false.png")
        self.false_button = Button(image=f_button, highlightthickness=0, command=self.false_press)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.user_score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.score_label.config(text="")
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz. Congratulations!"
                                                            f"Your final score: {self.quiz.user_score} "
                                                            f"from {self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_press(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def false_press(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, func=self.get_next_question)
