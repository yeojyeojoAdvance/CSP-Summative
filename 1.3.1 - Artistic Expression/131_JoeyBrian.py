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



ingame = False

def envelopeopener(x,y):
    wn.bgpic(open_envelope)
    trtl.onscreenclick(mapopener)

def mapopener(x,y):
    global ingame
    wn.bgpic(map)
    ingame = False
    trtl.onscreenclick(mapclicker)



def mapclicker(x,y):
    global ingame
    if 0 < x < 300 and -300 < y < 0 and ingame == False:
        ingame = True
        leave = trtl.textinput("Continue?","Thank you for playing, if you want to stay, enter in 'y'!")
        if leave == "y":
            print("stay")
        else:
            exit()
    if -300 < x < 0 and -300 < y < 0 and ingame == False:
        ingame = True
        music()


    if 0 < x < 300 and 0 < y < 300 and ingame == False:
        ingame = True
        golf()


    if -300 < x < 0 and 0 < y < 300 and ingame == False:
        ingame = True
        shuffleboard()

def shuffleboard():
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

def music(): 
    print("music")
    global musicplaying
    global ingame
    indexchoice = trtl.textinput("What type of music?","1 = Calm Jazz, 2 = Cool Jazz, 3 = Mozart, 4 = Put Your Head On My Shoulder")
    indexchoice = int(indexchoice)
    musicchoice = musiclist[indexchoice-1]
    if musicplaying == True:
        playsound(musicchoice, block=False)
    musicplaying = False


wn.listen()
wn.onkeypress(lambda: mapopener("x","y"))

trtl.onscreenclick(envelopeopener)




#Make interactable sections of the map

#Golf

#Shuffleboard

#Music?

#Exit button



wn.mainloop()