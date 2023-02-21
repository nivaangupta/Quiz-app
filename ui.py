from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class UI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.answer = ''
        self.window = Tk()
        self.window.title('TRIVIA')
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.canvas = Canvas(height=300, width=300, background='white', highlightthickness=0)
        self.question = self.canvas.create_text(150,
                                                150,
                                                width=275,
                                                text='The question is here',
                                                fill=THEME_COLOR,
                                                font=('arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2)

        true_pic = PhotoImage(file='./images/true.png')
        self.true_b = Button(image=true_pic, highlightthickness=0, command=self.true_click)
        self.true_b.grid(row=2, column=0, padx=20, pady=20)

        false_pic = PhotoImage(file='./images/false.png')
        self.false_b = Button(image=false_pic, highlightthickness=0, command=self.false_click)
        self.false_b.grid(row=2, column=1, padx=20, pady=20)

        self.score_board = Label(font=('arial', 12), bg=THEME_COLOR, text='SCORE : 0', fg='white')
        self.score_board.grid(row=0, column=1)
        self.score_board.config(padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.closing_ui()

    def true_click(self):
        self.check_answer('True')

    def false_click(self):
        self.check_answer('False')

    def check_answer(self, answer):
        if answer == self.quiz.current_question.answer:
            self.quiz.score += 1
            self.canvas.configure(bg='green')
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.configure(bg='red')
            self.window.after(1000, self.get_next_question)
        self.score_board.configure(text=f'SCORE : {self.quiz.score}')

    def closing_ui(self):
        self.canvas.itemconfig(self.question,
                               text=f'Quiz Over.\nYour final score is:\n{self.quiz.score}/{self.quiz.question_number}')
        self.true_b.config(state='disabled')
        self.false_b.config(state='disabled')




