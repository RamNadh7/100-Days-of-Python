from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
Timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(Timer)
    check_marks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    Timer_Headline.config(text="Timer", fg=GREEN)
    global reps
    reps=0



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1

    work_sec=WORK_MIN*60
    short_break=SHORT_BREAK_MIN*60
    long_break=LONG_BREAK_MIN*60

    if reps%8==0:
        count_down(long_break)
        Timer_Headline.config(text="Break", fg=RED)
    elif reps%2==0:
        Timer_Headline.config(text="Break", fg=PINK)
        count_down(short_break)
    else:
        Timer_Headline.config(text="work", fg=GREEN)
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    min_count= math.floor(count/60)
    sec_count= count%60

    if sec_count<10:
        sec_count=f"0{sec_count}"

    canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")
    if count>0:
        global Timer
        Timer=window.after(1000, count_down, count - 1)
    else:
        start_timer()
        tick=""
        for i in range(math.floor(reps/2)):
            tick+="✔️"
        check_marks.config(text=tick)

 

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro Timer")
window.config(padx=100,pady=50,bg=YELLOW)

Timer_Headline=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,35,"bold"),highlightthickness=0)
Timer_Headline.grid(row=0,column=1)


canvas=Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_img= PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130, text="00:00" , font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=1,column=1)



start_Button=Button(text="Start", highlightthickness=0,command=start_timer)
start_Button.grid(row=2,column=0)

Reset_Button=Button(text="Reset", highlightthickness=0, command=reset_timer)
Reset_Button.grid(row=2,column=2)

check_marks=Label(font=(30),fg=GREEN,bg=YELLOW)
check_marks.grid(row=3,column=1)



window.mainloop()