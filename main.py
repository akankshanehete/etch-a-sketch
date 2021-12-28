from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forward():
    t.forward(10)


screen.listen()
# when you pass function as an input, don't include the brackets as the function will then be executed then and there
# a higher order function is one that can work with other functions
screen.onkey(key='space', fun=move_forward)
screen.exitonclick()



