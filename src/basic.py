from random import randint, uniform
from time import sleep
import logging as log

framerate = 24  # In Frames Per Secound
grid_x = 50
grid_y = 50
ballno = 100
minvel = 5/framerate
maxvel = 10/framerate

log.basicConfig(level=log.INFO)
# Functions
def gen_render_array(balls, x_size, y_size, ball_char="0"):
    # https://stackoverflow.com/questions/240178/list-of-lists-changes-reflected-across-sublists-unexpectedly
    render_array = [[' ']*x_size for _ in range(y_size)]
    for ball in balls:
        loc = ball["loc"]
        try: render_array[round(loc[1])][round(loc[0])] = ball_char
        except: pass
    return render_array

# Frame simulate
def simulate_frame(balls, max_x, max_y):
    maxes = [max_x, max_y]
    # This loop goes through every ball and updates their positions.
    for ball in balls:
        # This loop goes through the indicies 0 and 1 to process the X and Y axis respectively.
        for i in range(2):
            # Move the ball one step at it's velocity.
            ball['loc'][i] += ball['velocity'][i]

            # If the ball goes off the side of the screen, this will 
            # flip the balls velocity in that direction and put the ball back onscreen.
            if ball['loc'][i] <= 0:
                ball['loc'][i] = 1
                ball['velocity'][i] *= -1
                
                log.debug(f"0 Edge bounce. New Velocity: {ball['velocity']}. New location: {ball['loc']}.")
            elif ball['loc'][i] >= maxes[i]:
                ball['velocity'][i] *= -1
                ball['loc'][i] = maxes[i]-1
                log.debug(f"Max edge bounce. New Velocity: {ball['velocity']}. New location: {ball['loc']}.")

    return balls

# Generate balls
balls = []
for n in range(ballno):
    balls.append({
        "loc": [randint(0, grid_x-1), randint(0, grid_y-1)],
        "velocity": [uniform(minvel, maxvel), uniform(minvel, maxvel)]
    })
print(balls)

# Main loop
while True:
    print("-"*grid_x*2)
    render_array = gen_render_array(balls, grid_x, grid_y)
    for line in render_array:
        print((" ".join(line)))
    sleep(1/framerate)
    balls = simulate_frame(balls, grid_x, grid_y)