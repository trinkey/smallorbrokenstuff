import turtle, random

pizzaSize = int(input("How large? "))
pepperoni = input("Pepperoni? (True/False) ").lower()

if pepperoni == "true":
    pepperoniAmount = int(input("How many pepperoni? "))
    pepperoniSize = int(input("How large is the pepperoni? "))

turt = turtle.Turtle()
scr = turtle.Screen()

scr.setup(400, 400)
scr.bgcolor("cyan")
scr.tracer(0)

turt.pu()

turt.color("tan")
turt.dot(pizzaSize)
turt.color("gold")
turt.dot(pizzaSize - 20)

if pepperoni == "true":
    turt.color("red")
    for i in range(pepperoniAmount):
        turt.goto(random.randint(20 - pizzaSize / 2, 20 + pizzaSize / 2), random.randint(20 - pizzaSize / 2, 20 + pizzaSize / 2))
        turt.dot(pepperoniSize)

turt.hideturtle()
scr.update()
scr.mainloop()
