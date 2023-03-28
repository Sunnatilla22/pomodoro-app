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
reps = 0
timer = None
# check_mark = ""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        #if it's the 8th rep
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        #if it's 2nd/4th/6th rep
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
        # global check_mark
        # check_mark += "✔"
        # check_marks.config(text=check_mark)
    else:
        # if it's the 1st/3rd/5th/7th rep:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # 300
    # 245 =
    # 245 / 60 = 4 minutes
    # 245 % 60 = remaining seconds

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        #Recursion if the count is less than 0 then continue out timer to the next phase
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        check_marks.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(bg=YELLOW, padx=100, pady=50)

canvas = Canvas(width=200, height=230)
pomodoro_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=pomodoro_image)
timer_text = canvas.create_text(100, 125, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.config(bg=YELLOW, highlightthickness=0)
canvas.grid(row=1, column=1)


timer_label = Label(text="Timer", bg= YELLOW, highlightthickness=0, font=(FONT_NAME, 25, "bold"), fg=GREEN)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", command=reset)
reset_button.grid(row=2, column=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()

#
