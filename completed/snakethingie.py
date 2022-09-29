import turtle
import random

snake = turtle.Turtle()
setup = turtle.Turtle()
apple = turtle.Turtle()
screen = turtle.Screen()

score = -1

screen.setup(400, 400)
screen.bgcolor("darkgreen")

snake.hideturtle()
setup.hideturtle()
apple.hideturtle()

snake.shape("turtle")
snake.color("lime")
snake.penup()

apple.shape("circle")
apple.color("red")
apple.penup()
apple.speed(-1)

setup.color("green")
setup.speed(-1)
setup.goto(195, -195)
setup.begin_fill()
for i in range(4):
  setup.lt(90)
  setup.fd(390)
setup.end_fill()

rot = 0
trot = 180

def up():
  global rot
  rot = 1 # 90

def dn():
  global rot
  rot = 3 # 270

def lt():
  global rot
  rot = 4 # 0

def rt():
  global rot
  rot = 2 # 180

def die():
  global snake
  global screen
  global setup
  global score
  
  snake.color("maroon")
  screen.bgcolor("red")
  setup.clear()
  endtext = turtle.Turtle()
  endtext.hideturtle()
  endtext.write("YOU LOSE! D:", align = "center", font = ("Arial", 24, "bold"))
  snake.goto(0, -20)
  apple.hideturtle()
  
  print("Score: " + str(score))

def colApple():
  global snake
  global score
  global apple
  if apple.xcor() > snake.xcor() - 15 and apple.xcor() < snake.xcor() + 15 and apple.ycor() > snake.ycor() - 15 and apple.ycor() < snake.ycor() + 15:
    apple.goto(random.randint(-190,190), random.randint(-190,190))
    score += 1
  

screen.onkey(up, "Up")
screen.onkey(dn, "Down")
screen.onkey(lt, "Left")
screen.onkey(rt, "Right")
screen.onkey(up, "w")
screen.onkey(dn, "s")
screen.onkey(lt, "a")
screen.onkey(rt, "d")
screen.listen()

snake.showturtle()
snake.speed(-1)
apple.showturtle()
while True:
  screen.update()
  if trot == 180: # 2
    if rot == 1:
      trot = 90
      snake.lt(90)
    elif rot == 3:
      trot = 270
      snake.rt(90)
    elif rot == 4:
      rot = 2
  elif trot == 270: # 3
    if rot == 1:
      rot = 3
    elif rot == 2:
      snake.lt(90)
      trot = 180
    elif rot == 4:
      snake.rt(90)
      trot = 0
  elif trot == 0: # 4
    if rot == 1:
      snake.rt(90)
      trot = 90
    elif rot == 2:
      rot = 4
    elif rot == 3:
      snake.lt(90)
      trot = 270
  elif trot == 90: # 1
    if rot == 2:
      snake.rt(90)
      trot = 180
    elif rot == 3:
      rot = 1
    elif rot == 4:
      snake.lt(90)
      trot = 0
  if snake.ycor() >= 195 or snake.xcor() >= 195 or snake.ycor() <= -195 or snake.xcor() <= -195:
    die()
    break
  colApple()
  if not rot == 0:
    snake.fd(4)
screen.mainloop()
