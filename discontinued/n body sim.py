import turtle
import random

screen = turtle.Screen()
screen.setup(500,500)
screen.bgcolor("#222222")

obj1 = turtle.Turtle()
obj2 = turtle.Turtle()
obj1.shape("circle")
obj2.shape("circle")
obj1.penup()
obj2.penup()

obj1.goto(random.randint(-250,250), random.randint(-250,250))
dist = obj1.distance(obj2)
print(dist)

turtle.bye()