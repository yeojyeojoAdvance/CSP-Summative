import turtle as trtl
import random as rdm

screen_h = 1000
screen_w = 1500
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
painter = trtl.Turtle()
painter.goto(0,0)

# Make the game with a decent gui - 1 hour


# Make the gui interactable - 15 minutes

# Make fish randomly sized, with bigger ones being much more rare - 1 hour
def getfish():
    sizefish = "small"
    fishsize = rdm.randint(0,100)
    if fishsize >= 50:
        sizefish = "medium"
        fishsize = rdm.randint(50,150)
        if fishsize >= 100:
            fishsize = rdm.randint(100,200)
            sizefish = "large"
            if fishsize >= 150:
                fishsize = rdm.randint(150,250)
                sizefish = "xlarge"
    print(fishsize)
    print(sizefish)

# Biggest fish displayed above fisherman - 30 minutes

# Save what your biggest fish is in a save file along with your name to correlate to it - 1 hour

getfish()