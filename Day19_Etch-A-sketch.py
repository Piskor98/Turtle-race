from turtle import Turtle, Screen

tim = Turtle()
scrren=Screen()
tim.speed('fastest')


def move_forwards():
    tim.forward(10)
def move_left():
    tim.left(10)
def move_right():
    tim.right(10)
def move_backward():
    tim.backward(10)

def clear():
    tim.reset()

scrren.listen()
scrren.onkey(key="w", fun=move_forwards)
scrren.onkey(key="s",fun=move_backward)
scrren.onkey(key="a",fun=move_left)
scrren.onkey(key="d",fun=move_right)
scrren.onkey(key = "space",fun=clear)


tim.reset()
scrren.exitonclick()