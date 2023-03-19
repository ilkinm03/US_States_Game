import turtle
import pandas

FONT = ("Arial", 8, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_name = turtle.Turtle()
state_name.hideturtle()
state_name.penup()

csv_data = "50_states.csv"
states_data = pandas.read_csv(csv_data)
states_list = states_data["state"].to_list()
states_count = len(states_list)

counter = 0
while counter < states_count:
    answer_state = screen.textinput(
        title=f"Guess the State {counter}/{states_count}",
        prompt="What's another state's name?"
    ).title()
    if answer_state in states_list:
        counter += 1
        x = states_data[states_data.state == answer_state]["x"]
        y = states_data[states_data.state == answer_state]["y"]
        state_name.goto(int(x), int(y))
        state_name.write(answer_state, align="center", font=FONT)

screen.exitonclick()
