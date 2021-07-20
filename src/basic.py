from random import randint
from time import sleep

grid_x = 20
grid_y = 20
ballno = 10
minvel = 1
maxvel = 1

# Functions
def gen_render_array(balls, x_size, y_size):
    # https://stackoverflow.com/questions/240178/list-of-lists-changes-reflected-across-sublists-unexpectedly
    render_array = [[' ']*x_size for _ in range(y_size)]
    for ball in balls:
        loc = ball["loc"]
        try: render_array[loc[1]][loc[0]] = "o"
        except: pass
    return render_array

# Frame simulate
def simulate_frame(balls, max_x, max_y):
    maxes = [max_x, max_y]
    for ball in balls:
        for i in range(2):
            if ball['loc'][i] <= 0 or ball['loc'][i] >= maxes[i]:
                ball['velocity'][i] *= -1
                print(ball['velocity'][i])
            ball['loc'][i] += ball['velocity'][i]

    return balls

# Generate balls
balls = []
for n in range(ballno):
    balls.append({
        "loc": [randint(0, grid_x-1), randint(0, grid_y-1)],
        "velocity": [randint(minvel, maxvel), randint(minvel, maxvel)]
    })
print(balls)

# Main loop
while True:
    print("-"*grid_x*2)
    render_array = gen_render_array(balls, grid_x, grid_y)
    for line in render_array:
        print((" ".join(line)))
    sleep(0.5)
    balls = simulate_frame(balls, grid_x, grid_y)