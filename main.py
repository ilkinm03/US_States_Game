import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

csv_data = "50_states.csv"
states_data = pandas.read_csv(csv_data)
states_list = states_data["state"].to_list()

answer_state = screen.textinput(
    title="Guess the State",
    prompt="What's another state's name?"
).title()

screen.exitonclick()
