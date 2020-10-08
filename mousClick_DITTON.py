"""
Created on Wed Oct  7 13:56:25 2020

@author: larry

This program creates a drawing of either a square spiral, a circle of circles,
or a line that goes in a random direction at any place the user clicks. The 
drawing will be of a random color.
"""

import turtle, random

#Variables

#Color palette
eerie = [39,39,39]
salsa = [249, 65, 68]
oranRed = [243, 113, 43]
yellOrange = [248, 144, 18]
mango = [249, 132, 74]
maize = [249, 199, 79]
pistachio = [144, 190, 109]
zomp = [67, 170, 139]
cadet = [77, 144, 142]
queenBlue = [87, 117, 144]
cgBlue = [39, 125, 161]

palette = [salsa, oranRed, yellOrange, mango, maize, 
           pistachio, zomp, cadet, queenBlue, cgBlue]

#Drawing Variables
#size = 1
drawingType = ["square", "circle", "line"]
squareAngle = 93
triAngle = 123
spiralRange = 35
circleSize = 50
circleTravel = 30

#Other Variables
###running = True
w = 1920
h = 1080
turtleWidth = 5

#Turtle Setup
turtle.setup(w, h)
panel = turtle.Screen()
panel.colormode(255)
panel.bgcolor(eerie)
drawTurt = turtle.Turtle()
drawTurt.shape("arrow")
drawTurt.width(turtleWidth)


def drawClick(x,y):
    "Creates a drawing of rand type (sq., circle, or crazy) & color at click"
    
    size = 5
    randDraw = random.choice(drawingType) #randomly pick drawing type
    randColor = random.choice(palette)    #randomly pick a color
    drawTurt.up()
    drawTurt.goto(x,y)
    drawTurt.color(randColor)
    drawTurt.down()
    
    
    if randDraw == "square":      #make square spiral
        
       for times in range(spiralRange):
            drawTurt.forward(size)
            drawTurt.left(squareAngle)
            size += 5

        
    elif randDraw == "circle":    #make circle of circles
        drawTurt.speed(0)
        for times in range(36):         
            drawTurt.circle(circleSize)
            drawTurt.forward(circleTravel)
            drawTurt.left(10)

    #Otherwise, make line in random direction of random size:
    else: 

        #make line in random direction of random size:
        drawTurt.left(random.randrange(0,360))
        drawTurt.forward(random.randrange(50,500))
    
    
    
panel.onclick(drawClick)
  
panel.mainloop()
turtle.done()