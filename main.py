from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=1200, height=650)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

color_index = 0
x_coordinate = -580
y_coordinate = 100
for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[color_index])
    new_turtle.penup()
    new_turtle.goto(x=x_coordinate, y=y_coordinate)
    color_index += 1
    y_coordinate -= 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 580:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner!")
            is_race_on = False
        else:
            for turtle in all_turtles:
                turtle.speed(5)
                turtle.forward(random.randint(1, 10))


screen.exitonclick()
