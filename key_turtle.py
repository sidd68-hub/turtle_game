from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def counter_clockwise():
    tim.left(90)


def clock_wise():
    tim.right(90)

def clear():
    tim.clear() 
    tim.penup()
    tim.home() 
    tim.pendown()

screen.listen()
screen.onkey(key='W', fun=move_forwards)
screen.onkey(key='S',fun=move_backward)
screen.onkey(key='A',fun=counter_clockwise)
screen.onkey(key='D',fun=clock_wise)
screen.onkey(key='C',fun=clear)


screen.exitonclick()