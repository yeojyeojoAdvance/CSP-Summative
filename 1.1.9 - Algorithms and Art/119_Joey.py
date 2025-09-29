# importing modules
import turtle as trtl
import random as rdm
import keyboard as key
import time as time
painter = trtl.Turtle()
# screen and variables
screen_h = 1000
screen_w = 1500
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
start = ("c")
season = ("idk")

def changeseason():
    season = trtl.textinput("Confirmation:","What season would you like? Summer, Fall, Winter, Spring")
trtl.onkeypress(changeseason, "c")

start = trtl.textinput("Confirmation:","Press C to bring up the menu to set the season! Enter 'y' to continue!")
wn.onkeypress(changeseason, "c") 

while start != ("y"):
    start = trtl.textinput("Confirmation:","Press C to bring up the menu to set the season! Enter 'y' to continue!")


while start == ("y"):
    season = trtl.textinput("Confirmation:","What season would you like? Summer, Fall, Winter, Spring")
    if season == ("Summer"):
        print("hi")
    
    if season == ("Fall"):
        print("hi")
    
    if season == ("Winter"):
        print("hi")
    
    if season == ("Spring"):
        print("hi")
    time.sleep(1)
    print(season)
        






wn.listen()
wn.mainloop()
