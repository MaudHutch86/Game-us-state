import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "image_start.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
# TODO Check if the guess is among the 50 states


data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
total_states = (len(states_list))
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} / {total_states} guessed states", prompt="What's another state's name?")
    user_guess = answer_state.capitalize()

    if user_guess == "Exit":
        states_to_learn = []
        for state in states_list:
            if state not in guessed_states:
                states_to_learn.append(state)
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    if user_guess in states_list:
        guessed_states.append(user_guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_item = data[data.state == user_guess]
        t.goto(int(state_item.x), int(state_item.y))
        t.write(user_guess)





screen.exitonclick()
