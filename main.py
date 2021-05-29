import random
from turtle import Turtle, Screen

s = Screen()
s.bgcolor("black")
s.title("Turtle Race")
is_on = False
s.setup(width=1000, height=700)
user_bet = s.textinput(title="your bet", prompt="on which turtle you will make your guess ? ")
is_on = True
colors = ["green", "blue", "orange", "red", "pink", "yellow"]
turtles = []
for i in range(6):
    t = Turtle()
    t.penup()
    t.shape("turtle")
    t.goto(-450, -150 + i * 60)
    t.color(colors[i])
    turtles.append(t)

while is_on:
    for t in turtles:
        t.forward(random.randint(1, 10))
        if t.xcor() > 450:
            is_on = False
            if t.color() == user_bet:
                print("your turtle won the race")
            else:
                print("you lost")
            break
s.exitonclick()
