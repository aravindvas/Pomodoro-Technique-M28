pink = "#e2979c"
red = "#e7305b"
green = "#4aa96c"
yellow = "#f7f5dd"
fnt = "Courier"
tck = "✔"
wm = 25
shtbk = 5
lngbk = 20
rep = 0
tm = None

from tkinter import *
import math

# import time
# c = 5
# while True:
#     time.sleep(1)
#     c -= 1
def rst():
    wd.after_cancel(tm)
    t1.config(text="Timer",fg=green)
    t2.config(text="")
    cn.itemconfig(tmr, text="00:00")
    global rep
    rep = 0

def stmr():
    global rep
    rep += 1
    if rep % 8 == 0:
        t1.config(text="LBreak",fg=red)
        cntd(lngbk * 60)
    elif rep % 2 == 0:
        t1.config(text="SBreak",fg=pink)
        cntd(shtbk * 60)
    else:
        t1.config(text="Work",fg=green)
        cntd(wm * 60)


def cntd(c):
    cmin = math.floor(c / 60)
    csec = c % 60
    if csec < 10:
        csec = f"0{csec}"

    cn.itemconfig(tmr, text=f"{cmin}:{csec}")
    if c > 0:
        global tm
        tm = wd.after(1000, cntd, c - 1)
    else:
        stmr()
        m =  ""
        for i in range(math.floor(rep/2)):
            m += tck
        t2.config(text=m)


wd = Tk()
wd.title("Aravindvas's Pomodoro")
wd.config(padx=100, pady=50,bg=yellow)

cn = Canvas(width=200, height=224, bg=yellow, highlightthickness=0)
timg = PhotoImage(file="tomato.png")
cn.create_image(100, 112, image=timg)
tmr = cn.create_text(100,130,text="00:00",fill="white",font=(fnt, 35, "bold"))
cn.grid(column=1, row=1)

t1 = Label(text="Timer",font=(fnt, 40),fg=green,bg=yellow)
t1.grid(column=1, row=0)

t2 = Label(fg=green,bg=yellow)
t2.grid(column=1, row=3)

b1 = Button(text="Start",highlightthickness=0, command=stmr)
b1.grid(column=0, row=2)

b2 = Button(text="Reset",highlightthickness=0, command=rst)
b2.grid(column=2, row=2)












wd.mainloop()