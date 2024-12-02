import turtle
import pandas as pd

US_MAP = "blank_states_img.gif"
ANSWERS = "50_states.csv"
TOTAL_STATES = 50

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
screen.addshape(US_MAP)
turtle.shape(US_MAP)

states_data = pd.read_csv(ANSWERS)

correct_guesses = 0
guessed_states = []

while correct_guesses != TOTAL_STATES:
    title = f"{correct_guesses}/{TOTAL_STATES} States Correct"
    answer_state = screen.textinput(
        title=title, prompt="What's another state's name?"
    ).title()

    if answer_state == "Exit":
        states_to_learn = states_data[~states_data.state.isin(guessed_states)].state
        print(states_to_learn)
        states_to_learn.to_csv("states_to_learn.csv", index=False)
        break
    correct_guess = states_data[states_data["state"] == answer_state]
    if len(correct_guess) > 0:
        # print(states_data[states_data["state"] == answer_state])
        # x = states_data[states_data["state"] == answer_state].iloc[0]["x"]
        # y = states_data[states_data["state"] == answer_state].iloc[0]["y"]
        state_data = states_data[states_data["state"] == answer_state]
        x = state_data.x.item()
        y = state_data.y.item()
        correct_guesses += 1
        guessed_states.append(answer_state)
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.goto(x, y)
        state.write(answer_state, align="center")

if correct_guesses == 50:
    print("You guessed them all!")
    exit()

turtle.mainloop()
