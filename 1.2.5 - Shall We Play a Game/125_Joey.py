import turtle as trtl
import random as rdm

screen_h = 1000
screen_w = 1500
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
painter = trtl.Turtle()
painter.goto(0,0)

# make custom shapes


# Make deck of cards - 1 hour
heart = [2,3,4,5,6,7,8,9,10,10,10,10,11]
diamond = [2,3,4,5,6,7,8,9,10,10,10,10,11]
spade = [2,3,4,5,6,7,8,9,10,10,10,10,11]
club = [2,3,4,5,6,7,8,9,10,10,10,10,11]
fulldeck = [heart,diamond,spade,club]

painter.setheading(90)
rdm.choice(fulldeck)


# Make bettable chips - 15 minutes
chips = 1000
# Make the rules of blackjack - 2+ hours
# Manipulate your chips and record them in a txt file - 1 hour
# Make the game with a gui - 1 hour


wn.mainloop()