import turtle as trtl
import random as rand
from playsound import playsound
wn = trtl.Screen()
drawer = trtl.Turtle()
wn.screensize(600,700)

#Envelope that opens on click 
open_envelope="openenvelope.gif"
closed_envelope="closedenvelope.gif"
map="map.gif"
wn.addshape(open_envelope)
wn.addshape(closed_envelope)
wn.bgpic(closed_envelope)
def envelopeopener(x,y):
    wn.bgpic(open_envelope)
    trtl.onscreenclick(mapopener)

def mapopener(x,y):
    wn.bgpic(map)

trtl.onscreenclick(envelopeopener)




#Make interactable sections of the map

#Golf

#Shuffleboard

#Music?

#Exit button



wn.mainloop()