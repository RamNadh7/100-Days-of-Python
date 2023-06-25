class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0


    def still_has_question(self):
        if self.question_number<len(self.question_list):
            return True
        else:
            return False


    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        usr_answer=input(f"Q.{self.question_number}: {current_question.text} (True/False) :")
        self.check_answer(usr_answer,current_question.answer)


    def check_answer(self, usr_answer, correct_answer):
        if usr_answer.lower()==correct_answer.lower():
            self.score+=1
            print("Your answer is correct!!")
        else:
            print("That's wrong answer.")
        print(f"The Correct Answer is {correct_answer} ")
        print(f"Your score is {self.score}/{self.question_number}") 
        print("\n")