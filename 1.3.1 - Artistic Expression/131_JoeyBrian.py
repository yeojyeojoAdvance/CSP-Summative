import turtle as trtl
import random as rand
from playsound import playsound
wn = trtl.Screen()
drawer = trtl.Turtle()
golfball = trtl.Turtle()
golfball.hideturtle()
wn.screensize(600,600)

#Envelope that opens on click 
open_envelope="openenvelope.gif"
closed_envelope="closedenvelope.gif"
map="map.gif"
golfcourse = "golfcourse.gif"

musicplaying = True

wn.addshape(open_envelope)
wn.addshape(closed_envelope)
wn.bgpic(closed_envelope)

musiclist = ["calmjazz.mp3", "cooljazz.mp3", "mozart.mp3", "pyhoms.mp3"]

def envelopeopener(x,y):
    wn.bgpic(open_envelope)
    trtl.onscreenclick(mapopener)

def mapopener(x,y):
    wn.bgpic(map)
    trtl.onscreenclick(mapclicker)

def mapclicker(x,y):
    if 0 < x < 300 and -300 < y < 0:
        leave = trtl.textinput("Continue?","Thank you for playing, if you want to stay, enter in 'y'!")
        if leave == "y":
            print("stay")
        else:
            exit()
    if -300 < x < 0 and -300 < y < 0:
        print("music")
        global musicplaying
        if musicplaying == True:
            playsound(rand.choice(musiclist), block=False)
        musicplaying = False


    if 0 < x < 300 and 0 < y < 300:
        golf()


    if -300 < x < 0 and 0 < y < 300:
        print("shuffleboard")



def golf():
    print("golf")
    wn.bgpic(golfcourse)
    drawer.penup()
    drawer.speed(0)
    drawer.goto(-150,-300)
    golfball.penup()
    golfball.goto(-125,-275)
    golfball.shape("circle")
    golfball.color("azure3")
    golfball.shapesize(2)
    golfball.showturtle() 

trtl.onscreenclick(envelopeopener)




#Make interactable sections of the map

#Golf

#Shuffleboard

#Music?

#Exit button



wn.mainloop()