from html import unescape


class Question:

    def __init__(self, text, answer):
        self.text = unescape(text)
        self.answer = answer
