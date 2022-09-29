import turtle
import time
import random

# Turtles
paddleLeft = turtle.Turtle()
paddleRight = turtle.Turtle()
arena = turtle.Screen()
setup = turtle.Turtle()
ball = turtle.Turtle()

arena.tracer(0)

# Number Variables
LeftY = 0
RightY = 0
ballRotation = random.randint(10,45)
ballDir = "Right"
ballNeg = random.randint(0,1)
leftUp = 0
leftDown = 0
rightUp = 0
rightDown = 0
scoreLeft = 0
scoreRight = 0

# Custom Shape
shape =((-35, -3), (35, -3), (35, 3), (-35, 3))
turtle.register_shape("paddle", shape)

# Background
arena.bgcolor("#000000")
arena.setup(1000, 1000)
arena.tracer(0)

# Left Paddle
paddleLeft.shape("paddle")
paddleLeft.speed(-1)
paddleLeft.penup()
paddleLeft.goto(-470, LeftY)

# Right Paddle
paddleRight.shape("paddle")
paddleRight.speed(-1)
paddleRight.penup()
paddleRight.goto(470, RightY)

# black borders
setup.penup()
setup.color("#000000")
setup.speed(-1)

setup.goto(-500, 480)
setup.pendown()
setup.begin_fill()
setup.goto(500, 480)
setup.goto(500, 500)
setup.goto(-500, 500)
setup.end_fill()
setup.penup()

setup.goto(-500, -480)
setup.pendown()
setup.begin_fill()
setup.goto(500, -480)
setup.goto(500, -500)
setup.goto(-500, -500)
setup.end_fill()
setup.penup()

setup.goto(480, 480)
setup.pendown()
setup.begin_fill()
setup.goto(480, 70)
setup.goto(500, 70)
setup.goto(500, 480)
setup.end_fill()
setup.penup()

setup.goto(480, -480)
setup.pendown()
setup.begin_fill()
setup.goto(480, -70)
setup.goto(500, -70)
setup.goto(500, -480)
setup.end_fill()
setup.penup()

setup.goto(-480, 480)
setup.pendown()
setup.begin_fill()
setup.goto(-480, 70)
setup.goto(-500, 70)
setup.goto(-500, 480)
setup.end_fill()
setup.penup()

setup.goto(-480, -480)
setup.pendown()
setup.begin_fill()
setup.goto(-480, -70)
setup.goto(-500, -70)
setup.goto(-500, -480)
setup.end_fill()
setup.penup()

# Make the bong ball
ball.shape("circle")
ball.color("#dddddd")
ball.penup()

# Add Colors
paddleRight.color("#55ff55")
paddleLeft.color("#55ff55")
arena.bgcolor("#222222")

# What Keystrokes Do
def paddleLeftUp():
    global leftUp
    leftUp = 1

def paddleLeftDown():
    global leftDown
    leftDown = 1

def paddleRightUp():
    global rightUp
    rightUp = 1

def paddleRightDown():
    global rightDown
    rightDown = 1

def sRelease():
    global leftDown
    leftDown = 0

def wRelease():
    global leftUp
    leftUp = 0

def downRelease():
    global rightDown
    rightDown = 0

def upRelease():
    global rightUp
    rightUp = 0

def movement():
    global leftUp
    global leftDown
    global rightUp
    global leftUp
    global paddleLeft
    global paddleRight

    if leftUp == 1:
        paddleLeft.goto(paddleLeft.xcor(), paddleLeft.ycor() + 5)
    
    if leftDown == 1:
        paddleLeft.goto(paddleLeft.xcor(), paddleLeft.ycor() - 5)
    
    if rightUp == 1:
        paddleRight.goto(paddleRight.xcor(), paddleRight.ycor() + 5)
    
    if rightDown == 1:
        paddleRight.goto(paddleRight.xcor(), paddleRight.ycor() - 5)

def bye():
    arena.listen(False)
    arena.bye()

# Keystrokes
arena.onkeypress(paddleLeftDown, "s")
arena.onkeypress(paddleLeftUp, "w")
arena.onkeypress(paddleRightDown, "Down")
arena.onkeypress(paddleRightUp, "Up")
arena.onkeyrelease(sRelease, "s")
arena.onkeyrelease(wRelease, "w")
arena.onkeyrelease(downRelease, "Down")
arena.onkeyrelease(upRelease, "Up")
arena.onkey(bye, "0")

arena.listen(True)

# First Rotate the Ball
if ballNeg == 1:
    ball.lt(0 - ballRotation)
else:
    ball.lt(ballRotation)

def ballBounceUD():
    pass

def ballBounceLR():
    global ballNeg
    global ballDir
    global ballRotation
    global ball

    r = 180 - (2 * ballRotation)
    if ballNeg == 1:
        if ballDir == 1:
            ball.lt(r)
            ballDir = 0
        else:
            ball.rt(r)
            ballDir = 1
    else:
        if ballDir == 1:
            ball.rt(r)
            ballDir = 0
        else:
            ball.lt(r)
            ballDir = 10

while True:
    if ball.xcor():
        ballBounceLR()
    if True:
        ballBounceUD()
    ball.fd(5)
    movement()
    
    arena.update()

    time.sleep(1 / 60)
