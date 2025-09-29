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
season = ("idk")
creating = 1
def createpainter():
    painter.pensize(10)
    painter.pencolor("black")

def changeseason():
    season = trtl.textinput("Confirmation:","What season would you like? Summer, Fall, Winter, Spring")
wn.onkeypress(changeseason, "c")
wn.listen()
start = trtl.textinput("Confirmation:","Press C to bring up the menu to set the season! Enter 'y' to continue!")


while start != ("y"):
    start = trtl.textinput("Confirmation:","Press C to bring up the menu to set the season! Enter 'y' to continue!")


while start == ("y"):
    changeseason()
    if season == ("Summer"):
        if creating == 1:
            createpainter()
            painter.forward(100)
            painter.forward(100)
            painter.forward(100)
            painter.forward(100)
            painter.forward(100)
            painter.forward(100)
            creating - 1

    
    while season == ("Fall"):
        createpainter()
        painter.forward(100)
    
    while season == ("Winter"):
        createpainter()
        painter.forward(100)
    
    while season == ("Spring"):
        createpainter()
        painter.forward(100)
    print(season)
    tme.sleep(1)


        




wn.listen()
wn.mainloop()
