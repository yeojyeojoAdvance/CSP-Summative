# importing modules
import turtle as trtl
import random as rdm
import time as tme
painter = trtl.Turtle()
# screen and variables
screen_h = 1000
screen_w = 1500
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
start = ("idk")
creating = 1
mtnx = -750
mtny = 250
colorlist = [("gray50"),("gray60"),("gray70")]


def sky():
    painter.penup()
    painter.speed(0)
    painter.pencolor("DarkSlateGray1")
    painter.fillcolor("DarkSlateGray1")
    painter.goto(750,200)
    painter.setheading(45)
    painter.pendown()
    painter.begin_fill()
    painter.circle(10000, steps = 4)
    painter.end_fill()
    painter.penup()
def mountain():
    randomcolor = rdm.choice(colorlist)
    painter.color(randomcolor,randomcolor)
    painter.begin_fill()
    painter.setheading(180)
    randomheight = rdm.randint(100,130)
    painter.circle(randomheight, steps=3)
    painter.end_fill()

'trtl.textinput("Confirmation:", "Hello! Are you ready to be sent to a winter wonderland?")'
sky()
painter.goto(mtnx,mtny)
painter.pendown()
for mountains in range(25):
    mtny = 250
    randomy = rdm.randint(-25,25)
    mtny = mtny + randomy
    painter.penup()
    painter.goto(mtnx,mtny)
    painter.pendown()
    mountain()
    painter.penup()
    painter.setheading(0)
    randomforward = rdm.randint(50,100)
    painter.forward(randomforward)
    mtnx = mtnx + randomforward
    painter.pendown()





wn.listen()
wn.mainloop()
