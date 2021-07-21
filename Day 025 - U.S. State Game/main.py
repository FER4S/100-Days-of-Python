import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
screen.setup(725, 491)
screen.bgpic('blank_states_img.gif')

feras = turtle.Turtle()
feras.hideturtle()
feras.penup()

score = 0
data = pandas.read_csv('50_states.csv')
states = data.state.to_list()
guessed = []
is_on = True
while is_on:
    ans = screen.textinput(f'{score}/50 States Guessed!', 'Enter a state name: ').title()
    if ans in states and ans not in guessed:
        guessed.append(ans)
        score += 1
        state_data = data[data.state == ans]
        x = int(state_data.x)
        y = int(state_data.y)
        feras.goto(x, y)
        feras.write(f'{ans}', align='center', font=("Courier", 7, "normal"))
    if score == 50:
        is_on = False
        feras.color('red')
        feras.home()
        feras.write('You have guessed all the states right!', align='center', font=("Courier", 20, "bold"))
    if ans == 'Exit':
        # missed = []
        # for state in states:
        #     if state not in guessed:
        #         missed.append(state)
        missed = [state for state in states if state not in guessed]
        df = pandas.DataFrame(missed)
        df.to_csv('missed states.csv')
        break

screen.exitonclick()
