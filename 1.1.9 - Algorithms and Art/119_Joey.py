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
creating = 1
mtnx = -750
mtny = 250
lakecolor = ("lightblue")
colorlist = [("gray50"),("gray60"),("gray70")]
trtl.addshape("car",((0,0),(1,0),(1,-3),(4,-3),(4,0),(7,0),(7,-3),(10,-3),(10,0),(11,0),(11,2),(9,2),(9,3),(8,3),(8,4),(5,4),(5,3),(4,3),(4,2),(0,2)))
carxcor = painter.xcor
carcolorlist = [
    "white","black","gray","grey","red","green","blue","cyan","yellow","magenta",
    "orange","brown","pink","purple","violet","indigo","gold","silver","lime",
    "maroon","navy","teal","olive","coral","salmon","khaki","plum","orchid",
    "turquoise","beige","azure","lavender","tan","chocolate","crimson","sienna",
    "steelblue","slategray","lightgray","darkgray","lightblue","darkblue",
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



def sky():
    painter.penup()
    painter.speed(0)
    painter.pencolor("DarkSlateGray1")
    painter.fillcolor("DarkSlateGray1")
    painter.goto(750,200)
    painter.setheading(45)
    painter.pendown()
    painter.begin_fill()
    painter.circle(10000, steps = 4)
    painter.end_fill()
    painter.penup()
def mountain():
    randomcolor = rdm.choice(colorlist)
    painter.color(randomcolor,randomcolor)
    painter.begin_fill()
    painter.setheading(180)
    randomheight = rdm.randint(130,145)
    painter.circle(randomheight, steps=3)
    painter.end_fill()

checkno = trtl.textinput("Confirmation:", "Hello! Are you ready to be sent to a winter wonderland?")
if checkno == ("no","n","NO","N","No","Nah","nah","nope"):
    trtl.textinput("Too bad.","That is too bad.")
sky()
painter.goto(mtnx,mtny)
painter.pendown()
for mountains in range(25):
    mtny = 250
    randomy = rdm.randint(-25,25)
    mtny = mtny + randomy
    painter.penup()
    painter.goto(mtnx,mtny)
    painter.pendown()
    mountain()
    painter.penup()
    painter.setheading(0)
    randomforward = rdm.randint(50,100)
    painter.forward(randomforward)
    mtnx = mtnx + randomforward
    painter.pendown()


is_error = False
while not is_error:
    lakecolor = trtl.textinput("Color?","What color do you want the lake to be? Recommended is 'lightblue'!")
    try:
        painter.color(lakecolor,lakecolor)
        is_error = True
    except trtl.TurtleGraphicsError:
        is_error = False

painter.penup()
painter.goto (325,-100)
painter.pendown()
painter.begin_fill()
painter.circle(75)
painter.end_fill()
painter.penup()
painter.goto(-325,-100)
painter.pendown()
painter.begin_fill()
painter.circle(75)
painter.end_fill()
painter.penup()

painter.goto(750,-350)
painter.pendown()
painter.color("LightSlateGray","LightSlateGray")
painter.setheading(180)

painter.begin_fill()
painter.forward(1500)
painter.right(90)
painter.forward(75)
painter.right(90)
painter.forward(1500)
painter.right(90)
painter.forward(75)
painter.right(90)
painter.end_fill()
painter.penup()

wn.update()


cloop = int(trtl.textinput("Question:","How many cars should go down this highway?"))

painter.tilt(270)
painter.setheading(180)
painter.shapesize(10,10,10)
painter.shape("car")

for car in range(cloop):
    painter.hideturtle()
    randomcarcolor = rdm.choice(carcolorlist)
    painter.color(randomcarcolor,randomcarcolor)
    painter.speed(0)
    painter.goto(750,-313)
    painter.showturtle()
    painter.speed(3)
    painter.forward(1600)





wn.listen()
wn.mainloop()
