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
fishsize = rdm.randint(1,100)
print(fishsize)

# Biggest fish displayed above fisherman - 30 minutes

# Save what your biggest fish is in a save file along with your name to correlate to it - 1 hour
