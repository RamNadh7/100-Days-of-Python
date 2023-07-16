from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class UI():
    def __init__(self,quiz_brain:QuizBrain) -> None:
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quiz")

        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_label=Label(text="score: 0",fg="white",bg=THEME_COLOR,font=("Ariel",15,"bold"))
        self.score_label.grid(column=1, row=0)
    
        self.canvas=Canvas(width=350,height=250, bg="white")
        self.question_text=self.canvas.create_text(175,125,width=340,text="question", fill=THEME_COLOR,font=("Ariel",15,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=10)

        true_img= PhotoImage(file="images/true.png")
        self.true_button=Button(image=true_img,highlightthickness=0,command=self.true_click)
        self.true_button.grid(row=2,column=1)

        wrong_img= PhotoImage(file="images/false.png")
        self.false_button=Button(image=wrong_img,highlightthickness=0,command=self.false_click)
        self.false_button.grid(row=2,column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached the end of QUIZ.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_click(self):
        self.feedback(self.quiz.check_answer("True"))


    
    def false_click(self):
        self.feedback(self.quiz.check_answer("False"))
    
    def feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
