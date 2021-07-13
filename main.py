from turtle import Turtle, Screen
import random

start_game = False
colours = ["red", "green", "yellow", "blue", "purple"]
starting_y = [60, 30, 0, -30, -60]
all_turtles = []
screen = Screen()
screen.setup(width=500, height=400)
prediction = screen.textinput("Your Prediction", "Enter colour : ")

for turtles in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtles])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=starting_y[turtles])
    all_turtles.append(new_turtle)

if prediction:
    start_game = True

while start_game:
    random_movement = random.randint(0, 10)
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_colour = turtle.pencolor()
            if winning_colour == prediction:
                print("You won")
            else:
                print(f"You lost. The winning colour is {winning_colour}.")
            start_game = False
        random_movement = random.randint(0, 10)
        turtle.forward(random_movement)

screen.exitonclick()
