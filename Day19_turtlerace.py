import random
from turtle import Turtle, Screen

x = -200
y = -150


screen = Screen()
screen.setup(width = 500,height = 400)

user_bet = screen.textinput("Choose your turtle","Color:")
if user_bet:
    is_race_on=True

turtle_list = ["red","blue","orange","green","pink","purple","black"]
turtle_color_list = turtle_list[:]

for i in range (7):
    turtle_list[i] = Turtle()
    turtle_list[i].shape("turtle")
    turtle_list[i].penup()
    turtle_list[i].color(f"{turtle_color_list[i]}")
    turtle_list[i].goto(x,y)
    y=y+50

while is_race_on == True:
    distance = random.randint(0,10)
    x = random.choice(turtle_list)
    x.forward(distance)
    if x.xcor() >230:
        print(f"The winner is {x.pencolor()}")
        is_race_on = False
        if user_bet == x.pencolor():
            print("Your turtle won!")
        else:
            print("Try luck next time")

screen.exitonclick()