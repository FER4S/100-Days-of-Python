from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text='xd test', font=FONT, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_img = PhotoImage(file='images/true.png')
        wrong_img = PhotoImage(file='images/false.png')

        self.btn_right = Button(image=right_img, highlightthickness=0, bd=0, command=self.right)
        self.btn_right.grid(row=2, column=0)

        self.btn_wrong = Button(image=wrong_img, highlightthickness=0, bd=0, command=self.wrong)
        self.btn_wrong.grid(row=2, column=1)

        self.lbl_score = Label(text='score: 0', bg=THEME_COLOR, fg='white')
        self.lbl_score.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.lbl_score.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f'You have reached the end of the quiz!\n'
                                                            f'Your score is {self.quiz.score}/10!',
                                   font=('Arial', 20, 'bold'))
            self.btn_right.config(state='disabled')
            self.btn_wrong.config(state='disabled')

    def right(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def wrong(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
