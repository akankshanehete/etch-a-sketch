from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def turn_ccw():
    t.left(10)


def turn_cw():
    t.right(10)

def clear():
    t.speed(0)
    t.goto(0, 0)
    t.setheading(0)
    t.clear()


screen.listen()
# when you pass function as an input, don't include the brackets as the function will then be executed then and there
# a higher order function is one that can work with other functions (as inputs)
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_ccw)
screen.onkey(key='d', fun=turn_cw)
screen.onkey(key='c', fun=clear)

screen.exitonclick()



