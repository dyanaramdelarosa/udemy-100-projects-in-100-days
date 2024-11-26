import turtle
import pandas as pd

US_MAP = "blank_states_img.gif"
ANSWERS = "50_states.csv"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(US_MAP)
turtle.shape(US_MAP)

states_data = pd.read_csv(ANSWERS)
print(states_data)

correct_guesses = 0
while correct_guesses != 50:
    answer_state = screen.textinput(
        title="Guess the state",
        prompt="What's another state's name?"
    )
    if states_data[states_data["state"] == answer_state]:
        x_coor = states_data[states_data["state"] == answer_state]["x"]
        y_coor = states_data[states_data["state"] == answer_state]["y"]
        correct_guesses += 1
        state = turtle.Turtle()
        state.penup()
        state.goto(x_coor, y_coor)
        state.write()

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
# screen.exitonclick()
