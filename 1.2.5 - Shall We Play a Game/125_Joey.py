import turtle as trtl
import random as rdm

screen_h = 750
screen_w = 750
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
painter = trtl.Turtle()
fish = trtl.Turtle()
fishcounterscore = trtl.Turtle()
fishcounterscore2 = trtl.Turtle()
fish.shape("turtle")
painter.goto(0,0)
painter.speed(0)

score = 0

fishcolorlist = [
    "white","black","gray","grey","red","green","blue","cyan","yellow","magenta",
    "orange","brown","pink","purple","violet","indigo","gold","silver","lime",
    "maroon","navy","teal","olive","coral","salmon","khaki","plum","orchid",
    "turquoise","beige","azure","lavender","tan","chocolate","crimson","sienna",
    "steelblue","slategray","lightgray","darkgray","darkblue",
    "lightgreen","darkgreen","mintcream","seagreen","aquamarine","springgreen",
    "peru","tomato","fuchsia","papayawhip","lemonchiffon","ivory","linen",
    "aliceblue","antiquewhite","burlywood","cadetblue","chartreuse","cornflowerblue",
    "cornsilk","darkorange","darksalmon","deeppink","dodgerblue","firebrick",
    "gainsboro","hotpink","indianred","lavenderblush","lightcoral","lightcyan",
    "lightgoldenrodyellow","lightsalmon","lightskyblue","lightsteelblue",
    "lightyellow","mediumaquamarine","mediumblue","mediumorchid","mediumpurple",
    "mediumseagreen","mediumslateblue","mediumspringgreen","mediumturquoise",
    "mediumvioletred","midnightblue","moccasin","navajowhite","oldlace","palegreen",
    "paleturquoise","palevioletred","powderblue","rosybrown","royalblue","saddlebrown",
    "seashell","sienna","skyblue","steelblue","thistle","wheat"
    ]

# Make the game with a decent gui - 1 hour
painter.color("lightblue")
painter.begin_fill()
painter.circle(100)
painter.end_fill()
painter.penup()
painter.goto(-50,-150)
painter.color("black")
painter.write("Click to fish!", font= ("Papyrus", 25, "normal"))
# Make the gui interactable - 15 minutes

# Make fish randomly sized, with bigger ones being much more rare - 1 hour
def getfish():
    global fishsize
    global sizefish 
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
def fishtrtl():
    fish.penup()
    fish.goto(0,75)
    fish.speed(1)
    fish.color(rdm.choice(fishcolorlist))
    if sizefish == "small":
        fish.shapesize(1)
    elif sizefish == "medium":
        fish.shapesize(3)
    elif sizefish == "large":
        fish.shapesize(5)
    elif sizefish == "xlarge":
        fish.shapesize(7)
    fish.goto(0,250)
    showfish()

def showfish():
    fishcounterscore.penup()
    fishcounterscore2.penup()
    fishcounterscore.speed(0)
    fishcounterscore2.speed(0)
    fishcounterscore.hideturtle()
    fishcounterscore2.hideturtle()
    fishcounterscore.goto(-175,250)
    fishcounterscore2.goto(-175,225)
    fishcounterscore.write("The fish is " + sizefish, font= ("Papyrus", 20, "normal"))
    fishcounterscore2.write(fishsize, font= ("Papyrus", 20, "normal"))
# Save what your biggest fish is in a save file along with your name to correlate to it - 1 hour

getfish()
fishtrtl()



wn.mainloop()