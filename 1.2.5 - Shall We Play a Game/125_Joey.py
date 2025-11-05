import turtle as trtl
import random as rdm

screen_h = 750
screen_w = 750
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
painter = trtl.Turtle()
painter.goto(0,0)
painter.speed(0)
# Make the game with a decent gui - 1 hour
painter.color("lightblue")
painter.begin_fill()
painter.circle(100)
painter.end_fill()
painter.penup()
painter.setheading(45)
painter.goto(25,-100)
painter.color("black")
painter.pendown()
painter.circle(radius=50, steps=4)
painter.setheading(0)
painter.penup()
painter.goto(-50,-150)
painter.write("Click above to fish!", font= ("Papyrus", 25, "normal"))
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




wn.mainloop()