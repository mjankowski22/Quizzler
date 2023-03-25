THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

import tkinter
import time

class UI():

    def __init__(self,quiz: QuizBrain):
        self.quiz=quiz
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_label = tkinter.Label()
        self.score_label.config(text="Score: 0",highlightthickness=0,bg=THEME_COLOR,fg="white")
        self.score_label.grid(row=0,column=1,padx=15,pady=15)
        self.canvas = tkinter.Canvas()
        self.canvas.config(width=300,height=250,bg="white",highlightthickness=0)
        self.question = self.canvas.create_text(150,125,text="Sample question",font=("Arial",20,"italic"),fill=THEME_COLOR,width=270)
        self.canvas.grid(row=1,column=0,columnspan=2,padx=15,pady=15)
        image1 = tkinter.PhotoImage(file="images/false.png")
        image2 = tkinter.PhotoImage(file="images/true.png")
        self.true=tkinter.Button(image=image2,highlightthickness=0,command=self.true_button)
        self.true.grid(row=2,column=0,padx=15,pady=15)
        self.false=tkinter.Button(image=image1,highlightthickness=0,command=self.false_button)
        self.false.grid(row=2,column=1,padx=15,pady=15)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text= self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=q_text)
        else:
            self.canvas.itemconfig(self.question,text="You've reached the end of the quiz")
            self.true.config(state="disabled")
            self.false.config(state="disabled")
            self.canvas.config(bg="white")

    def change_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def true_button(self):
        is_right=self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_button(self):
        is_right=self.quiz.check_answer("false")
        self.give_feedback(is_right)
        
    def turn_back(self):
        self.canvas.config(bg="white")
        self.change_score()
        self.get_next_question()

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.turn_back)
    
    