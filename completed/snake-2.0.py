import turtle
import random
import time

snake = turtle.Turtle()
apple = turtle.Turtle()
screen = turtle.Screen()

screen.tracer(0)

screen.setup(1000, 1000)
screen.bgcolor("darkgreen")

snake.hideturtle()
apple.hideturtle()

snake.color("lime")
snake.shape("turtle")
snake.penup()
snake.speed(-1)

apple.color("red")
apple.shape("circle")
apple.speed(-1)

score = -1
rotation = 0
turtlerotation = 180
dead = False

def up():
    global rotation
    rotation = 1 # 90

def dn():
    global rotation
    rotation = 3 # 270

def lt():
    global rotation
    rotation = 4 # 0

def rt():
    global rotation
    rotation = 2 # 180

def die():
    global snake
    global screen
    global score
    global dead

    dead = True
    
    screen.listen(False)
    screen.tracer(1)
    snake.color("maroon")
    screen.bgcolor("red")
    endtext = turtle.Turtle()
    endtext.hideturtle()
    endtext.penup()
    endtext.speed(-1)
    endtext.write("YOU LOSE! D:", align = "center", font = ("Arial", 24, "bold"))

    endtext.rt(90)
    endtext.fd(60)
    scf = "Score: " + str(score)
    endtext.write(scf, align = "center", font = ("Arial", 12, "bold"))

    endtext.fd(20)
    endtext.write("This window will close in 10 seconds.", align = "center", font = ("Arial", 8, "bold"))

    snake.goto(0, -20)
    snake.showturtle()
    apple.hideturtle()

    time.sleep(10)
    screen.bye()

def rotate():
    global turtlerotation
    global rotation
    global snake

    if turtlerotation == 180: # 2
        if rotation == 1:
            turtlerotation = 90
            snake.lt(90)
        elif rotation == 3:
            turtlerotation = 270
            snake.rt(90)
        elif rotation == 4:
            rotation = 2
    elif turtlerotation == 270: # 3
        if rotation == 1:
            rotation = 3
        elif rotation == 2:
            snake.lt(90)
            turtlerotation = 180
        elif rotation == 4:
            snake.rt(90)
            turtlerotation = 0
    elif turtlerotation == 0: # 4
        if rotation == 1:
            snake.rt(90)
            turtlerotation = 90
        elif rotation == 2:
            rotation = 4
        elif rotation == 3:
            snake.lt(90)
            turtlerotation = 270
    elif turtlerotation == 90: # 1
        if rotation == 2:
            snake.rt(90)
            turtlerotation = 180
        elif rotation == 3:
            rotation = 1
        elif rotation == 4:
            snake.lt(90)
            turtlerotation = 0

def colApple():
    global snake
    global score
    global apple
    if apple.xcor() > snake.xcor() - 15 and apple.xcor() < snake.xcor() + 15 and apple.ycor() > snake.ycor() - 15 and apple.ycor() < snake.ycor() + 15:
        score += 1
    while apple.xcor() > snake.xcor() - 15 and apple.xcor() < snake.xcor() + 15 and apple.ycor() > snake.ycor() - 15 and apple.ycor() < snake.ycor() + 15:
        apple.goto(random.randint(-490,490), random.randint(-490,490))

snake.showturtle()
snake.speed(10)
apple.penup()
apple.showturtle()

screen.onkey(dn, "Down")
screen.onkey(up, "Up")
screen.onkey(lt, "Left")
screen.onkey(rt, "Right")

screen.onkey(dn, "s")
screen.onkey(up, "w")
screen.onkey(lt, "a")
screen.onkey(rt, "d")

screen.listen(True)

while dead == False:
    rotate()
    
    if not rotation == 0:
        snake.fd(5)
    
    colApple()
    screen.update()
    
    if snake.ycor() >= 495 or snake.xcor() >= 495 or snake.ycor() <= -495 or snake.xcor() <= -495:
        die()
        break
    
    time.sleep(1 / 60)