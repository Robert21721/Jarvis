# TODO

import turtle


def speech_draw():

    turtle.bgcolor("black")
    turtle.pencolor("dark blue")
    turtle.speed(0)
    turtle.pensize(10)
    turtle.hideturtle()
    a=12
    for i in range(1, 260, 20):
        turtle.right(90)
        turtle.forward(i)
        turtle.right(270)
        turtle.pendown()
        turtle.circle(i)
        turtle.penup()
        turtle.pensize(a)
        turtle.home()
        a = a - 1


def listening():
    i=0
    while i < 3:
        speech_draw()
        turtle.clear()
        i=i+1

listening()