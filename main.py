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

found_states = []
while len(found_states) < states_count:
    answer_state = screen.textinput(
        title=f"Guess the State {len(found_states)}/{states_count}",
        prompt="What's another state's name?"
    ).title()
    if answer_state == "Exit":
        break
    if answer_state in states_list and answer_state not in found_states:
        found_states.append(answer_state)
        x = states_data[states_data.state == answer_state]["x"]
        y = states_data[states_data.state == answer_state]["y"]
        state_name.goto(int(x), int(y))
        state_name.write(answer_state, align="center", font=FONT)
