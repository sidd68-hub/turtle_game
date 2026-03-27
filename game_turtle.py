from turtle import Turtle,Screen
import random


screen = Screen()
screen.setup(width=500,height=400)
choose_color = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color: ")

color = ['purple', 'blue', 'green', 'yellow', 'orange', 'red']
y_position = [-70,-40,-10,20,50,80]

is_race_on = False
all_turtles = []

for turtle_index in range(0,6):
    tim = Turtle(shape='turtle',)
    tim.color(color[turtle_index])
    tim.penup()
    tim.goto(x=-230,y=-y_position[turtle_index])
    all_turtles.append(tim)

if choose_color:
    is_race_on = True





while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if(winning_color == choose_color):
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")    
        distance = random.randint(0,10)
        turtle.forward(distance)





screen.exitonclick()