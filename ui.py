from tkinter import *
import quiz_brain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label()
        self.score_label.config(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 13, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.create_text(
            150,
            125,
            text="Some text",
            width=280,
            font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        t_button = PhotoImage(file="images/true.png")
        self.true_button = Button(image=t_button, highlightthickness=0)
        self.true_button.grid(row=2, column=0)
        f_button = PhotoImage(file="images/false.png")
        self.false_button = Button(image=f_button, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()
